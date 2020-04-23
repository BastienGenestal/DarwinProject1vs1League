from discord.ext import commands


class LogsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        for role in self.client.RankRoles:
            wasAttributed = self.client.RankRoles[role] in before.roles
            isAttributed = self.client.RankRoles[role] in after.roles
            if not wasAttributed and isAttributed:
                await self.client.usefulChannels['feed'].send('{} is now {}.'.format(after.name, self.client.RankRoles[role].name))
                return


def setup(client):
    client.add_cog(LogsCog(client))
