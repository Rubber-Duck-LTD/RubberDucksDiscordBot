import requests
from requests.api import post
import discord
import datetime as dt
from datetime import datetime
from discord.ext import commands


class HslCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hsl', aliases=['rt', 'route'])
    # "self" and "ctx" won't be explained, because understanding
    # them is not necessary to understand the rest
    async def get_route_plan(self, ctx, orig, dest):

        coords = []  # TODO: change from list to dictionary
        origin = orig  # starting point for the route
        destination = dest  # ending point for the route
        error = False  # when an error should occur, switched to TRUE

        # store map points for origin and destination
        coords = self.get_coords_for_o_and_d(origin, destination)

        # setting proper names for origin and destination
        # (e.g. malmi -> Malmi, Malmin kauppatie 14, Helsinki)
        origin = coords[0]["name"]
        destination = coords[1]["name"]

        # this variable contains complete route details in string format
        # aka is the content seen by the end user
        route_plan = await self.plan_route(coords, origin, destination)

        # TODO: set route details to map

        await self.send_result_to_discord(ctx, route_plan, error, origin, destination)

    ''' End of main function '''

    def get_coords_for_o_and_d(self, origin, destination):
        # dynamic urls for api calls
        o_url = "https://api.digitransit.fi/geocoding/v1/search?text=" + origin + "&size=1"
        d_url = "https://api.digitransit.fi/geocoding/v1/search?text=" + destination + "&size=1"

        coords = []  # stores objects with information about given coords

        coords.append(self.get_coords_object(o_url))
        coords.append(self.get_coords_object(d_url))
        return coords

    def get_coords_object(self, url):
        # variable for the response to the HTTP request (in JSON format)
        data = requests.get(url).json()

        # make useful data easier to read...
        # e.g { "name": "Valtimotie, Vantaa", "coords": [coord_x, coord_y] }
        coords_object = {"name": data["features"][0]["properties"]
                         ["label"], "coords": data["features"][0]["geometry"]
                         ["coordinates"]}
        return coords_object

    async def plan_route(self, coords, orig, dest):
        url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"

        # header for the http request
        header_json = {"Content-Type": "application/json"}

      # TODO: make vars below easier to read maybe?
        o_coords_str = str(coords[0]["coords"][1]) + "," + \
            str(coords[0]["coords"][0])
        d_coords_str = str(coords[1]["coords"][1]) + "," + \
            str(coords[1]["coords"][0])

        # console prints (for developing purposes)
        print("origin: " + orig)
        print("o_coords: " + o_coords_str)
        print("destination: " + dest)
        print("d_coords: " + d_coords_str)

        # will contain the cleaned route, which will then be returned
        the_route = ""

        # "skeleton" for the query
        query = '''{
            plan(
              fromPlace: "''' + orig + '''::''' + o_coords_str + '''",
              toPlace: "''' + dest + '''::''' + d_coords_str + '''",
              numItineraries: 1
              ) {
              itineraries{
                walkDistance,
                duration,
                legs {
                  mode
                  startTime
                  endTime
                  from {
                    lat
                    lon
                    name
                    stop {
                      code
                      name
                    }
                  },
                  to {
                    lat
                    lon
                    name
                  },
                  trip {
                    routeShortName
                    tripHeadsign
                  },
                  distance
                  legGeometry {
                    length
                  }
                }
              }
            }
          }
        '''

        # variable for the HTTP response
        data = requests.post(url, data=query, json=header_json)

        if data.status_code == 200:
            data = data.json()
        else:  # if the HTTP request fails...
            print("HTTP Error: Status code " + str(data.status_code))
            the_route = "HTTP Error"
            return the_route

        # if the response is successful but empty...
        if data == {'data': {'plan': {'itineraries': []}}}:
            the_route = "out of region"
            return the_route

        # if the response is successful...

        duration = str(dt.timedelta(
            seconds=data["data"]["plan"]["itineraries"][0]["duration"]))

        # TODO: make a function to format time
        the_route += "*duration: " + duration + "*\n\n"
        # list of "legs" (aka kind of different steps during the trip - walk,train,bus etc...)
        data = data["data"]["plan"]["itineraries"][0]["legs"]

        for leg in data:
            start_time = datetime.utcfromtimestamp(
                leg["startTime"] / 1000)
            end_time = datetime.utcfromtimestamp(
                leg["endTime"] / 1000)
            leg_duration = end_time - start_time

            trip = ""

            if leg["mode"] != "WALK":
                trip = " - " + leg["trip"]["routeShortName"] + \
                    " " + leg["trip"]["tripHeadsign"]

            # forms the data into form that is seen by the end user
            the_route += "↓ **" + leg["mode"]+"**" + trip + " \n↓ *(" + str(leg_duration)+")*" + "\n↓ **from:** " + \
                leg["from"]["name"] + "\n"
            the_route += "↓ **to:** " + leg["to"]["name"] + "\n↓\n"

        url_prefix = "https://www.google.fi/maps/dir/"
        origin_for_url = self.urlify_location(orig)
        dest_for_url = self.urlify_location(dest)

        the_route += "\n [Click here](" + url_prefix + \
            origin_for_url + "/" + dest_for_url+") for more advanced planning."

        print(orig, dest)

        return the_route

    def urlify_location(self, location):
        split_location = location.split(" ")
        stringified_location = ""

        for string in split_location:
            stringified_location += string + "+"

        return stringified_location

    async def send_result_to_discord(self, ctx, route_plan, error, origin, destination):
        # the message that will be sent to discord
        embed_message = discord.Embed(
            title="HSL Route Planner", color=0x98c878)

        if route_plan == "out of region":
            error = True
            error_text = "Error when planning route. Make sure both origin and destination is within the HSL region.\n\n**from:** " + \
                origin+"\n **to:** "+destination

            embed_message.add_field(
                name="Error", value=error_text, inline=False)

            await ctx.channel.send(embed=embed_message)
        if route_plan == "HTTP Error":
            error = True
            error_text = "HTTP Error when making a request to the API. Please wait for a few seconds and try again."

            embed_message.add_field(
                name="Error", value=error_text, inline=False)

            await ctx.channel.send(embed=embed_message)

        if not error:
            embed_message.add_field(
                name="Route", value=route_plan, inline=False)

            await ctx.channel.send(embed=embed_message)


def setup(bot):
    bot.add_cog(HslCog(bot))


"""

"""
