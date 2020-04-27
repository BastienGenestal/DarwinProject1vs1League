import discord
from EloCalculation import EloCalculation
from Ranks import set_rank


class Player:
    def __init__(self, client, member):
        self.user = member
        self.client = client
        self.db_user = None
        self.new_elo = None

    async def update_elo(self):
        await self.client.usefulCogs['DB'].update_elo(self.user.id, self.new_elo)
        await set_rank(self.client, self.user, self.new_elo)

    @staticmethod
    def get_text_for_player(elo, new_elo):
        msg = ''
        diff = new_elo - elo
        if diff > 0:
            msg += ' won {} elo.'.format(diff)
        else:
            msg += ' lost {} elo.'.format(abs(diff))
        return msg

    def get_update_elo_text(self):
        return self.get_text_for_player(self.db_user['elo'], self.new_elo)

    async def print_new_elos(self, loser, channel):
        e = discord.Embed(color=discord.Color.purple(), title="Elo update")
        e.add_field(name=self.user.name, value=self.get_update_elo_text())
        e.add_field(name=loser.user.name, value=loser.get_update_elo_text())
        await channel.send(embed=e)

    async def calculate_elos(self, loser):
        elo_brain = EloCalculation(self.db_user['elo'], loser.db_user['elo'])
        self.new_elo, loser.new_elo = elo_brain.calculate(1)

    async def get_db_user(self):
        self.db_user = await self.client.usefulCogs['DB'].get_user(self.user.id)
        return self.db_user

    async def log_beats(self, loser):
        await self.client.usefulChannels['feed'].send('```{} beats {} !```'.format(self.user.name, loser.user.name))

    async def wins(self, loser, channel):
        try:
            await self.get_db_user()
            await loser.get_db_user()
        except Exception as e:
            await self.client.log("Wins function failed, can find users in db", e)
        await self.log_beats(loser)
        await self.calculate_elos(loser)
        await self.print_new_elos(loser, channel)
        await self.update_elo()
        await loser.update_elo()
