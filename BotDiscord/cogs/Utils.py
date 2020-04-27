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

    @commands.Cog.listener()
    async def on_disconnect(self):
        await self.client.log("Disconnected")

    @commands.Cog.listener()
    async def on_connected(self):
        await self.client.log("Connected")

    @commands.command()
    @has_permissions(administrator=True)
    async def update_region_in_db(self, ctx):
        for role in self.client.RegionRoles:
            for member in self.client.RegionRoles[role].members:
                await self.client.usefulCogs['DB'].set_region_platform("region", member.id, role)

    @commands.command()
    @has_permissions(administrator=True)
    async def update_platform_in_db(self, ctx):
        for role in self.client.PlatformRoles:
            for member in self.client.PlatformRoles[role].members:
                await self.client.usefulCogs['DB'].set_region_platform("platform", member.id, role)

    @commands.command()
    @has_permissions(administrator=True)
    async def reset_ranks(self, ctx):
        for member in self.client.server.members:
            await member.remove_roles(self.client.RankRoles)
            member.add_roles(self.client.RankRoles['Newbie'])

    @commands.command()
    @has_permissions(administrator=True, manage_messages=True)
    async def clear(self, ctx):
        try:
            await ctx.channel.purge(limit=100)
        except Exception as e:
            await self.client.log(e)


def setup(client):
    client.add_cog(Utils(client))
