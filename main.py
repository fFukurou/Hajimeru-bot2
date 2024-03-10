#TO DO -- fix queue not playing next audio
#--People with space in their names can't be banned
#--Bot detects it's own messages and reacts to it
import discord
import requests
import json

from tokenapi import token_API
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
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
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('Currently being coded'))
    #await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type= discord.ActivityType.listening, name = 'currently being coded'))
    await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='Currently being coded', url="https://www.twitch.tv/fukurouvi"))
    print("The bot is now ready for use")
    print("----------------------------")




#------------------- Events -------------------
    
#message when a user joins the server
@client.event
async def on_member_join(member):
    channel = client.get_channel(766291501432045582)
    await channel.send(f"{member} is here")

#message when a user leaves the server
@client.event
async def on_member_remove(member): 
    channel = client.get_channel(766291501432045582)
    await channel.send(f"{member} is gone")
   
#detects chat messages
@client.event
async def on_message(message):
    lis = ["****","***","****","****"]
    #these stars are abusive language
    for i in lis:
        if message.content == i:
            await message.delete()

            await message.channel.send("Watch'yo mouth >:(")

    if "hello" in message.content.lower():
        await message.channel.send("daremo inai")
    if "remember" in message.content.lower():
        await message.channel.send("Oboete yo")
    if "something" in message.content.lower():
        await message.channel.send("nanimonai")
    if "hate" in message.content.lower():
        await message.channel.send("地ならし")
    if "live" in message.content.lower():
        await message.channel.send("苦労")
    
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

#------------------- Embeds Commands -------------------
@client.command()
async def founding(ctx):
    embed = discord.Embed(title="Founding Titan - 始祖の巨人", url="https://attackontitan.fandom.com/wiki/Founding_Titan", description="The first of all Titans, creator and destroyer.", color=0x28283e)
    embed.set_author(name="Hajime Isayama", url="https://en.wikipedia.org/wiki/Hajime_Isayama", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/FIBD2023HajimeIsayama_01.jpg/720px-FIBD2023HajimeIsayama_01.jpg")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/shingekinokyojin/images/b/bc/Founding_Titan_character_image_%28Eren_Yeager%29.png/revision/latest?cb=20210414102728")
    await ctx.send(embed=embed)

@client.command()
async def Fukurou(ctx):
    embed = discord.Embed(title="Fukurou", url="https://www.youtube.com/channel/UCAYGMeIDuyNVSee7w611a3A", description="I like anime, coding and gaming. \n Author of Hajimeru.", color=0x28283e)
    embed.set_author(name="Fukurou", url="https://www.instagram.com/___yeager___/", icon_url="https://i.ibb.co/6PGYh8r/Vicenzo-5.png")
    embed.set_thumbnail(url="https://i.ibb.co/PZ7hWTP/1-4-1-1.png")
    embed.add_field(name="フクロウ", value="Katakana", inline=True)
    embed.add_field(name="ふくろう", value="Hiragana", inline=True)
    embed.set_footer(text=f"おれが見せてやる")
    #ctx.author.display_name WILL ADD the name of the message's author.
    await ctx.send(embed=embed)

#Dynamic, author-based embeds
@client.command()
async def scd(ctx):
    embed = discord.Embed(title="Just commited suicide!", description="Press F to pay respects.", color=0x28283e)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://cdn.7tv.app/emote/61de32c05001b6b33b2e32c8/4x.webp")
    await ctx.send(embed=embed)

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

#------------------- Mod commands -------------------
# KICK people
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason= None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been exiled.')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't exile people.")

# BAN people
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason= None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been executed.')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't kill people.")




# Initializes the bot
client.run(token_API)