import json
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# because nobody likes hardcoded things
PREFIX = os.getenv('PREFIX')

footer = "<> means required, [] means optional"

# .json file with multiple different attributes
# this can be expanded and make the 'help'-command even more specific with categories
# e.g. '-help group' to display all commands available for different group of users (users, moderators, admins etc.)
with open('help_commands.json') as cmd_json:
    help_cmd = json.load(cmd_json)

class HelpCmdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', invoke_without_command=True)
    async def help_msg(self, ctx, *args):
        author = ctx.message.author
        embed = discord.Embed(title=PREFIX+"Help", color=0x7289da)

        # show all commands if nothing is specified after 'help'-command
        if len(args) == 0:
            for cmd in help_cmd:
                help_embed(cmd, embed)
        
        # if one argument is specified after 'help'...
        elif len(args) == 1:
            # ...check if that command exsist
            if check_cmd(args[0].lower()):
                # and if command is found, change it to lowercase because reasons
                arg = str(args[0]).lower()
                # search that command from the local .json file
                for cmd in help_cmd:
                    # and when it's found, add it to embed
                    if arg == help_cmd[cmd]["help"]:
                        help_embed(cmd, embed)
            # these steps are pretty self-explanatory
            else:
                something_wrong(embed)
        # why this is here twice?
        else:
            something_wrong(embed)
        
        # adds footer note to the embed as additional info
        # this can be moved somewhere else, because now it's added in every 'help'-command, even if there is no need to display this information, hence the footer variable is specified elsewhere 
        embed.set_footer(text=footer)
        await author.send(embed=embed)

# actually I have no idea how I got this to work
def help_embed(cmd, embed):
    # if there is alias commands for the command, it adds it to the embed
    # it means if you are too lazy to write the whole word
    if help_cmd[cmd]["alias"] != "":
        # this is the part where magic happens
        embed.add_field(name=help_cmd[cmd]["name"], value="**Description: **" + 
        help_cmd[cmd]["desc"] + "\n**Usage: **" + PREFIX + help_cmd[cmd]["usage"] + 
        "\n**Alias: **" + help_cmd[cmd]["alias"],
        inline=False)
    # and no need to add alias to the embed if there isn't one
    else:
        embed.add_field(name=help_cmd[cmd]["name"], value="**Description: **" + 
        help_cmd[cmd]["desc"] + "\n**Usage: **" + 
        PREFIX + help_cmd[cmd]["usage"],
        inline=False)
    return embed

# checking if given command exsist
def check_cmd(arg):
    for cmd in help_cmd:
        if arg == help_cmd[cmd]["help"]:
            return True
    return False

# you guessed it, something went wrong
def something_wrong(embed):
    embed.add_field(name="Oops", value="Something went wrong, try typing \'" + PREFIX + "help\' to see all available commands.", inline=False)
    return embed
    
def setup(bot):
    bot.add_cog(HelpCmdCog(bot))
