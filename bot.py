from __future__ import annotations

import discord
from discord.ext import commands

from dotenv import dotenv_values

config = dotenv_values(".env")
# checkign if it is a development stage or not
is_dev = config["ENVIRONMENT"] == "development"

intents = discord.Intents.all()
# Create a bot instance
bot = commands.Bot(
                command_prefix=config["DEFAULT_PREFIX"],
                intents=intents,
                help_command=None  # This should be comment out, If you wnat to use default help command. 
                )

@bot.event
async def on_ready():
    print(f'Ready as a {bot.user.name}!')

# Sample command
@bot.command(description="This is an test command.",
              hidden=not is_dev) # if it is not development then hide the command.
async def hello(ctx: commands.Context) -> None:
    """This is an test command."""
    await ctx.send(f"Hi! {ctx.author.display_name}")

# Run the bot
if __name__ == "__main__":
    bot.run(config["TOKEN"])
