from discord.ext import commands
from Room import Room


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
        for req in self.client.DuelRequests:
            if self.is_it_this_request(req, react.message, user):
                return req
        return None

    @commands.Cog.listener()
    async def on_reaction_add(self, react, user):
        if not self.is_it_a_request_msg(react, user):
            return
        # check if the reacter isn't already in a room
        request = self.get_valid_request(react, user)
        if not request:
            print('NO VALID REQUEST FOUND')
            return
        if react.emoji == self.client.usefulBasicEmotes['yes']:
            new_room = Room(request['req'].message, request['req'].attacker, request['req'].defender, self.client)
            await new_room.create()
            self.client.Rooms.append(new_room)
            self.client.DuelRequests.remove(request)

def setup(client):
    client.add_cog(ChallengeReaction(client))
