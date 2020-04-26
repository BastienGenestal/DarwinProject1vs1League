import asyncio
from datetime import datetime
import inspect
import discord
from const_messages import *
from EloCalculation import EloCalculation
from Ranks import set_rank


class Room:
    def __init__(self, duel_request_msg, attacker, defender, client):
        self.client = client
        self.duelRequestMsg = duel_request_msg
        self.attacker = attacker
        self.defender = defender
        self.bracket = None
        self.channel = None
        self.result_msgs = None
        self.result_reactions = {'a': None, 'd': None}
        self.results = None
        self.done = False
        self.task = None

    def is_this_reaction_for_me(self, react, user):
        if user.id != self.attacker.id and user.id != self.defender.id:
            return False
        if react.message.id != self.result_msgs.id:
            return False
        return True

    async def claim_was_right(self, winner):
        await self.end_the_set(winner)

    @staticmethod
    async def call_this_in(func, args, time):
        await asyncio.sleep(time)
        if inspect.iscoroutinefunction(func):
            if args:
                return await func(args)
            return await func()
        if args:
            return func(args)
        return func()

    async def check_results(self):
        winner = None
        msg = ''
        if self.task:
            self.task.cancel()
        if self.result_reactions['d'] == self.result_reactions['a']:
            msg = CONFLICT_MSG
        elif self.result_reactions['a'] == 0:
            msg = '{} admits defeat. {} won\n'.format(self.attacker.name, self.defender.name)
            winner = 'd'
        elif self.result_reactions['d'] == 0:
            msg = '{} admits defeat. {} won\n'.format(self.defender.name, self.attacker.name)
            winner = 'a'
        elif self.result_reactions['a'] == 1:
            msg = CLAIM_VICTORY_MSG.format(self.attacker.name, self.defender.name, self.defender.mention)
            await self.client.log("{} claims victory at {}".format(self.attacker.name, datetime.now()))
            self.task = self.client.loop.create_task(self.call_this_in(self.claim_was_right, 'a', 60))
        elif self.result_reactions['d'] == 1:
            msg = CLAIM_VICTORY_MSG.format(self.defender.name, self.attacker.name, self.attacker.mention)
            await self.client.log("{} claims victory at {}".format(self.defender.name, datetime.now()))
            self.task = self.client.loop.create_task(self.call_this_in(self.claim_was_right, 'd', 60))
        await self.channel.send(msg)
        return winner

    async def enter_score(self, user, victory):
        who = None
        if user.id == self.attacker.id:
            who = 'a'
        elif user.id == self.defender.id:
            who = 'd'
        if not who:
            return False
        self.result_reactions[who] = victory
        winner = await self.check_results()
        if winner:
            await self.end_the_set(winner)

    async def update_elos(self, new_elo_A, new_elo_D):
        await self.client.usefulCogs['DB'].update_elo(self.attacker.id, new_elo_A)
        await set_rank(self.client, self.attacker, new_elo_A)
        await self.client.usefulCogs['DB'].update_elo(self.defender.id, new_elo_D)
        await set_rank(self.client, self.defender, new_elo_D)

    @staticmethod
    def get_text_for_player(elo, new_elo):
        msg = ''
        diff = new_elo - elo
        if diff > 0:
            msg += ' won {} elo.'.format(diff)
        else:
            msg += ' lost {} elo.'.format(abs(diff))
        return msg

    async def print_new_elos(self, elo_a, new_elo_a, elo_d, new_elo_d):
        e = discord.Embed(color=discord.Color.purple(), title="Elo update")
        attacker_msg = self.get_text_for_player(elo_a, new_elo_a)
        defender_msg = self.get_text_for_player(elo_d, new_elo_d)
        e.add_field(name=self.attacker.name, value=attacker_msg)
        e.add_field(name=self.defender.name, value=defender_msg)
        await self.channel.send(embed=e)

    async def calculate_elos(self, winner):
        attacker = await self.client.usefulCogs['DB'].get_user(self.attacker.id)
        defender = await self.client.usefulCogs['DB'].get_user(self.defender.id)
        elo_brain = EloCalculation(attacker['elo'], defender['elo'])
        if winner == 'a':
            new_elo_A, new_elo_D = elo_brain.calculate(1)
        elif winner == 'd':
            new_elo_A, new_elo_D = elo_brain.calculate(0)
        else:
            return
        await self.print_new_elos(attacker['elo'], new_elo_A, defender['elo'], new_elo_D)
        await self.update_elos(new_elo_A, new_elo_D)

    async def clear(self):
        for member in self.bracket.members:
            await member.remove_roles(self.bracket)
        await self.channel.purge()

    async def log_beats(self, winner):
        if winner == 'a':
            await self.client.usefulChannels['feed'].send('```{} beats {} !```'.format(self.attacker.name, self.defender.name))
        if winner == 'd':
            await self.client.usefulChannels['feed'].send('```{} beats {} !```'.format(self.defender.name, self.attacker.name))

    async def end_the_set(self, winner):
        if self.done:
            return
        self.done = True
        await self.log_beats(winner)
        await self.calculate_elos(winner)
        await self.channel.send('```This room will close in 10 seconds...```'   )
        self.client.loop.create_task(self.call_this_in(self.clear, (), 10))
        #self.client.loop.create_task(self.call_this_in(self.delete_set, (), 10))

    async def ask_who_won(self):
        e = discord.Embed(color=discord.Color.green(),
                          title=START_GAME_TITLE.format(self.attacker.name, self.defender.name))
        e.add_field(name='Results', value=DUEL_RESULTS_MSG)
        msg = await self.channel.send(embed=e)
        await msg.add_reaction(self.client.usefulBasicEmotes['win'])
        await msg.add_reaction(self.client.usefulBasicEmotes['lose'])
        self.result_msgs = msg

    async def init_duel(self):
        e = discord.Embed(color=discord.Color.red(),
                          title=START_DUEL_TITLE.format(self.attacker.name, self.defender.name))
        e.set_thumbnail(url=self.attacker.avatar_url)
        e.set_image(url=self.defender.avatar_url)
        e.set_author(name=self.attacker, icon_url=self.attacker.avatar_url)
        e.add_field(name='Fight !', value=START_DUEL_MSG.format(self.attacker.mention))
        await self.channel.send("{} vs {}".format(self.attacker.mention, self.defender.mention), embed=e)

    async def delete_request_msg(self):
        await self.duelRequestMsg.delete()
        self.duelRequestMsg = None

    async def init_bracket(self):
        roomId, self.bracket = self.get_free_bracket()
        if not self.bracket:
            await self.client.log('No free bracket to play {} vs {}'.format(self.attacker, self.defender))
            return
        self.channel = self.client.usefulChannels[roomId]
        try:
            await self.attacker.add_roles(self.bracket)
            await self.defender.add_roles(self.bracket)
        except Exception as e:
            await self.client.log("Can't give {} role to {} or {}. {}".format(
                self.bracket.name, self.attacker, self.defender, e)
            )

    def get_free_bracket(self):
        for role in self.client.BracketRoles:
            if not len(self.client.BracketRoles[role].members):
                return (role, self.client.BracketRoles[role])
        return None

    async def create(self):
        await self.init_bracket()
        await self.init_duel()
        await self.delete_request_msg()
        await self.ask_who_won()
