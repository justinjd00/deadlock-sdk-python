#!/usr/bin/env python3
"""Generates typed bindings from the Deadlock API OpenAPI spec.

Writes two modules:

* ``deadlock_sdk/_generated/schemas.py``: every schema as a ``TypedDict`` or
  ``Literal`` alias. TypedDicts cost nothing at runtime and never reject a
  response, so a field the API adds or drops cannot break callers.
* ``deadlock_sdk/_generated/api.py``: ``@overload`` signatures for every GET
  endpoint, so ``dl.api.get("/v1/assets/heroes")`` is typed end to end.

Usage::

    python scripts/generate.py            # download the live spec and regenerate
    python scripts/generate.py --check    # fail if the committed files are stale
    python scripts/generate.py --spec openapi.json
"""

from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

SPEC_URL = "https://api.deadlock-api.com/openapi.json"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "deadlock_sdk" / "_generated"

HEADER = '''"""Generated from {url} by scripts/generate.py. Do not edit by hand."""

# ruff: noqa
# fmt: off
from __future__ import annotations
'''

Schema = dict[str, Any]


def class_name(raw: str) -> str:
    name = re.sub(r"[^0-9a-zA-Z]+", " ", raw).title().replace(" ", "")
    if raw and raw[0].isupper() and re.fullmatch(r"[A-Za-z0-9_]+", raw):
        name = raw  # keep the spec's own PascalCase names untouched
    if not name or name[0].isdigit():
        name = f"T{name}"
    return name


def pascal(raw: str) -> str:
    return "".join(p[:1].upper() + p[1:] for p in re.split(r"[^0-9a-zA-Z]+", raw) if p)


def literal(values: list[Any]) -> str:
    return "Literal[" + ", ".join(json.dumps(v) if isinstance(v, str) else repr(v) for v in values) + "]"


