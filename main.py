#TO DO -- fix queue not playing next audio
import discord
import requests
import json

from tokenapi import token_API
from discord.ext import commands
from discord import FFmpegPCMAudio


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)


queues = {}
#         voice = ctx.guild.voice_client <--- gets the voice channel


#function to check a queue
def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)





#------------------- Dev Commands -------------------
#what you'll see when the bot is turned on

@client.event 
async def on_ready():
    print("The bot is now ready for use")
    print("----------------------------")


#------------------- Event Commands -------------------
    
#message when a user joins the server
@client.event
async def on_member_join(member):
    channel = client.get_channel(766291501432045582)
    await channel.send("he's here")

#message when a user leaves the server
@client.event
async def on_member_remove(member):
    channel = client.get_channel(766291501432045582)
    await channel.send("he's gone")
   
#detects chat messages
@client.event
async def on_message(message):
    lis = ["****","***","****","****"]
    #these stars are abusive language
    for i in lis:
        if message.content == i:
            await message.delete()

            await message.channel.send("Watch'yo mouth >:(")

    if "hi" in message.content.lower():
        await message.channel.send("darenimo, inai")
    
    
    else:
        await client.process_commands(message)






#------------------- Text Commands -------------------
    
@client.command()   
async def hello(ctx):
    await ctx.send("Hi...")
    
@client.command()   
async def sus(ctx):
    await ctx.send("That's omega sus bro")


@client.command()   
async def goodbye(ctx):
    await ctx.send("i go sleep")


#------------------- Voice Chat Commands -------------------

#command to make bot join a VC, with a sound effect
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bruh.mp3')
        player = voice.play(source)

    else:
        await ctx.send("User not in a voice channel.")

# Pause the audio file
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No audio playing.")

# Resume the audio file
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else: 
        await ctx.send("Audio is not paused.")

# Stop the audio file
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

# play audio file
@client.command(pass_context = True)
async def play(ctx, arg):
    if (ctx.voice_client):
        voice = ctx.guild.voice_client
        audio = arg + '.mp3'
        source = FFmpegPCMAudio(audio)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
        
    else:
        await ctx.send("I'm not in a voice channel")

# queues audio files
@client.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client 
    audio = arg + '.mp3'
    source = FFmpegPCMAudio(audio)    

    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]

    await ctx.send('Added to queue.')

# command to make bot leave VC
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("a'ight bet, bye")
    else:
        await ctx.send("I'm not even in a voice channel.")

# command to make bot enter a VC saying "bruh"... currently redundant.
@client.command()   
async def bruh(ctx):

    if (ctx.author.voice):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bruh.mp3')
        player = voice.play(source)
    else:
        await ctx.send("User not in a voice channel.")









# Initializes the bot
client.run(token_API)