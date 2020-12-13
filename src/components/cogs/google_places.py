import googlemaps
import pprint
import time
import discord
import requests
import urllib
import json
import os
from discord.ext import commands
from dotenv import load_dotenv


# Awakening google platform key, reading a local file.
load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY1')
# Opening a different API-key for MAPQUEST.
api_key = os.getenv('API_KEY2')


class GPlacesCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='places')
    async def extract_lat_long_via_address(self, ctx, *args):

        try:
            # First error check - indicating the user to be more specific so that the search works.

            if (len(args) < 2):

                embed = discord.Embed(title="Nearby Places", color=0xf2680c)
                embed.add_field(name="Error", value="Please input the command -places followed by a SPACE and the address as specifically as you can. E.G. -places Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                inline=False)
                # Sending error message.
                await ctx.channel.send(embed=embed)

            else:

                # Splitting the "-places" start-predicative from the actual wanted String.
                address_initial = ' '.join(args)
                # Replacing unwanted characters.
                address_initial = address_initial.replace("ä", "a")
                # Replacing unwanted characters.
                address_initial = address_initial.replace("ö", "o")
                # Splitting the string given, only the address-part remains. E.G. -places Marsinkuja 1, Vantaa => "Marsinkuja 1, Vantaa".
                addressForReplacement = address_initial

                # Error checking for the below IF-clause.
                #address_error_check = addressForReplacement.split(" ")

                if (len(args) < 2 or len(args) < 1):
                    embed = discord.Embed(
                        title="Nearby Places", color=0xf2680c)
                    embed.add_field(name="Error", value="Please input the command -places followed by a SPACE and the address as specifically as you can. E.G. -places Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                    inline=False)
                    await ctx.channel.send(embed=embed)

                else:

                    # Replacing every SPACE string with another string that indicates space. Replace() -function, built-in with Python.
                    address = addressForReplacement.replace(" ", "%20")

                    url = "https://www.mapquestapi.com/geocoding/v1/address?key=" + api_key + \
                        "&inFormat=kvp&outFormat=json&location=" + address + "&thumbMaps=false"

                    # Opening and reading and converting to JSON the coordinates-dict with location attributes.
                    with urllib.request.urlopen(url) as response:
                        html = response.read()
                        # Loads the whole datapoint as JSON.
                        data = json.loads(html)

                    # Setting the desired coordinates from the JSON-output.
                    coordLat = data["results"][0]["locations"][0]["latLng"]["lat"]
                    coordLng = data["results"][0]["locations"][0]["latLng"]["lng"]

                    # Getting the google platform key
                    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
                    # Google maps own dictionary methods and places find

                    # Using the desired coordinates with gmaps-API. Making int to String conversion for the URL so that it is not N/A.
                    places_result = gmaps.places_nearby(location=str(
                        coordLat)+","+str(coordLng), radius=1000, open_now=False, type="restaurant")
                    print(places_result)
                    # Bot message awakening and later on adding the address

                    # Opening the list and checking if there are any results - no ERRORS are given when there are no places, THUS creating an informative output.
                    if (len(places_result["results"]) <= 0):

                        embed = discord.Embed(
                            title="Nearby Places", color=0xf2680c)
                        embed.add_field(name="Error", value="Could not find any nearby places. Maybe be more specific? Please input the command -places followed by a SPACE and the address as specifically as you can. E.G. -places Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                        inline=False)
                        await ctx.channel.send(embed=embed)

                    else:

                        # Limiting the results to 7 from the desired list...
                        for place in places_result['results'][:5]:
                            # ... These are within 1 km of the desired address. 20 places is the default - too much SPAM on the user's part.

                            # naming place id
                            my_place_id = place['place_id']
                            # naming fields that we want to be seen from the json list
                            my_fields = ['name', 'formatted_address',
                                         'formatted_phone_number']

                            # goooglemaps' own method for place find with my_fields and place_id
                            place_details = gmaps.place(
                                place_id=my_place_id, fields=my_fields)

                            # discords own embed style for clean message
                            embed = discord.Embed(
                                color=0xf2680c, title="Places: ")
                            embed.add_field(
                                name="Name: ", value=place_details['result']['name'], inline=True)
                            embed.add_field(
                                name="Address: ", value=place_details["result"]["formatted_address"], inline=True)

                            # Correcting Keyerrors
                            try:
                                embed.add_field(
                                    name="Phone number: ", value=place_details["result"]['formatted_phone_number'], inline=True)
                            except KeyError:
                                embed.add_field(name="Phone number: ",
                                                value="No number", inline=True)

                            # Sending places to discord bot
                            await ctx.channel.send(embed=embed)

        except:  # ERROR checking. The last resort. Cacthes anything that went by the above ERROR checks.
            embed = discord.Embed(title="Nearby Places", color=0xf2680c)
            embed.add_field(name="Error", value="Please input the command -places followed by a SPACE and the address as specifically as you can. E.G. -places Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                            inline=False)


def setup(bot):
    bot.add_cog(GPlacesCog(bot))
