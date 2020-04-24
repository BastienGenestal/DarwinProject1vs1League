import discord
from discord.ext import commands
from const_messages import DUEL_REQUEST_MSG, CHALLENGE_SAME_PLAYER_MESSAGE, CHALLENGE_YOURSELF_MESSAGE
from Request import Request
from datetime import datetime


class ChallengeCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def challenge(self, message):
        author = message.author
        content = message.content
        channel = message.channel
        mention = message.mentions[0]
        await message.delete()
        e = discord.Embed(color=discord.Color.red(), title="DUEL REQUEST")
        e.add_field(name='FIGHT', value=DUEL_REQUEST_MSG.format(author.name, mention, content))
        e.set_author(name=author, icon_url=author.avatar_url)
        botMsg = await channel.send(embed=e, delete_after=60 * 2)
        await botMsg.add_reaction(self.client.usefulBasicEmotes['yes'])
        req = Request(botMsg, author, mention)
        self.client.DuelRequests.append({'req': req, 'time': datetime.now()})

    def is_it_more_than_x_minutes(self, request_time):
        difference = datetime.now() - request_time
        seconds_in_day = 24 * 60 * 60
        datetime.timedelta(0, 8, 562000)
        diff_in_minutes = divmod(difference.days * seconds_in_day + difference.seconds, 60)
        print(diff_in_minutes, diff_in_minutes[0])
        return diff_in_minutes[0] > 5

    async def chall_same_player(self, message):
        for request in self.client.DuelRequests:
            if request['req'].attacker.id == message.author.id and request['req'].defender.id == message.mentions[0].id and not self.is_it_more_than_x_minutes(request['time']):
                await message.author.send(content=CHALLENGE_SAME_PLAYER_MESSAGE)
                await message.delete()
                return True
        return False

    @staticmethod
    async def chall_yourself(message):
        await message.author.send(content=CHALLENGE_YOURSELF_MESSAGE)
        await message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id == self.client.usefulChannels['chal'].id:
            if not message.mentions or len(message.mentions) != 1:
                await message.delete()
                return
            if message.mentions[0].id == message.author.id:
                return await self.chall_yourself(message)
            #if await self.chall_same_player(message):
            #    return
            await self.challenge(message)



def setup(client):
    client.add_cog(ChallengeCog(client))
