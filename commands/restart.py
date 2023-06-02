import os
import sys
import asyncio
from discord.ext import commands

@commands.command()
async def restart(ctx):
    """Restarts the bot. Only usable by the bot owner."""
    if ctx.author == ctx.bot.user:
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
        await ctx.bot.logout()
        await ctx.bot.close()
        os.execl(sys.executable, sys.executable, *sys.argv)

def setup(bot):
    bot.add_command(restart)
