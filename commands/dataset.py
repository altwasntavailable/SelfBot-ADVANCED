import discord
from discord.ext import commands
import json
import asyncio
import os
import sys

class Dataset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dataset(self, ctx, guild_id: int, channel_id: int):
        """Edit the data.json file with new guild and channel IDs and restart the bot."""
        data = {
            "guild": str(guild_id),
            "channel": str(channel_id)
        }

        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)

        message = await ctx.send("`Data has been set. Restarting...`")
        await asyncio.sleep(5)
        await ctx.message.delete()  # Delete the dataset command message
        await message.delete()

        try:
            await self.restart_bot(ctx, message)
        except discord.NotFound:
            print("Restart message not found. Skipping restart.")

    @dataset.error
    async def dataset_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message = await ctx.send("Missing required arguments. Usage: `!dataset <guild_id> <channel_id>`")
        elif isinstance(error, commands.BadArgument):
            message = await ctx.send("Invalid arguments. Please provide valid guild and channel IDs.")
        else:
            message = await ctx.send("An error occurred while processing the command.")

        await asyncio.sleep(5)
        await ctx.message.delete()  # Delete the dataset command message
        await message.delete()

    async def restart_bot(self, ctx, restart_message):
        print("Restarting in 20 seconds...")
        for i in range(20, 0, -1):
            print(f"Rebooting: {i}")
            await asyncio.sleep(1)

        print("Restarting...")
        try:
            await restart_message.edit(content="`Restarting...`")
        except discord.NotFound:
            print("Restart message not found. Skipping message edit.")

        python = sys.executable
        os.execl(python, python, *sys.argv)


def setup(bot):
    bot.add_cog(Dataset(bot))