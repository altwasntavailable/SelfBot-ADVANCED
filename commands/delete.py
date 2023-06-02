import discord
from discord.ext import commands
import asyncio

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, number: int):
        if number <= 0:
            usage_message = await ctx.send("Incorrect usage of the command. Please provide a valid number of messages to delete.")
            await asyncio.sleep(5)
            await usage_message.delete()
            await ctx.message.delete(delay=5)
            return

        messages = []
        async for message in ctx.channel.history(limit=number + 1):
            if message.author == self.bot.user:
                messages.append(message)

        if len(messages) == 0:
            await ctx.send("`No messages found to delete.`")
            await asyncio.sleep(5)
            return

        if len(messages) > 10:
            status_message = await ctx.send("`Deleting messages. This may take a moment...`")
            for message in messages:
                await message.delete(delay=1)
                await asyncio.sleep(1)
            await status_message.delete()
            delete_message = await ctx.send(f"`Deleted {len(messages)} messages.`")
            await asyncio.sleep(3)
            await delete_message.delete()
        else:
            for message in messages:
                await message.delete()
            delete_message = await ctx.send(f"Deleted {len(messages)} messages.")
            await asyncio.sleep(3)
            await delete_message.delete()
        await ctx.message.delete(delay=3)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            error_message = await ctx.send("Please provide the number of messages to delete.")
            await asyncio.sleep(5)
            await error_message.delete()
            await ctx.message.delete(delay=5)

def setup(bot):
    bot.add_cog(Delete(bot))
