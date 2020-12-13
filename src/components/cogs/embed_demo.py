# this is not the code you are looking for
# move along
import random
import discord
from discord.ext import commands

class DemoForEmbedCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='demo', invoke_without_command=True)
    async def example(self, ctx):
        await ctx.channel.send("This is example output from bot whitout embed")
    
    @example.command(name='withembed')
    async def with_embed(self, ctx):
        embed = discord.Embed(title='Embed Demo', color=0xF20587)
        embed.add_field(name="Field 1", value="This is example field one\nand inline set to ***True***", inline=True)
        embed.add_field(name="Field 2", value="This is example field two\nand inline set to ***True***", inline=True)
        embed.add_field(name="Field 3", value="This is example field three\nand inline set to ***True***", inline=True)
        embed.add_field(name="Field 4", value="This is example field four\nand inline set to ***False***", inline=False)
        embed.add_field(name="Field 5", value="This is example field five\nand inline set to ***False***", inline=False)
        await ctx.channel.send(embed=embed)
    
    @commands.command(name='haiku')
    async def haiku(self, ctx):
        haiku = [
            '```Roses are red\nViolets are blue\nUnexpected \'{\' at line 32```',
            '```Tester found a bug\n\"It works fine in my local\"\nWrong answer, dude```',
            '```What is with this code?\noh my, looks like I wrote it\nwhat was I thinking```',
            '```Yesterday it worked\nToday it is not working\nWindows is like that```',
            '```Why doesn\'t this work\nI\'ve checked ninety times\nOh, missed a bracket```'
        ]
        await ctx.channel.send(random.choice(haiku))

def setup(bot):
    bot.add_cog(DemoForEmbedCog(bot))

# this code is for demo purposes only, nothing important happens here