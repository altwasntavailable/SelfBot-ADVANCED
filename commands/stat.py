import discord
from discord.ext import commands
import asyncio

class Stat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stat(self, ctx, status: str = None):
        valid_statuses = ['online', 'idle', 'dnd', 'invisible']
        
        if status is None or status.lower() not in valid_statuses:
            usage = f"Usage: `!stat <status>`\nValid statuses: {', '.join(valid_statuses)}"
            usage_msg = await ctx.send(usage)
            await asyncio.sleep(10)
            await ctx.message.delete()
            await usage_msg.delete()
            return

        # Set the bot's status
        if status.lower() == 'online':
            await self.bot.change_presence(status=discord.Status.online)
        elif status.lower() == 'idle':
            await self.bot.change_presence(status=discord.Status.idle)
        elif status.lower() == 'dnd':
            await self.bot.change_presence(status=discord.Status.dnd)
        elif status.lower() == 'invisible':
            await self.bot.change_presence(status=discord.Status.invisible)

        response = f"Status changed to: `{status}`"
        response_msg = await ctx.send(response)
        await asyncio.sleep(10)
        await ctx.message.delete()
        await response_msg.delete()

def setup(bot):
    bot.add_cog(Stat(bot))