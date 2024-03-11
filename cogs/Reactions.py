import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os



class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.client.user:
            return
        channel = reaction.message.channel
        await channel.send(user.name + " added: " + reaction.emoji)


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user == self.client.user:
            return
        channel = reaction.message.channel
        await channel.send(user.name + " removed: " + reaction.emoji)


    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author == self.client.user:
            return
        
        if ('bozo') in message.content.lower() or ('clown') in message.content.lower():
            emoji = '🤡'
            await message.add_reaction(emoji)
        
        if ('now') in message.content.lower():
            emoji = '⚡'
            await message.add_reaction(emoji)











async def setup(client):
    await client.add_cog(Reactions(client))