from datetime import datetime

import discord
from discord.ext import commands
from Room import Room
from Request import Request

from const_messages import CHALL_ME_TITLE


class ChallengeReaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @staticmethod
    def is_it_this_request(req, msg, user):
        if user.bot:
            return False
        if msg.id != req['req'].message.id:
            return False
        if user.id != req['req'].defender.id:
            return False
        return True

    def is_it_a_request_msg(self, react, user):
        if user.bot or react.message.channel.id != self.client.usefulChannels['chal'].id:
            return False
        if react.emoji != self.client.usefulBasicEmotes['yes'] and react.emoji != self.client.usefulBasicEmotes['no']:
            return False
        return True

    def get_valid_request(self, react, user):
        ## Checking if it is a 'duel request' message
        for req in self.client.DuelRequests:
            if self.is_it_this_request(req, react.message, user):
                return req
        ## Now checking if it is a 'challenge me' message
        if react.emoji != self.client.usefulBasicEmotes['yes']:
            return None
        if react.message.embeds and react.message.embeds[0].title == CHALL_ME_TITLE:
            author = discord.utils.get(self.client.server.members, discriminator=react.message.embeds[0].author.name[-4:])
            if author.id == user.id:
                return
            if not author:
                return None
            req = Request(react.message, author, user)
            return {'req': req, 'time': datetime.now()}
        return None

    async def create_room(self, msg, attacker, defender):
        new_room = Room(msg, attacker, defender, self.client)
        await new_room.create()
        self.client.Rooms.append(new_room)

    @commands.Cog.listener()
    async def on_reaction_add(self, react, user):
        if not self.is_it_a_request_msg(react, user):
            return
        request = self.get_valid_request(react, user)
        if not request:
            return
        if react.emoji == self.client.usefulBasicEmotes['yes']:
            await self.create_room(request['req'].message, request['req'].attacker, request['req'].defender)
            if request in self.client.DuelRequests:
                self.client.DuelRequests.remove(request)
        elif react.emoji == self.client.usefulBasicEmotes['no']:
            await request['req'].message.delete()
            self.client.DuelRequests.remove(request)

def setup(client):
    client.add_cog(ChallengeReaction(client))
