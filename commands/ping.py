import discord
from discord.ext import commands
import datetime
import asyncio

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
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

def setup(bot):
    bot.add_cog(Ping(bot))
