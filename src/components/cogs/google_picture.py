# importing required modules
import requests
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY1')

class GPictureCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='map')
    async def locationInMap(self, ctx, *args):

        location = ''.join(args)
        location = location.replace("ä", "a")  # Replacing unwanted characters.
        location = location.replace("ö", "o")  # Replacing unwanted characters.
        print(location)
        BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"

        # zoom value
        ZOOM = 13

        # updating the URL
        URL = BASE_URL + "center=" + location + "&zoom=" + \
            str(ZOOM) + "&size=500x500" + \
            "&markers=color:red%7C"+location+"&key=" + API_KEY
        # HTTP request
        print(URL)

        # I think there is better way to do this, but this way works...
        try:
            # If HTTP headers contains 'x-staticmap-api-warning', this way it catches the error and correct message can be displayed to the user
            if (requests.get(URL).headers["x-staticmap-api-warning"]):
                embed = discord.Embed(title="Map error", color=0x9e0035)
                embed.add_field(name="invalid parameter", value="Did you have a stroke? Or did you try to find map for the Fairyland?\nEither way this place you tried to find doesn't seem to exist. Please check your spelling or this time try with place that does exist :)\nBut hey, here's picture of ocean for you!",
                inline=False)
                await ctx.channel.send(embed=embed)
        # again, this feels really really really wrong way to do this but...
        # if there isn't 'x-static-map-warning', this except handles the anti-error
        # but hey, the code doesn't explode.. so am I an anti-errorist? :D
        except:
            print("Working as intended")

        # if no place was specified, this error message will be sent to the channel
        if len(args) < 1:
            embed = discord.Embed(title="Map error", color=0x9e0035)
            embed.add_field(name="no parameters", value="You didn't specify any location, probably you should try that. Unless you like to see a picture of ocean. I won't judge you.\nHere's the picture of nothing :)", inline=False)
            await ctx.channel.send(embed=embed)
        
        # sends the url to the channel and hopefully it converts to a picture
        await ctx.channel.send(URL)

def setup(bot):
    bot.add_cog(GPictureCog(bot))