class Generator:
    def __init__(self, spec: Schema) -> None:
        self.spec = spec
        self.schemas: dict[str, Schema] = spec.get("components", {}).get("schemas", {})
        self.names = {raw: class_name(raw) for raw in self.schemas}
        self.blocks: list[str] = []
        self.emitted: set[str] = set()

    # Types -----------------------------------------------------------------

    def type_of(self, schema: Schema | bool | None, hint: str) -> str:
        """Python type expression for a schema. Inline objects become named TypedDicts."""
        if schema is None or schema is True or schema == {}:
            return "Any"
        if schema is False:
            return "None"
        if "$ref" in schema:
            return self.names[schema["$ref"].rsplit("/", 1)[-1]]
        for key in ("oneOf", "anyOf"):
            if key in schema:
                return self.union([self.type_of(s, f"{hint}{i}") for i, s in enumerate(schema[key])])
        if "allOf" in schema:
            parts = schema["allOf"]
            return self.type_of(parts[0], hint) if len(parts) == 1 else "dict[str, Any]"
        if "const" in schema:
            return literal([schema["const"]])
        if "enum" in schema:
            values = [v for v in schema["enum"] if v is not None]
            expr = literal(values) if values else "None"
            return self.union([expr, "None"]) if None in schema["enum"] else expr

        types = schema.get("type")
        if isinstance(types, list):
            return self.union([self.type_of({**schema, "type": t}, hint) for t in types])
        if types == "null":
            return "None"
        if types == "boolean":
            return "bool"
        if types == "integer":
            return "int"
        if types == "number":
            return "float"
        if types == "string":
            return "bytes" if schema.get("format") == "binary" else "str"
        if types == "array":
            return f"list[{self.type_of(schema.get('items'), hint + 'Item')}]"
        if types == "object" or "properties" in schema or "additionalProperties" in schema:
            if schema.get("properties"):
                return self.typed_dict(hint, schema)
            extra = schema.get("additionalProperties")
            return (
                f"dict[str, {self.type_of(extra, hint + 'Value')}]"
                if isinstance(extra, dict)
                else "dict[str, Any]"
            )
        return "Any"

    @staticmethod
    def union(parts: list[str]) -> str:
        seen: list[str] = []
        for p in parts:
            for piece in p.split(" | ") if not p.startswith("Literal[") else [p]:
                if piece not in seen:
                    seen.append(piece)
        if "Any" in seen:
            return "Any"
        # None last reads naturally: `int | None`.
        seen.sort(key=lambda p: p == "None")
        return " | ".join(seen)

    def typed_dict(self, name: str, schema: Schema, doc: str | None = None) -> str:
        if name in self.emitted:
            return name
        self.emitted.add(name)
        required = set(schema.get("required", []))
        fields: list[tuple[str, str, str | None]] = []
        for prop, sub in schema.get("properties", {}).items():
            t = self.type_of(sub, name + pascal(prop))
            fields.append(
                (prop, t if prop in required else f"NotRequired[{t}]", (sub or {}).get("description"))
            )

        doc = doc or schema.get("description")
        functional = any(not p.isidentifier() or keyword.iskeyword(p) for p, _, _ in fields)
        if functional:
            body = ", ".join(f"{json.dumps(p)}: {json.dumps(t)}" for p, t, _ in fields)
            self.blocks.append(f"{name} = TypedDict({json.dumps(name)}, {{{body}}})\n")
            return name
        lines = [f"class {name}(TypedDict):"]
        if doc:
            lines.append(f'    """{clean_doc(doc)}"""')
        for p, t, d in fields:
            lines.append(f"    {p}: {t}")
            if d:
                lines.append(f'    """{clean_doc(d)}"""')
        if not fields:
            lines.append("    pass")
        self.blocks.append("\n".join(lines) + "\n")
        return name

    def schemas_module(self) -> str:
        for raw, schema in self.schemas.items():
            name = self.names[raw]
            if schema.get("properties"):
                self.typed_dict(name, schema)
            else:
                expr = self.type_of(schema, name)
                if expr != name:
                    doc = f'\n"""{clean_doc(schema["description"])}"""' if schema.get("description") else ""
                    self.blocks.append(f"{name}: TypeAlias = {json.dumps(expr)}{doc}\n")
        imports = "\nfrom typing import Any, Literal, TypedDict\n\nfrom typing_extensions import NotRequired, TypeAlias\n"
        names = sorted({self.names[r] for r in self.schemas})
        all_ = "\n__all__ = [\n" + "".join(f"    {json.dumps(n)},\n" for n in names) + "]\n"
        return HEADER.format(url=SPEC_URL) + imports + all_ + "\n\n" + "\n\n".join(self.blocks)

    # Endpoints -------------------------------------------------------------

    def endpoints(self) -> list[dict[str, Any]]:
        out = []
        for path, item in sorted(self.spec["paths"].items()):
            op = item.get("get")
            if not op:
                continue
            params = list(item.get("parameters", []) + op.get("parameters", []))
            path_params = [p for p in params if p.get("in") == "path"]
            query_params = [p for p in params if p.get("in") == "query"]
            base = pascal(op.get("operationId") or path) + "Get"
            ok = op.get("responses", {}).get("200", {}).get("content", {})
            if "application/json" in ok:
                response = self.type_of(ok["application/json"].get("schema"), base + "Response")
                kind = "json"
            elif any(k.startswith("text/") for k in ok):
                response, kind = "str", "text"
            elif ok:
                response, kind = "bytes", "bytes"
            else:
                response, kind = "None", "json"
            out.append(
                {
                    "path": path,
                    "summary": (op.get("summary") or "").strip(),
                    "path_type": self.param_dict(base + "Path", path_params, total=True)
                    if path_params
                    else None,
                    "query_type": self.param_dict(base + "Query", query_params, total=False)
                    if query_params
                    else None,
                    "query_required": any(p.get("required") for p in query_params),
                    "response": response,
                    "kind": kind,
                }
            )
        return out

    def param_dict(self, name: str, params: list[Schema], total: bool) -> str:
        schema = {
            "type": "object",
            "properties": {
                p["name"]: {**p.get("schema", {}), "description": p.get("description")} for p in params
            },
            "required": [p["name"] for p in params if p.get("required") or total],
        }
        return self.typed_dict(name, schema)

    def api_module(self) -> str:
        self.blocks = []
        endpoints = self.endpoints()
        params_blocks = self.blocks
        imports = (
            "\nfrom typing import TYPE_CHECKING, Any, Literal, TypedDict, overload\n\n"
            "from typing_extensions import NotRequired, TypeAlias\n\n"
            "from .schemas import *  # noqa: F403\n\n"
            "if TYPE_CHECKING:\n    from .._options import CallOptions\n"
        )
        paths = "GetPath: TypeAlias = " + literal([e["path"] for e in endpoints]) + "\n"
        kinds = (
            "RESPONSE_KIND: dict[str, str] = {\n"
            + "".join(
                f"    {json.dumps(e['path'])}: {json.dumps(e['kind'])},\n"
                for e in endpoints
                if e["kind"] != "json"
            )
            + "}\n"
        )

        def overloads(is_async: bool) -> str:
            lines = []
            prefix = "async " if is_async else ""
            for e in endpoints:
                args = ["self", f"path: Literal[{json.dumps(e['path'])}]"]
                kw = []
                if e["path_type"]:
                    kw.append(f"path_params: {e['path_type']}")
                if e["query_type"]:
                    kw.append(f"query: {e['query_type']}" + ("" if e["query_required"] else " | None = None"))
                kw.append("options: CallOptions | None = None")
                sig = ", ".join([*args, "*", *kw])
                body = f'"""{clean_doc(e["summary"])}"""' if e["summary"] else "..."
                lines.append(
                    f"    @overload\n    {prefix}def get({sig}) -> {e['response']}:\n        {body}\n"
                )
            return "\n".join(lines)

        mixins = (
            "class TypedGetMixin:\n"
            '    """Typed overloads for every GET endpoint. Implemented by the client."""\n\n'
            + overloads(False)
            + "\n    def get(self, path: str, *, path_params: Any = None, query: Any = None, options: Any = None) -> Any:\n"
            "        return self._request_get(path, path_params, query, options)\n\n"
            "    def _request_get(self, path: str, path_params: Any, query: Any, options: Any) -> Any:\n"
            "        raise NotImplementedError\n\n\n"
            "class AsyncTypedGetMixin:\n"
            '    """Async counterpart of TypedGetMixin."""\n\n'
            + overloads(True)
            + "\n    async def get(self, path: str, *, path_params: Any = None, query: Any = None, options: Any = None) -> Any:\n"
            "        return await self._request_get(path, path_params, query, options)\n\n"
            "    async def _request_get(self, path: str, path_params: Any, query: Any, options: Any) -> Any:\n"
            "        raise NotImplementedError\n"
        )
        return (
            HEADER.format(url=SPEC_URL)
            + imports
            + "\n\n"
            + paths
            + "\n"
            + kinds
            + "\n\n"
            + "\n\n".join(params_blocks)
            + "\n\n"
            + mixins
        )


def clean_doc(text: str) -> str:
    text = " ".join(text.split()).replace('"""', "'''").replace("\\", "\\\\")
    return text[:-1] + text[-1] + " " if text.endswith('"') else text


def load_spec(path: str | None) -> Schema:
    if path:
        return json.loads(Path(path).read_text())
    req = urllib.request.Request(SPEC_URL, headers={"User-Agent": "deadlock-sdk-python generator"})
    with urllib.request.urlopen(req, timeout=60) as res:
        return json.loads(res.read())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--spec")
    args = parser.parse_args()

    spec = load_spec(args.spec)
    gen = Generator(spec)
    files = {OUT / "schemas.py": gen.schemas_module()}
    files[OUT / "api.py"] = gen.api_module()
    files[OUT / "__init__.py"] = '"""Types generated from the Deadlock API OpenAPI spec."""\n'

    if args.check:
        stale = [p.name for p, text in files.items() if not p.exists() or p.read_text() != text]
        if stale:
            print(f"Generated files are out of date: {', '.join(stale)}. Run `python scripts/generate.py`.")
            return 1
        print("Generated types match the live API spec.")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    for p, text in files.items():
        p.write_text(text)
    print(f"Wrote {len(files)} files, {len(gen.schemas)} schemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
