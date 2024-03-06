from tokenapi import token_API
import discord
from discord.ext import commands
import requests
import json

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event 
async def on_ready():
    print("The bot is now ready for use")
    print("----------------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel(766291501432045582)
    await channel.send("he's here")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(766291501432045582)
    await channel.send("he's gone")
   



@client.command()   
async def hello(ctx):
    await ctx.send("HELLO MOTHERFUCKER")

@client.command()   
async def goodbye(ctx):
    await ctx.send("i go sleep")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("User not in a voice channel.")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("a'ight bet, bye")
    else:
        await ctx.send("I'm not even in a voice channel.")
















client.run(token_API)