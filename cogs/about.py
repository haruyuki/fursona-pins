import textwrap

import discord
from discord.ext import commands

from constants import Constants, FursonaPins


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info'])
    @commands.guild_only()
    async def about(self, ctx):
        guild_count = len(self.bot.guilds)
        user_count = len(list(self.bot.get_all_members()))
        unique_user_count = len(set(self.bot.get_all_members()))

        description = f'''\
        **Created by:** `Haru#5616`
        **Running on:** `{guild_count} guilds`
        **Serving:** `{user_count} users ({unique_user_count} unique)`'''
        description = textwrap.dedent(description)

        embed = discord.Embed(title='Fursona Pins Discord Bot!', description=description, colour=Constants.embed_colour)
        embed.set_thumbnail(url=FursonaPins.banner_logo)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(About(bot))
