import discord
from discord.ext import commands
from const_messages import DUEL_REQUEST_MSG
from Request import Request


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
        self.client.DuelRequests.append(Request(botMsg, author, mention))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id == self.client.usefulChannels['chal'].id:
            if not message.mentions or len(message.mentions) != 1:
                await message.delete()
                return
            # if you already challenged that person, return
            await self.challenge(message)



def setup(client):
    client.add_cog(ChallengeCog(client))
