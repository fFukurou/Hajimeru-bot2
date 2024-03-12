#TO DO -- queue completely broke after cog
#--People with space in their names can't be banned, Roles with space in their names can't be selected
#--Bot detects it's own messages and reacts to it     ---------- FIXED
#-- Errors section currently very broken and fragile
#-- FFMPEG not working in cogs       --------- FIXED
import requests
import json

from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
from discord import FFmpegPCMAudio

import discord
from discord.utils import get
from discord.ext import commands
import os
import asyncio

from tokenapi import token_API

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event 
async def on_ready():
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('Currently being coded'))
    #await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type= discord.ActivityType.listening, name = 'currently being coded'))
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Currently being coded', url="https://www.twitch.tv/fukurouvi"))
    print("The bot is now ready for use")
    print("----------------------------")


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await client.start(token_API)


asyncio.run(main())