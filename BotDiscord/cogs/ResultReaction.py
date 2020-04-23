import discord
from discord.ext import commands


class ResultReaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    def search_for_set(self, react, user):
        for idx in range(len(self.client.Rooms)):
            if self.client.Rooms[idx].channel == react.message.channel and self.client.Rooms[idx].is_this_reaction_for_me(react, user):
                return self.client.Rooms[idx]
        return None

    def is_it_a_result_msg(self, react, user):
        if user.bot:
            return False
        if react.emoji != self.client.usefulBasicEmotes['win'] and react.emoji != self.client.usefulBasicEmotes['lose']:
            return False
        found_set = self.search_for_set(react, user)
        if not found_set:
            return False
        return found_set

    def get_set_game_from_messgae(self, room, react):
        for idx, msg in enumerate(room.result_msgs):
            if react.message.id == msg.id:
                return idx + 1
        return None

    @commands.Cog.listener()
    async def on_reaction_add(self, react, user):
        room = self.is_it_a_result_msg(react, user)
        if not room:
            return
        game = self.get_set_game_from_messgae(room, react)
        if not game:
            print('Can not find the game for this message.')
            return
        victory = 0
        if react.emoji == self.client.usefulBasicEmotes['win']:
            victory = 1
        should_end = await room.enter_score(self.client, game, user, victory)
        if should_end:
            self.client.Rooms.remove(room)






def setup(client):
    client.add_cog(ResultReaction(client))
