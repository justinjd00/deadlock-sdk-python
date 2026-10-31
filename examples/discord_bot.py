"""A Discord bot with a /rank command, using the async client.

pip install deadlock-sdk discord.py
DISCORD_TOKEN=... python examples/discord_bot.py
"""

import os

import discord
from discord import app_commands

from deadlock_sdk import AsyncDeadlock, DeadlockError

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
dl = AsyncDeadlock(api_key=os.environ.get("DEADLOCK_API_KEY"))


@tree.command(description="Deadlock rank and recent form for a Steam id or profile URL")
async def rank(interaction: discord.Interaction, player: str) -> None:
    await interaction.response.defer()
    try:
        s = await dl.players.summary(player, matches=20)
    except DeadlockError as error:
        await interaction.followup.send(f"Could not load that player: {error.message}")
        return
    embed = discord.Embed(
        title=s.profile["personaname"] if s.profile else str(s.account_id),
        description=f"**{s.rank.label if s.rank else 'Unranked'}**\n"
        f"Last {s.recent.matches}: {s.recent.wins}W {s.recent.losses}L ({s.recent.win_rate:.0%}), KDA {s.recent.kda}",
        url=f"https://steamcommunity.com/profiles/{s.steam_id64}",
    )
    if s.rank and s.rank.image:
        embed.set_thumbnail(url=s.rank.image)
    for h in s.top_heroes[:3]:
        embed.add_field(name=h.name, value=f"{h.matches} games, {h.win_rate:.0%}")
    embed.set_footer(text="Data from the Deadlock API")
    await interaction.followup.send(embed=embed)


@bot.event
async def on_ready() -> None:
    await tree.sync()
    print(f"Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
