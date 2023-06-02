import discord
from discord.ext import commands
from pytz import timezone
import datetime
import asyncio

class Date(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def date(self, ctx):
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

def setup(bot):
    bot.add_cog(Date(bot))
