import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
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
    async def kick(ctx, member: discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been exiled.')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't exile people.")

    # BAN people
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been executed.')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't kill people.")


    #ROLES
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def addRole (self, ctx, user : discord.Member, *, role: discord.Role):

        if role in user.roles:
            await ctx.send(f'{user.mention} already has the role {role}')
        else:
            await user.add_roles(role)
            await ctx.send(f'Added {role} to {user.mention}')

    @addRole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use this command.')

    #REMOVE ROLES
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def removeRole(self, ctx, user : discord.Member, *, role: discord.Role):

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f'Removed {role} from {user.mention}')
        else:
            await ctx.send(f'{user.mention} does not have the role {role}')

    @removeRole.error
    async def removeRole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use this command.')






async def setup(client):
    await client.add_cog(Admin(client))