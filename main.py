import discord
from discord.ext import commands
import datetime
from pytz import timezone
from keep_alive import keep_alive
from os import environ
import asyncio
import json
import os
import sys

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
    if ctx.author == bot.user:
        message = await ctx.send("`Restarting... This may take a while.`")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

        await asyncio.sleep(20)
        await bot.logout()
        await bot.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

# Command: Stop the bot
@bot.command()
async def stop(ctx):
    if ctx.author == bot.user:
        message = await ctx.send("`Stopping... This may take a while.`")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

        await asyncio.sleep(20)
        await bot.logout()
        await bot.close()
        os._exit(0)

# Command: Time
@bot.command()
async def date(ctx):
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

# Event: Bot mentions
last_mention_time = datetime.datetime.now()

@bot.event
async def on_message(message):
    global last_mention_time

    if bot.user.mentioned_in(message):
        current_time = datetime.datetime.now()
        time_diff = current_time - last_mention_time

        if time_diff.total_seconds() > 50:  # Check if enough time has passed since the last mention
            response = "Apologies, but I am currently occupied. Please send me a DM and I'll get back to you ASAP."
            reply = await message.channel.send(response)
            last_mention_time = current_time

            await asyncio.sleep(20)
            await reply.delete()

    await bot.process_commands(message)


# Keep the bot alive
keep_alive()

# Run the bot
bot.run(environ["token"], bot=False)
