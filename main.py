import datetime
import os
from os import environ

import discord
from discord.ext import commands

from utils.keep_alive import keep_alive
from utils.voice import connect_to_voice_channel

# Setting up intents
intents = discord.Intents.default()
intents.messages = True

# Creating the bot instance
bot = commands.Bot("!", self_bot=True, intents=intents)

# Store the start time of the bot
bot.start_time = datetime.datetime.now()

# Connect to voice channel when bot is ready
@bot.event
async def on_ready():
    print(f"This program has logged in to the account {bot.user}\n")
    # Connect to a voice channel if data is available
    await connect_to_voice_channel(bot)

# Load all commands in the commands directory
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")



# Keep the bot alive
keep_alive()

# Run the bot
bot.run(environ["token"], bot=False)