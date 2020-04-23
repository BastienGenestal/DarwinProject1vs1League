import discord
from discord.ext import commands
from const_messages import START_DUEL_TITLE, START_DUEL_MSG


class ChallengeReaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    def get_free_bracket(self):
        for role in self.client.BracketRoles:
            if not len(self.client.BracketRoles[role].members):
                return (role, self.client.BracketRoles[role])
        return None

    @staticmethod
    def is_it_this_request(req, msg, user):
        if user.bot:
            return False
        if msg.id != req.message.id:
            print("msg", msg.id, req.message.id)
            return False
        if user.id != req.defender.id:
            print("defender", user.id, req.defender.id)
            return False
        return True

    def is_it_a_request_msg(self, react, user):
        if user.bot or react.message.channel.id != self.client.usefulChannels['chal'].id:
            return False
        if react.emoji != self.client.usefulBasicEmotes['yes'] and react.emoji != self.client.usefulBasicEmotes['no']:
            return False
        return True

    def get_valid_request(self, react, user):
        for req in self.client.DuelRequests:
            if self.is_it_this_request(req, react.message, user):
                return req
        return None

    async def init_duel(self, request, id, bracket):
        e = discord.Embed(color=discord.Color.red(), title=START_DUEL_TITLE.format(request.attacker.name, request.defender.name))
        e.add_field(name='First Fight', value=START_DUEL_MSG.format(request.attacker.mention))
        e.set_author(name=request.attacker, icon_url=request.attacker.avatar_url)
        msg = await self.client.usefulChannels[id].send(embed=e)
        pass

    async def create_lobby(self, valid_request):
        id, bracket = self.get_free_bracket()
        if not bracket:
            print('No free bracket to play {} vs {}', valid_request.attacker, valid_request.defender)
            return
        try:
            await valid_request.attacker.add_roles(bracket)
            await valid_request.defender.add_roles(bracket)
        except Exception as e:
            print("Can't give {} role to {} or {}. {}".format(
                bracket.name, valid_request.attacker, valid_request.defender, e)
            )
        await self.init_duel(valid_request, id, bracket)
        await valid_request.message.delete()
        self.client.DuelRequests.remove(valid_request)

    @commands.Cog.listener()
    async def on_reaction_add(self, react, user):
        if not self.is_it_a_request_msg(react, user):
            print('NOT REQUEST')
            return
        # check if the reacter isn't already in a room
        valid_request = self.get_valid_request(react, user)
        if not valid_request:
            print('NO VALID REQUEST FOUND')
            return
        if react.emoji == self.client.usefulBasicEmotes['yes']:
            await self.create_lobby(valid_request)


def setup(client):
    client.add_cog(ChallengeReaction(client))
