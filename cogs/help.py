import discord
from discord.ext import commands

from constants import Constants


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(title='Fursona Pins', description='Available commands:', colour=Constants.embed_colour)
        embed.add_field(name='**.about**', value='Display information about the bot', inline=False)
        # embed.add_field(name='**.ch <name>**', value='Find a fursona pin based on the character name', inline=False)
        embed.add_field(name='**.id <Pin ID>**', value="Find a fursona pin based on it's ID", inline=False)
        embed.add_field(name='**.links**', value="Display links to various Fursona Pins' sites")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
