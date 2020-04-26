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
        await botMsg.add_reaction(self.client.usefulBasicEmotes['no'])
        req = Request(botMsg, author, mention)
        self.client.DuelRequests.append({'req': req, 'time': datetime.now()})

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
            await self.challenge(message)



def setup(client):
    client.add_cog(ChallengeCog(client))
