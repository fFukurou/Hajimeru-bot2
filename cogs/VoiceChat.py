
import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os



class VoiceChat(commands.Cog):

    def __init__(self, client):
        self.client = client


    #------------------- Voice Chat Commands -------------------

    #    voice = ctx.guild.voice_client <--- gets the voice channel

    #function to check a queue
    def check_queue(self, ctx, id):
        self.queues = {}
        if self.queues[id] != []:
            voice = ctx.guild.voice_client
            source = self.queues[id].pop(0)
            player = voice.play(source)

    #command to make bot join a VC, with a sound effect
    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()

        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = self.FFmpegPCMAudio('bruh.mp3')
            player = voice.play(source)

        else:
            await ctx.send("User not in a voice channel.")

    # Pause the audio file
    @commands.command(pass_context = True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("No audio playing.")

    # Resume the audio file
    @commands.command(pass_context = True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else: 
            await ctx.send("Audio is not paused.")

    # Stop the audio file
    @commands.command(pass_context = True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()    

    # play audio file
    @commands.command(pass_context = True)
    async def play(self, ctx, arg):
        if (ctx.voice_client):
            voice = ctx.guild.voice_client
            audio = arg + '.mp3'
            source = discord.FFmpegPCMAudio("./audio/" + audio) 
            player = voice.play(source, after=lambda x=None: self.check_queue(ctx, ctx.message.guild.id))
            
        else:
            await ctx.send("I'm not in a voice channel")

    # queues audio files
    @commands.command(pass_context = True)
    async def queue(self, ctx, arg):
        voice = ctx.guild.voice_client 
        audio = arg + '.mp3'
        source = discord.FFmpegPCMAudio("./audio/" + audio)    

        guild_id = ctx.message.guild.id

        if guild_id in self.queues:
            self.queues[guild_id].append(source)
        else:
            self.queues[guild_id] = [source]

        await ctx.send('Added to queue.')

    # command to make bot leave VC
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("a'ight bet, bye")
        else:
            await ctx.send("I'm not even in a voice channel.")

    # command to make bot enter a VC saying "bruh"... currently redundant.
    @commands.command()   
    async def bruh(self, ctx):

        if (ctx.author.voice):
            if (ctx.voice_client):
                await ctx.guild.voice_client.disconnect()
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = discord.FFmpegPCMAudio("./audio/" + "bruh.mp3")    
            player = voice.play(source)
        else:
            await ctx.send("User not in a voice channel.")





async def setup(client):
    await client.add_cog(VoiceChat(client))