import requests
import json
import urllib
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Opening a different API-key for MAPQUEST.
load_dotenv()
api_key = os.getenv('API_KEY2')


class HEventsCog(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    @commands.command(name='events')
    async def helsinki_events(self, ctx, *args):

        try:

            if (len(args) < 2):

                embed = discord.Embed(title="Events Nearby", color=0xd283ed)
                embed.add_field(name="Error",
                                value="Please input the command -events followed by a SPACE and the address as specifically as you can. E.G. -events Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                inline=False)
                # Sending error message.
                await ctx.channel.send(embed=embed)
            else:

                address_initial = ' '.join(args)
                # Splitting the string given, only the address-part remains. E.G. -places Marsinkuja 1, Vantaa => "Marsinkuja 1, Vantaa".
                address_initial = address_initial.replace("ä", "a")
                # Replacing unwanted characters.
                address_initial = address_initial.replace("ö", "o")
                # Splitting the string given, only the address-part remains. E.G. -places Marsinkuja 1, Vantaa => "Marsinkuja 1, Vantaa".
                addressForReplacement = address_initial

                print(len(args))  # DEBUGGING.
                print(args)  # DEBUGGING.

                if (len(args) < 2 or len(args) < 1 or len(args) >= 5):
                    embed = discord.Embed(
                        title="Nearby Places", color=0xd283ed)
                    embed.add_field(name="Error",
                                    value="Please input the command -places followed by a SPACE and the address as specifically as you can. E.G. -places Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                    inline=False)
                    await ctx.channel.send(embed=embed)

                else:

                    addressForReplacement = address_initial

                    # Replacing every SPACE string with another string that indicates space. Replace() -function, built-in with Python.
                    address = addressForReplacement.replace(" ", "%20")

                    url_map = "https://www.mapquestapi.com/geocoding/v1/address?key=" + api_key + \
                              "&inFormat=kvp&outFormat=json&location=" + address + "&thumbMaps=false"

                    with urllib.request.urlopen(
                            url_map) as response:  # Opening and reading and converting to JSON the coordinates-dict with location attributes.
                        html = response.read()
                        # Loads the whole datapoint as JSON.
                        data = json.loads(html)
                        print(data)  # DEBUGGING.

                    # Setting the desired coordinates from the JSON-output.
                    coordLat = data["results"][0]["locations"][0]["latLng"]["lat"]
                    coordLng = data["results"][0]["locations"][0]["latLng"]["lng"]

                    url = 'http://open-api.myhelsinki.fi/v1/events/?distance_filter=' + str(coordLat) + '%2C' + str(
                        coordLng) + '%2C2100'
                    data_2 = requests.get(url).json()

                    if (len(data_2["data"]) <= 0):

                        embed = discord.Embed(
                            title="Events Nearby", color=0xd283ed)
                        embed.add_field(name="Error",
                                        value="Could not find any nearby events. Maybe be more specific? Please input the command -events followed by a SPACE and the address as specifically as you can. E.G. -events Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                                        inline=False)
                        #print("Got here.")
                        await ctx.channel.send(embed=embed)

                    else:
                        print("Got here.") # Debugging. Fixed multiple duplicate moments.
                        for events in data_2['data'][:5]:
                            print("Got here INSIDE FOR EVENTS IN.") # Debugging.
                            embed = discord.Embed(
                                color=0xd283ed, title="Events ")

                            try:
                                embed.add_field(
                                    name="Name: ", value=events['name']['fi'], inline=True)
                            except KeyError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            except IndexError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            try:
                                embed.add_field(
                                    name="Address: ", value=events["location"]["address"]['street_address'],
                                    inline=True)

                            except KeyError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            except IndexError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            try:
                                embed.add_field(
                                    name="Description: ", value=events["description"]["intro"], inline=False)
                            except KeyError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            except IndexError:
                                embed.add_field(
                                    name="Description: ", value="No desc", inline=False)
                            try:
                                embed.set_thumbnail(
                                    url=events["description"]["images"][0]['url'])
                            except KeyError:
                                embed.set_thumbnail(
                                    url="https://upload.wikimedia.org/wikipedia/commons/f/fc/No_picture_available.png")
                            except IndexError:
                                embed.set_thumbnail(
                                    url="https://upload.wikimedia.org/wikipedia/commons/f/fc/No_picture_available.png")
                            try:
                                embed.add_field(
                                    name="Event link: ", value=events["info_url"], inline=False)
                            except KeyError:
                                embed.add_field(
                                    name="Event link: ", value="No link", inline=False)
                            except IndexError:
                                embed.add_field(
                                    name="Event link: ", value="No link", inline=False)

                            await ctx.channel.send(embed=embed)

        except:
            embed = discord.Embed(title="Events Nearby", color=0xd283ed)
            embed.add_field(name="Error",
                            value="Please input the command -events followed by a SPACE and the address as specifically as you can. E.G. -events Kaivokatu 1, Helsinki, Finland. This ensures that you get as accurate information as possible.",
                            inline=False)


def setup(bot):
    bot.add_cog(HEventsCog(bot))
