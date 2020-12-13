import urllib.request
import json
import discord
from discord.ext import commands

# Importing necessary sections.

with urllib.request.urlopen("https://api.covid19api.com/summary") as response:
    html = response.read()
    data = json.loads(html)  # Loads the whole datapoint as JSON.


class CovidCog(commands.Cog): # Starts with "-".

    def __init__(self, bot):
        self.bot = bot

    # print(data)

    @commands.group(name='covid', aliases=['virus', 'cov', 'c'], invoke_without_command=True)
    async def covidInformation(self, ctx, *args): # Starts with "-", accepts command groups, and then args. Push something new.

        print(args)

        if (len(args) == 0):

            embed = discord.Embed(title="Covid Information (Global)",
                                  color=0x42d8a8)

            # if (message == "-covid"):
            embed.set_thumbnail(
                url='https://unhabitat.org/themes/custom/habitat/images/icons/covid-19-campaign-icon-black.png')
            embed.add_field(name="New recovered cases:  ",
                            value=str("{:,}".format(data["Global"]["NewConfirmed"])), inline=True)
            embed.add_field(name="Total confirmed cases:    ",
                            value=str("{:,}".format(data["Global"]["TotalConfirmed"])), inline=True)
            embed.add_field(name="New deaths:   ",
                            value=str("{:,}".format(data["Global"]["NewDeaths"])), inline=True)
            embed.add_field(name="Total deaths:  ",
                            value=str("{:,}".format(data["Global"]["TotalDeaths"])), inline=True)
            embed.add_field(name="Recovered individuals:    ",
                            value=str("{:,}".format(data["Global"]["NewRecovered"])), inline=True)
            embed.add_field(name="Total recovered:  ",
                            value=str("{:,}".format(data["Global"]["TotalRecovered"])), inline=True)
            # embed.set_image(url='https://unhabitat.org/themes/custom/habitat/images/icons/covid-19-campaign-icon-black.png')
            """embed.add_field(name=(message.content.split("i")),
                            value="• Total recovered individuals: " + str("{:,}".format(data["Global"]["TotalRecovered"])), inline=False)"""




        else:

            i = -1

            # Error-checking if the list contains more than two strings; inputs an error message.
            if (len(args) >= 2):
                embed = discord.Embed(
                    title="Covid Information", color=0x42d8a8)
                embed.add_field(name="Error",
                                value="Please input the command followed by a SPACE and the country name. Country name must be without spaces. E.G. country [Holy See (Vatican City State)] is typed as [holy-see-vatican-city-state].",
                                inline=False)

            else:

                try:  # Error-handling.
                    # "_" implies that the variable/parameter is not needed; just iterating through the list.
                    def convertTuple(tup):
                        string = ''.join(tup)
                        return string

                    tuple = (args[0])
                    string = convertTuple(tuple)
                    print(string)
                    for _ in data["Countries"]:
                        i = (i + 1)

                        # Comparing to Slug-attribute; these are more prone to be error free, since...
                        if (string.lower() == data["Countries"][i]["Slug"]):
                            # ... all the country names are joined e.g. by "-"; they are still one string without spaces. Splitting works now.
                            embed = discord.Embed(
                                color=0x42d8a8, title="Covid Information " + string.lower().capitalize())
                            # If the user inputs e.g. finland, will be displayed...
                            # ... as Finland. Capitalizing the firt letter of the String-type data.

                            # Added an image to the printing. Cleaned up the front-end style.
                            embed.set_thumbnail(
                                url='https://unhabitat.org/themes/custom/habitat/images/icons/covid-19-campaign-icon-black.png')
                            embed.add_field(name="New recovered cases:",
                                            value=str("{:,}".format(data["Countries"][i]["NewConfirmed"])),
                                            inline=True)  # Formatting by thousands.
                            embed.add_field(name="Total confirmed cases:",
                                            value=str("{:,}".format(data["Countries"][i]["TotalConfirmed"])),
                                            inline=True)
                            embed.add_field(name="New deaths:",
                                            value=str("{:,}".format(data["Countries"][i]["NewDeaths"])), inline=True)
                            embed.add_field(name="Total deaths:",
                                            value=str("{:,}".format(data["Countries"][i]["TotalDeaths"])), inline=True)
                            embed.add_field(name="New recovered individuals:",
                                            value=str("{:,}".format(data["Countries"][i]["NewRecovered"])), inline=True)
                            embed.add_field(name="Total recovered individuals:",
                                            value=str("{:,}".format(data["Countries"][i]["TotalRecovered"])),
                                            inline=True)
                            break
                            # Checking if the country can be matched. If not, ERROR-message is displayed.

                        elif (string != data["Countries"][i]["Slug"]):
                            embed = discord.Embed(
                                title="Covid Information", color=0x42d8a8)
                            embed.add_field(
                                name="Error",
                                value="Could not find the country - please input the command followed by a SPACE and the country name. Also; check the country name. Country name must be without spaces. E.G. country [Holy See (Vatican City State)] is typed as [holy-see-vatican-city-state].",
                                inline=False)




                except:
                    embed.add_field(name="Error",
                                    value="Something went wrong - please input the command followed by a SPACE and the country name.",
                                    inline=False)


        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CovidCog(bot))
