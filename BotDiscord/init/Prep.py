import discord
from discord.ext import commands
from const import *


class Prep(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def init_server(self):
        server = discord.utils.get(self.client.guilds, id=ServerId)
        if not server:
            raise self.client.MissingSomething("Discord server not found")
        self.client.server = server

    async def init_channels(self):
        for (var, chanName) in UsefulChannelNames:
            channel = discord.utils.get(self.client.server.channels, name=chanName)
            if not channel:
                raise self.client.MissingSomething("{} channel is missing".format(chanName))
            self.client.usefulChannels[var] = channel

    async def init_roles(self):
        for (var, roleName) in UsefulRoles:
            role = discord.utils.get(self.client.server.roles, name=roleName)
            if not role:
                raise self.client.MissingSomething("{} role is missing".format(roleName))
            self.client.usefulRoles[var] = role

    async def init_rank_roles(self):
        for (var, roleName, elo) in RankRoles:
            role = discord.utils.get(self.client.server.roles, name=roleName)
            if not role:
                raise self.client.MissingSomething("{} role is missing".format(roleName))
            self.client.RankRoles[var] = role

    async def init_bracket_roles(self):
        for (var, roleName) in sorted(BracketRoles, key=lambda x: x[1]):
            role = discord.utils.get(self.client.server.roles, name=roleName)
            if not role:
                raise self.client.MissingSomething("{} role is missing".format(roleName))
            self.client.BracketRoles[var] = role

    async def init_custom_emotes(self):
        for (var, emoteName) in UsefulCustomEmotes:
            emote = discord.utils.get(self.client.server.emojis, name=emoteName)
            if not emote:
                raise self.client.MissingSomething("{} emote is missing".format(emoteName))
            self.client.usefulCustomEmotes[var] = emote

    async def init_basic_emotes(self):
        for (var, emote) in UsefulBasicEmotes:
            self.client.usefulBasicEmotes[var] = emote


    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.init_server()
            await self.init_channels()
            await self.init_roles()
            await self.init_rank_roles()
            await self.init_bracket_roles()
            await self.init_custom_emotes()
            await self.init_basic_emotes()
        except self.client.MissingSomething as e:
            print(e)
            print("The bot will shut down, please check the discord server for whatever is missing.")
            exit(84)


def setup(client):
    client.add_cog(Prep(client))
