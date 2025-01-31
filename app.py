import discord
from discord.ext import commands
import os

# Load bot token from environment variable (set this in your system or .env file)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set bot command prefix
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: DISCORD_BOT_TOKEN not found. Set it as an environment variable.")
