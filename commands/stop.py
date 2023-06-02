import discord
from discord.ext import commands
import os
import sys
import asyncio

class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx):
        """Stops the bot. Only usable by the bot owner."""
        if ctx.author == self.bot.user:
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
            await self.bot.logout()
            await self.bot.close()
            os._exit(0)

def setup(bot):
    bot.add_cog(Stop(bot))
