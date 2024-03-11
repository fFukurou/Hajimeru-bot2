import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os



class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    #------------------- Events -------------------
        
    #message when a user joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(766291501432045582)
        await channel.send(f"{member} is here")

    #message when a user leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member): 
        channel = self.client.get_channel(766291501432045582)
        await channel.send(f"{member} is gone")
    
    #detects chat messages
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
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
        


            
async def setup(client):
    await client.add_cog(Events(client))