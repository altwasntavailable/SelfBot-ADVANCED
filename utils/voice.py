import discord
import json

async def connect_to_voice_channel(bot):
    with open("data/data.json", "r") as f:
        data = json.load(f)
    if data.get("guild") and data.get("channel"):
        try:
            guild_id = int(data["guild"])
            channel_id = int(data["channel"])
            guild = bot.get_guild(guild_id)
            voice_channel = discord.utils.get(guild.channels, id=channel_id)
            await voice_channel.connect()
            print("[-] Connected to a voice channel.")
        except Exception as e:
            print(f"[ - ] Error occurred while connecting to voice channel: {e}")
