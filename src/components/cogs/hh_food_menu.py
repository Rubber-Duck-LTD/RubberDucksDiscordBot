import urllib.request
import json
import discord
import datetime
from discord.ext import commands

# fetch data from the internet and handle accordingly


def fetch_food():
    url = "https://foodandco.fi/modules/json/json/Index?costNumber=0083&language=fi"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        data = json.loads(html)
        menu = data["MenusForDays"]
        return menu


# creates class for our connection.py to load as a cog
class HHMenuCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='bistro', aliases=['b'], invoke_without_command=True)
    async def list_food(self, ctx):

        menu = fetch_food()
        # initializes the sendable message with a title and color
        embed = discord.Embed(title="Bistro Menu", color=0x006798)

        # starts iterating through each day of the week starting from
        # the current one
        for day in menu:
            days_meals = ""  # declare an empty string for an individual day's meals

            if day["LunchTime"] is None:  # if there's no lunch..
                days_meals = "Bistro is closed"
                break

            # iterate through meals of current iteration (day)
            for meal in day["SetMenus"]:
                for meal_comp in meal["Components"]:
                    # add component (eg. perunamuusi) to string
                    days_meals += "•   " + meal_comp + "\n"
            # add days_meals to the embedded Discord message
            embed.add_field(name="Today", value=days_meals, inline=False)
            break
        # send the message to the Discord chat
        await ctx.channel.send(embed=embed)

    @list_food.command(name='week', aliases=['w'])
    async def food_day(self, ctx):

        menu = fetch_food()
        # initializes the sendable message with a title and color
        embed = discord.Embed(title="Bistro Menu", color=0x98c878)

        # iterating through each day
        for day in menu:
            # variable used to store the date in form "YYYY-MM-DD"
            bistro_date = day["Date"][0:10].split("-")

            # parse the date and time to get the weekday
            # returns a number from 0-6 to represent each day
            # (0 = monday... 6 = sunday)
            weekday = datetime.date(
                int(bistro_date[0]), int(bistro_date[1]), int(bistro_date[2])).weekday()

            # turn the number to the corresponding weekday string
            if weekday == 0:
                weekday = "Monday"
            elif weekday == 1:
                weekday = "Tuesday"
            elif weekday == 2:
                weekday = "Wednesday"
            elif weekday == 3:
                weekday = "Thursday"
            elif weekday == 4:
                weekday = "Friday"
            elif weekday == 5:
                weekday = "Saturday"
            elif weekday == 6:
                weekday = "Sunday"

            days_meals = ""  # declare an empty string for an individual day's meals

            # if there is no lunch that day...
            if day["LunchTime"] is None:
                days_meals += "Bistro is closed\n"

            # iterate through meals of current iteration (day)
            # AKA start adding content to the "days_meals" string
            for meal in day["SetMenus"]:
                # iterate through each meal component in a meal
                for meal_comp in meal["Components"]:
                    # add meal component (eg. perunamuusi) to the meals string
                    days_meals += "•   " + meal_comp + "\n"

                # empty line to differentiate meals
                days_meals += "\n"

            # add meals of the day to the embedded Discord message
            embed.add_field(name=weekday,
                            value=days_meals, inline=False)

        # send the complete message to the Discord chat
        await ctx.channel.send(embed=embed)


# setups the cog included in the module
def setup(bot):
    bot.add_cog(HHMenuCog(bot))
