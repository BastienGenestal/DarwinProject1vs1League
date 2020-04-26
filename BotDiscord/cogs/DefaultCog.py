import discord
from discord.ext import commands


class DefaultCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Activity(name="Humans fight", type=discord.ActivityType.watching)
        await self.client.change_presence(status=discord.Status.dnd, activity=game)
        print('Bot Ready', flush=True)

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send("pong")

def setup(client):
    client.add_cog(DefaultCog(client))
