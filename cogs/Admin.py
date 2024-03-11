import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os



class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #------------------- Mod commands -------------------
    # KICK people
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason= None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been exiled.')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't exile people.")

    # BAN people
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason= None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been executed.')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't kill people.")






async def setup(client):
    await client.add_cog(Admin(client))