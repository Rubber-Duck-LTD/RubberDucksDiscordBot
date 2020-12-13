import os
import urllib
import json
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands


# [THIS IS THE MAIN MODULE WHICH IS USED TO COMMUNICATE WITH DISCORD]

# Getting tokens "keys" for discord connection
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('PREFIX')

# Gets the prefix from .env as the bots prefix (it comes first in every command "-help" etc.) this way everyone can have their own prefix
bot = commands.Bot(command_prefix=PREFIX)

# Removes the default help command for our custom help command.
bot.remove_command('help')

# 'cogs.help_command',
# all included cogs named as initial_extensions
initial_extensions = ['cogs.help_command',
                      'cogs.embed_demo',
                      'cogs.hh_food_menu', # list "[MenusForDays]" seems to be empty at certain times and this prevents the bot from starting. Maybe fix this ASAP?
                      'cogs.covid19_information',
                      'cogs.google_picture',
                      'cogs.google_places',
                      'cogs.google_travel_time',
                      'cogs.helsinki_api_event',
                      'cogs.route_planner']

# loads all cogs that have commands in them
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
# Searches for the assigned guild
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
            # guild needs to be found once

    # announces bots succesful link to server/guild
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # prints current members of the server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# event for greeting new members


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Enjoy your stay!'
    )


@bot.command(name='lukkari', aliases=["timetable", "tt"])
async def lukkari_kone(ctx):
    response = 'https://idpt.haaga-helia.fi/idp/profile/SAML2/Redirect/SSO?execution=e2s1'
    embed = discord.Embed(color=0x98c878)
    embed.add_field(name="Lukkari", value=response, inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(name='kide')
async def kide_app(ctx):
    response = 'https://kide.app/'
    embed = discord.Embed(color=0x98c878)
    embed.add_field(name="Kide", value=response, inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(name='moodle')
async def moodle(ctx):
    response = 'https://idpt.haaga-helia.fi/idp/profile/SAML2/Redirect/SSO?execution=e2s1'
    embed = discord.Embed(color=0x98c878)
    embed.add_field(name="Moodle", value=response, inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(name='mynet')
async def moodle(ctx):
    response = 'https://idpt.haaga-helia.fi/idp/profile/SAML2/Redirect/SSO;jsessionid=z5etf1icdn4510t0qrvcv0wnk?execution=e1s1'
    embed = discord.Embed(color=0x98c878)
    embed.add_field(name="Mynet", value=response, inline=False)
    await ctx.channel.send(embed=embed)

bot.run(TOKEN)
