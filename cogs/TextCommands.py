import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os

class TextCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

        #------------------- Text Commands -------------------
        
    @commands.command()   
    async def hello(self, ctx):
        await ctx.send("Hi...")
        
    @commands.command()   
    async def sus(self, ctx):
        await ctx.send("That's omega sus bro")


    @commands.command()   
    async def goodbye(self, ctx):
        await ctx.send("i go sleep")

    #DMs the author of the message
    @commands.command()
    async def icecream(self, ctx, user:discord.Member, *, message=None):
        message = "BIN CHILLING? BIIN CHILLING."
        embed = discord.Embed(title=message)    
        await user.send(embed=embed)

    #    user = await client.fetch_user(ctx.author.id) <---- gets an user's ID, API sided.
    @commands.command()
    async def pizza(self, ctx, *, message=None):
        messagee = "WELCOME TO KAIKY'S PIZZERIA!"
        user = await self.client.fetch_user(ctx.author.id)
        embed = discord.Embed(title=messagee)    
        await user.send(embed=embed)




async def setup(client):
    await client.add_cog(TextCommands(client))