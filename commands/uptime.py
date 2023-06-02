import datetime
from discord.ext import commands
import asyncio

# Command: Uptime
@commands.command()
async def uptime(ctx):
    """Displays the bot's uptime."""
    uptime = datetime.datetime.now() - ctx.bot.start_time
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    message = await ctx.send(f"Bot has been up for `{days} days`, `{hours} hours`, `{minutes} minutes`.")
    await asyncio.sleep(10)
    await ctx.message.delete()
    await message.delete()

def setup(bot):
    bot.add_command(uptime)
