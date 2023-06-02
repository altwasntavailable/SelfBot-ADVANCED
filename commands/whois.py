import discord
from discord.ext import commands
import asyncio

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, mention: discord.Member = None):
        """Shows information about a user (defaults to the author if no mention)."""
        if not mention:
            mention = ctx.author

        user_info = f"Name: {mention.name}#{mention.discriminator}\n"
        user_info += f"ID: {mention.id}\n"
        user_info += f"Joined Server: {mention.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        user_info += f"Joined Discord: {mention.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"

        common_servers = [guild.name for guild in self.bot.guilds if guild.get_member(mention.id)]
        user_info += f"Servers in Common: {', '.join(common_servers)}"

        message = f"```{user_info}```"
        sent_message = await ctx.send(message)
        await asyncio.sleep(10)
        await ctx.message.delete()
        await sent_message.delete()

def setup(bot):
    bot.add_cog(Whois(bot))
