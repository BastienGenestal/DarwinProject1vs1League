from discord.ext import commands


class RemoveWinnerMedKitRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        pass

def setup(client):
    client.add_cog(RemoveWinnerMedKitRole(client))
