from discord.ext import commands
from discord.ext.commands import CommandNotFound, has_permissions


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error

    @commands.command()
    @has_permissions(administrator=True, manage_messages=True)
    async def clear(self, ctx):
        try:
            await ctx.channel.purge(limit=100)
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Utils(client))