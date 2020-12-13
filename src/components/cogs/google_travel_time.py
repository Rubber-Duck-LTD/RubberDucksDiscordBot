import requests  # New module dependency.
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


# Google API key
load_dotenv()
api_key = os.getenv('API_KEY1')


class GDistanceCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='distance', aliases=['dist'])
    # message props for distance
    async def distancetime(self, ctx, arg1, arg2, arg3=None):
        # splitting command from spaces

        # Picking the citys after command(spaces)
        home = arg1.lower()
        home = home.replace("ä", "a")  # Replacing unwanted characters.
        home = home.replace("ö", "o")  # Replacing unwanted characters.
        work = arg2.lower()
        work = work.replace("ä", "a")  # Replacing unwanted characters.
        work = work.replace("ö", "o")  # Replacing unwanted characters.

        # Googlemaps url for distancematrix
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"

        # Implementing our own information to url and apikey
        r = requests.get(url + "origins=" + home +
                         "&destinations=" + work + "&key=" + api_key)
        response = r
        print(response)

        try:
            # forming our wanted output from json
            time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
            travel = r.json()["rows"][0]["elements"][0]["distance"]["text"]
            print(travel)

            # error message for wrong input
            if (arg3 is not None):

                embed = discord.Embed(title="Distance Time", color=0xf2680c)
                embed.add_field(name="Error",
                                value="Please input the command followed by a SPACE wanted location and "
                                "SPACE Wanted destination \n For example: -distance Helsinki Tampere "
                                "\n or \n -distance Isonniitynkatu5 Meri-rastilantie19 "
                                "Addresses need to be written with no spaces",
                                inline=False)

            # message for correct input
            else:
                embed = discord.Embed(
                    title="Distance Time", color=0xf2680c)
                embed.add_field(name="Time: ",
                                value=time,
                                inline=True)
                embed.add_field(name="Travel: ",
                                value=travel,
                                inline=True)

        # message for key errors | Important to remember; certain fields must have values, otherwise unwanter errors.
        except KeyError:

            embed = discord.Embed(title="Distance Time", color=0xf2680c)
            embed.add_field(name="Cars do not fly",
                            value="Don't put your destination or location over seas.", inline=False)
            embed.add_field(name="Error",
                            value="Please input the command followed by a SPACE wanted location and "
                            "SPACE Wanted destination \n For example: -distance Helsinki Tampere "
                            "\n or \n -distance Isonniitynkatu5 Meri-rastilantie19 "
                            "Addresses need to be written with no spaces",
                            inline=False)

            # message for any other exception
        except:
            embed.add_field(name="Error",
                            value="Something went wrong - please input the command followed by a"
                            " SPACE wanted location and SPACE Wanted destination \n "
                            "For example: -distance Helsinki Tampere \n or \n -distance Isonniitynkatu5 Meri-rastilantie19. "
                            "\n Addresses need to be written with no spaces",
                            inline=False)

        # Sending message to discord
        await ctx.channel.send(embed=embed)


# Error for discords own errors that may occur

    @distancetime.error
    async def deistancetime_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Distance Time", color=0xf2680c)
            embed.add_field(name="Error",
                            value="Please input the command followed by a SPACE wanted location and "
                            "SPACE Wanted destination \n For example: -distance Helsinki Tampere "
                            "\n or \n -distance Isonniitynkatu5 Meri-rastilantie19 "
                            "Addresses need to be written with no spaces",
                            inline=False)
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(GDistanceCog(bot))
