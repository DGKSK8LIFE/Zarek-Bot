import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.command()
async def whelp(ctx):
    await ctx.send("""
    Commands:
    !help - what you're seeing right now
    !bing - returns with bong
    !triangle - sends a broken triangle
    !square - sends a broken square
    !sendyeets - yah yeet!
    !oof - oofer gang!
    
    
    
    """)

@client.command() 
async def bing(ctx):
    await ctx.send("bong")

@client.command()
async def triangle(ctx):
    await ctx.send("""
   /\
  /  \
 /    \
/      \
--------
    """)

@client.command()
async def square(ctx):
    await ctx.send("""
    xxxxxxxxxxxxxxxxx
    x               x
    x               x
    x               x
    x               x
    xxxxxxxxxxxxxxxxx
    """)

@client.command()
async def sendyeets(ctx):
    await ctx.send("yeet " * 100)

@client.command()
async def oof(ctx):
    await ctx.send("oof " * 100)
    
@client.event
async def on_member_join(member):
    await member.send("Have fun in this server")

@client.event
async def on_member_remove(member):
    await member.send("Hope you had a good time in the server!")

#this is a stupid bot that has a meme personality, don't take it seriously!





















client.run('[token]', bot = True)
