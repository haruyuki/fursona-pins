import discord
from discord.ext import commands

from constants import FursonaPins


class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def links(self, ctx):
        embed = discord.Embed(title='Fursona Pins Links', description="A list of everything Fursona Pins!")
        embed.set_thumbnail(url=FursonaPins.banner_logo)
        embed.add_field(name='Website', value=FursonaPins.website, inline=False)
        embed.add_field(name='Patreon', value=FursonaPins.patreon, inline=False)
        embed.add_field(name='Trello', value=FursonaPins.trello, inline=False)
        embed.add_field(name='Twitter', value=FursonaPins.twitter, inline=False)
        embed.add_field(name='Instagram', value=FursonaPins.instagram, inline=False)
        embed.add_field(name='Facebook', value=FursonaPins.facebook, inline=False)
        embed.add_field(name='Discord', value=FursonaPins.discord, inline=False)
        embed.add_field(name='Telegram', value=FursonaPins.telegram, inline=False)
        embed.add_field(name='Checklist Spreadsheet', value=FursonaPins.checklist_spreadsheet, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Links(bot))
