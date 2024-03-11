import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os



class Embeds(commands.Cog):

    def __init__(self, client):
        self.client = client

    #------------------- Embeds Commands -------------------
    @commands.command()
    async def founding(self, ctx):
        embed = discord.Embed(title="Founding Titan - 始祖の巨人", url="https://attackontitan.fandom.com/wiki/Founding_Titan", description="The first of all Titans, creator and destroyer.", color=0x28283e)
        embed.set_author(name="Hajime Isayama", url="https://en.wikipedia.org/wiki/Hajime_Isayama", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/FIBD2023HajimeIsayama_01.jpg/720px-FIBD2023HajimeIsayama_01.jpg")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/shingekinokyojin/images/b/bc/Founding_Titan_character_image_%28Eren_Yeager%29.png/revision/latest?cb=20210414102728")
        await ctx.send(embed=embed)

    @commands.command()
    async def Fukurou(self, ctx):
        embed = discord.Embed(title="Fukurou", url="https://www.youtube.com/channel/UCAYGMeIDuyNVSee7w611a3A", description="I like anime, coding and gaming. \n Author of Hajimeru.", color=0x28283e)
        embed.set_author(name="Fukurou", url="https://www.instagram.com/___yeager___/", icon_url="https://i.ibb.co/6PGYh8r/Vicenzo-5.png")
        embed.set_thumbnail(url="https://i.ibb.co/PZ7hWTP/1-4-1-1.png")
        embed.add_field(name="フクロウ", value="Katakana", inline=True)
        embed.add_field(name="ふくろう", value="Hiragana", inline=True)
        embed.set_footer(text=f"おれが手前を見せてやる")
        #ctx.author.display_name WILL ADD the name of the message's author.
        await ctx.send(embed=embed)

    #Dynamic, author-based embeds
    @commands.command()
    async def scd(self, ctx):
        embed = discord.Embed(title="Just commited suicide!", description="Press F to pay respects.", color=0x28283e)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn.7tv.app/emote/61de32c05001b6b33b2e32c8/4x.webp")
        await ctx.send(embed=embed)






async def setup(client):
    await client.add_cog(Embeds(client))