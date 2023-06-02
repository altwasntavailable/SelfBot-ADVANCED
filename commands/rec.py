import datetime
import psutil

from discord.ext import commands
import asyncio


class Rec(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rec(self, ctx):
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


def setup(bot):
    bot.add_cog(Rec(bot))
