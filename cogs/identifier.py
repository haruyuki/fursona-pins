import json
import math

import aiohttp
import discord
from discord.ext import commands

from constants import Constants, FursonaPins

exceptions = {147, 200, 229, 318}


class Identifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spreadsheet = Constants.google_sheets_api.open_by_key('1bYyZmN_Bm5NGHpRL-ox-5sn5kqsTDLNiLuyrbsEcEbY')  # Link to conversion spreadsheet
        self.worksheet = self.spreadsheet.sheet1

    @staticmethod
    def get_column(identifier):
        first = 6
        multiplier = identifier/100
        if multiplier.is_integer():
            multiplier -= 1
        multiplier = math.floor(multiplier)
        return first + (3 * multiplier)

    @commands.command(aliases=['id'])
    @commands.guild_only()
    async def identifier(self, ctx, identifier: int):
        if identifier in exceptions:
            column = self.get_column(identifier)
            column_cells = self.worksheet.get_col(column, returnas='cell', include_tailing_empty=False)
            for cell in column_cells:
                if cell.value == identifier:
                    pin_name = cell.neighbour((0, 1)).value
                    pin_owner = cell.neighbour((0, 2)).value
                    if pin_owner == '':
                        pin_owner = 'No name provided'
                    break
            else:
                pin_name = 'Unknown'
                pin_owner = 'Unknown'

            title = f'{pin_name} (#{f"{identifier:03}"})'
            description = f'Owned by: {pin_owner}'
            file = discord.File(fp=f'exceptions/{identifier}.png', filename=f'{identifier}.png')
            embed = discord.Embed(title=title, description=description, colour=Constants.embed_colour)
            embed.set_image(url=f'attachment://{identifier}.png')
            embed.set_thumbnail(url=FursonaPins.banner_logo)
            await ctx.send(file=file, embed=embed)
            return

        if identifier <= 20:  # 1
            api_call = FursonaPins.fursona_pins_api + '1'
        elif identifier <= 40:  # 2
            api_call = FursonaPins.fursona_pins_api + '2'
        elif identifier <= 60:  # 3
            api_call = FursonaPins.fursona_pins_api + '3'
        elif identifier <= 80:  # 4
            api_call = FursonaPins.fursona_pins_api + '4'
        elif identifier <= 100:  # 5
            api_call = FursonaPins.fursona_pins_api + '5'
        elif identifier <= 120:  # 6
            api_call = FursonaPins.fursona_pins_api + '6'
        elif identifier <= 140:  # 7
            api_call = FursonaPins.fursona_pins_api + '7'
        elif identifier <= 161:  # 8
            api_call = FursonaPins.fursona_pins_api + '8'
        elif identifier <= 181:  # 9
            api_call = FursonaPins.fursona_pins_api + '9'
        elif identifier <= 202:  # 10
            api_call = FursonaPins.fursona_pins_api + '10'
        elif identifier <= 222:  # 11
            api_call = FursonaPins.fursona_pins_api + '11'
        elif identifier <= 243:  # 12
            api_call = FursonaPins.fursona_pins_api + '12'
        elif identifier <= 263:  # 13
            api_call = FursonaPins.fursona_pins_api + '13'
        elif identifier <= 283:  # 14
            api_call = FursonaPins.fursona_pins_api + '14'
        elif identifier <= 303:  # 15
            api_call = FursonaPins.fursona_pins_api + '15'
        elif identifier <= 324:  # 16
            api_call = FursonaPins.fursona_pins_api + '16'
        elif identifier <= 344:  # 17
            api_call = FursonaPins.fursona_pins_api + '17'
        elif identifier <= 364:  # 18
            api_call = FursonaPins.fursona_pins_api + '18'
        elif identifier <= 402:  # 19
            api_call = FursonaPins.fursona_pins_api + '19'
        else:  # 20+
            api_call = FursonaPins.fursona_pins_api + '20'

        async with aiohttp.ClientSession() as session:  # Create an AIOHTTP session
            async with session.get(api_call, headers=Constants.http_headers) as response:
                if response.status == 200:  # If received response is OK
                    connection = await response.text()  # Get text HTML of site
        data = json.loads(connection)
        data = data['data']
        for pin in data:
            if pin['pseudo'] == identifier:
                column = self.get_column(identifier)
                column_cells = self.worksheet.get_col(column, returnas='cell', include_tailing_empty=False)
                for cell in column_cells:
                    if cell.value == identifier:
                        pin_name = cell.neighbour((0, 1)).value
                        pin_owner = cell.neighbour((0, 2)).value
                        if pin_owner == '':
                            pin_owner = 'No name provided'
                        break
                else:
                    pin_name = 'Unknown'
                    pin_owner = 'Unknown'

                title = f'{pin_name} (#{f"{identifier:03}"})'
                description = f'Owned by: {pin_owner}'
                pin_image = 'https://www.fursonapins.com/' + pin['image'].replace('\\', '')
                embed = discord.Embed(title=title, description=description, colour=Constants.embed_colour)
                embed.set_image(url=pin_image)
                embed.set_thumbnail(url=FursonaPins.banner_logo)
                await ctx.send(embed=embed)
                return
        await ctx.send("There's no pin with that ID found :frowning:")


def setup(bot):
    bot.add_cog(Identifier(bot))
