import discord
from discord.ext import commands
import datetime
from pytz import timezone
from keep_alive import keep_alive
import asyncio
import json
import os
from os import environ
import sys
import psutil

# Setting up intents
intents = discord.Intents.default()
intents.messages = True

# Creating the bot instance
bot = commands.Bot("!", self_bot=True, intents=intents)

# Store the start time of the bot
start_time = datetime.datetime.now()

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"This program has logged in to the account {bot.user}\n")

    # Set the bot's activity
    activity = discord.Activity(type=discord.ActivityType.listening, name="The voices in my head")
    await bot.change_presence(activity=activity)

    # Connect to a voice channel if data is available
    with open("data.json", "r") as f:
        data = json.load(f)
    if data.get("guild") and data.get("channel"):
        try:
            guild_id = int(data["guild"])
            channel_id = int(data["channel"])
            guild = bot.get_guild(guild_id)
            voice_channel = discord.utils.get(guild.channels, id=channel_id)
            await voice_channel.connect()
            print(f"[-] Connected to {voice_channel} in {voice_channel.guild}.")
        except Exception as e:
            print(f"[ - ] Error occurred while connecting to voice channel: {e}")

# Command: Uptime
@bot.command()
async def uptime(ctx):
    """Displays the bot's uptime."""
    uptime = datetime.datetime.now() - start_time
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    message = await ctx.send(f"Bot has been up for `{days} days`, `{hours} hours`, `{minutes} minutes`.")
    await asyncio.sleep(10)
    await ctx.message.delete()
    await message.delete()

# Command: Whois
@bot.command()
async def whois(ctx, mention: discord.Member = None):
    """Shows information about a user (defaults to the author if no mention)."""
    if not mention:
        mention = ctx.author

    user_info = f"Name: {mention.name}#{mention.discriminator}\n"
    user_info += f"ID: {mention.id}\n"
    user_info += f"Joined Server: {mention.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
    user_info += f"Joined Discord: {mention.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"

    common_servers = [guild.name for guild in bot.guilds if guild.get_member(mention.id)]
    user_info += f"Servers in Common: {', '.join(common_servers)}"

    message = f"```{user_info}```"
    sent_message = await ctx.send(message)
    await asyncio.sleep(10)
    await ctx.message.delete()
    await sent_message.delete()

# Command: Restart the bot
@bot.command()
async def restart(ctx):
    """Restarts the bot. Only usable by the bot owner."""
    if ctx.author == bot.user:
        print("Restart has been started.")
        message = await ctx.send("`Restarting... This may take a while.`")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

        countdown = 20
        while countdown > 0:
            print(f"Rebooting in {countdown} seconds...")
            await asyncio.sleep(1)
            countdown -= 1

        print("Rebooting...")
        await bot.logout()
        await bot.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

# Command: Stop the bot
@bot.command()
async def stop(ctx):
    """Stops the bot. Only usable by the bot owner."""
    if ctx.author == bot.user:
        print("Stop has been initiated.")
        message = await ctx.send("`Stopping... This may take a while.`")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

        countdown = 20
        while countdown > 0:
            print(f"Stopping in {countdown} seconds...")
            await asyncio.sleep(1)
            countdown -= 1

        print("Stopping...")
        await bot.logout()
        await bot.close()
        os._exit(0)

# Command: Date
@bot.command()
async def date(ctx):
    """Displays the current date and time in a specific timezone."""
    current_time = datetime.datetime.now(timezone('Africa/Tunis'))
    day = current_time.day
    month = current_time.month
    year = current_time.year
    time = current_time.strftime("%I:%M %p")
    message = await ctx.send(f"Current date is: `{day}/{month}/{year}`, `{time}` `GMT+1`")
    await asyncio.sleep(20)
    await ctx.message.delete()
    await message.delete()

@bot.command()
async def ping(ctx):
    """Displays the bot's latency."""
    start_time = datetime.datetime.now()

    # Send a message and calculate the bot's latency
    message = await ctx.send("`Pinging...`")
    latency = datetime.datetime.now() - start_time
    ping = latency.total_seconds() * 1000

    # Edit the message with the ping value
    await message.edit(content=f"Pong! Latency: `{ping}ms`")

    # Delete the command message after 10 seconds
    await asyncio.sleep(10)
    await ctx.message.delete()
    await message.delete()

@bot.command()
async def seta(ctx, activity_type: str, *, activity_name: str):
    """Changes the bot's activity."""
    valid_types = ["playing", "listening"]

    if activity_type.lower() not in valid_types:
        message = await ctx.send("Invalid activity type. Please choose one of the following: `playing`, `listening`.")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()
        return

    if activity_type.lower() == "playing":
        activity = discord.Game(name=activity_name)
    elif activity_type.lower() == "listening":
        activity = discord.Activity(type=discord.ActivityType.listening, name=activity_name)

    await bot.change_presence(activity=activity)

    message = await ctx.send(f"Changed activity to: `{activity_type.capitalize()} {activity.name}`")
    await asyncio.sleep(10)
    await ctx.message.delete()
    await message.delete()

# Command: Record CPU and memory usage
@bot.command()
async def rec(ctx):
    """Records CPU and memory usage for a specified duration."""
    duration = 60  # Duration to display the results (in seconds)
    interval = 1  # Interval between updates (in seconds)

    message = await ctx.send("`Recording CPU and memory usage...`")
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)

    while datetime.datetime.now() < end_time:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        await message.edit(content=f"CPU Usage: `{cpu_usage}%` | Memory Usage: `{memory_usage}%`")
        await asyncio.sleep(interval)

    await message.edit(content=f"`Recording complete.`")
    await asyncio.sleep(10)
    await ctx.message.delete()
    await message.delete()

# Keep the bot alive
keep_alive()

# Run the bot
bot.run(environ["token"], bot=False)
