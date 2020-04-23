import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from const_messages import CONTENT_ON_MESSAGE


class GetOnReaction(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @has_permissions(administrator=True)
    async def init_on_message(self, ctx):
        e = discord.Embed(color=discord.Color.dark_orange())
        e.add_field(name='Resquests', value=CONTENT_ON_MESSAGE)
        #e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=e, delete_after=150)
        await ctx.message.add_reaction('\U00002705')
        await msg.add_reaction(self.client.usefulBasicEmotes['yes'])


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == self.client.get_on_msg:
            user = self.client.server.get_member(payload.user_id)
            if user.bot:
                return
            try:
                await user.add_roles(self.client.usefulRoles['on'])
            except Exception as e:
                print(user.name, e)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == self.client.get_on_msg:
            user = self.client.server.get_member(payload.user_id)
            if user.bot:
                return
            try:
                await user.remove_roles(self.client.usefulRoles['on'])
            except Exception as e:
                print(user.name, e)

def setup(client):
    client.add_cog(GetOnReaction(client))
