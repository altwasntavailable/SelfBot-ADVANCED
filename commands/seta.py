from discord.ext import commands
import discord
import asyncio

class Seta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def seta(self, ctx, activity_type: str, *, activity_name: str = None):
        """Changes the bot's activity."""
        valid_types = ["playing", "listening"]

        if activity_type.lower() not in valid_types and activity_type.lower() != "c":
            message = await ctx.send("Invalid activity type. Please choose one of the following: `playing`, `listening`, `c`.")
            await asyncio.sleep(10)
            await ctx.message.delete()
            await message.delete()
            return

        if activity_type.lower() == "c":
            await self.bot.change_presence(activity=None)
            message = await ctx.send("`Cleared activity.`")
            await asyncio.sleep(10)
            await ctx.message.delete()
            await message.delete()
            return

        if not activity_name:
            message = await ctx.send("Missing activity name. Usage: `!seta <activity_type> <activity_name>`")
            await asyncio.sleep(10)
            await ctx.message.delete()
            await message.delete()
            return

        if activity_type.lower() == "playing":
            activity = discord.Game(name=activity_name)
        elif activity_type.lower() == "listening":
            activity = discord.Activity(type=discord.ActivityType.listening, name=activity_name)

        await self.bot.change_presence(activity=activity)

        message = await ctx.send(f"Changed activity to: `{activity_type.capitalize()} {activity.name}`")
        await asyncio.sleep(10)
        await ctx.message.delete()
        await message.delete()

    @seta.error
    async def seta_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message = await ctx.send("Missing required arguments. Usage: `!seta <activity_type> <activity_name>`")
            await asyncio.sleep(10)
            await ctx.message.delete()
            await message.delete()
        else:
            raise error

def setup(bot):
    bot.add_cog(Seta(bot))
