from discord.ext import commands


class Character(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ch'])
    @commands.guild_only()
    async def character(self, ctx):
        await ctx.send('This command has not been implemented yet!')


def setup(bot):
    bot.add_cog(Character(bot))
