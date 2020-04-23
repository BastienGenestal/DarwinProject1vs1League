import asyncio
import inspect
import discord
from const_messages import START_DUEL_TITLE, START_DUEL_MSG, DUEL_RESULTS_MSG, START_GAME_TITLE
from EloCalculation import EloCalculation
from Ranks import set_rank


class Room:
    def __init__(self, duel_request_msg, attacker, defender):
        self.duelRequestMsg = duel_request_msg
        self.attacker = attacker
        self.defender = defender
        self.roomId = None
        self.bracket = None
        self.channel = None
        self.game = 1
        self.result_msgs = [None, None, None]
        self.result_reactions = [{'a': None, 'd': None}, {'a': None, 'd': None}, {'a': None, 'd': None}]
        self.results = [None, None, None]
        self.done = False

    def is_this_reaction_for_me(self, react, user):
        if user.id != self.attacker.id and user.id != self.defender.id:
            print('user not attacker nor defender', user, self.attacker, self.defender)
            return False
        for msg in self.result_msgs:
            if msg.id == react.message.id:
                return True
        print('react.message not in results')
        return False

    async def check_results(self, game):
        if self.result_reactions[game]['a'] == 0:
            self.results[game] = 'd'
            return await self.channel.send('{} won game {}'.format(self.defender.mention, game + 1))
        if self.result_reactions[game]['d'] == 0:
            self.results[game] = 'a'
            return await self.channel.send('{} won game {}'.format(self.attacker.mention, game + 1))
        if self.result_reactions[game]['d'] == 1 and self.result_reactions[game]['a'] == 1:
            self.results[game] = None
            return await self.channel.send('There is a conflict.\n'
                                           'Please be honest or drop the screenshot and contact a mod.')
        if self.result_reactions[game]['d'] == 1:
            return await self.channel.send('{} claims victory for game {}'.format(self.defender.mention, game + 1))
        if self.result_reactions[game]['a'] == 1:
            return await self.channel.send('{} claims victory for game {}'.format(self.attacker.mention, game + 1))

    async def enter_score(self, client, game, user, victory):
        who = None
        if user.id == self.attacker.id:
            who = 'a'
        elif user.id == self.defender.id:
            who = 'd'
        if not who:
            print("User not attacker nor defender")
            return False
        if self.result_reactions[game-1]:
            if self.results[game-1]:
                print("Winner already decided for game {}".format(game))
                return False
        self.result_reactions[game-1][who] = victory
        await self.check_results(game-1)
        if self.game > 3 or (self.results[0] and self.results[0] == self.results[1]):
            await self.end_the_set(client)
            return True
        if game+1 < self.game:
            return False
        await self.ask_who_won(client)

    async def get_final_results(self):
        msg = 'Sum up:\n'
        a = 0
        d = 0
        for idx, result in enumerate(self.results):
            if result == 'a':
                a += 1
                msg += '{} won game {}/3\n'.format(self.attacker.name, idx + 1)
            elif result == 'd':
                d += 1
                msg += '{} won game {}/3\n'.format(self.defender.name, idx + 1)
            else:
                if self.result_reactions[idx]['a'] and self.result_reactions[idx]['d']:
                    msg += 'conflict on game {}/3\n'.format(idx + 1)
                elif self.result_reactions[idx]['a']:
                    msg += '{} won game {}/3\n'.format(self.attacker.name, idx + 1)
                    a += 1
                elif self.result_reactions[idx]['d']:
                    msg += '{} won game {}/3\n'.format(self.defender.name, idx + 1)
                    d += 1
        winner = None
        if a > d:
            winner = 'a'
            msg += '{} wins !\n'.format(self.attacker.mention)
        elif a < d:
            winner = 'd'
            msg += '{} wins !\n'.format(self.defender.mention)
        await self.channel.send(msg)
        return winner

    async def update_elos(self, client, new_elo_A, new_elo_D):
        client.usefulCogs['DB'].update_elo(self.attacker.id, new_elo_A)
        await set_rank(client, self.attacker, new_elo_A)
        client.usefulCogs['DB'].update_elo(self.defender.id, new_elo_D)
        await set_rank(client, self.defender, new_elo_D)

    async def calculate_elos(self, client, winner):
        attacker = client.usefulCogs['DB'].get_user(self.attacker.id)
        defender = client.usefulCogs['DB'].get_user(self.defender.id)
        elo_brain = EloCalculation(attacker['elo'], defender['elo'])
        if winner == 'a':
            new_elo_A, new_elo_D = elo_brain.calculate(1)
        elif winner == 'd':
            new_elo_A, new_elo_D = elo_brain.calculate(0)
        else:
            print('no elo update')
            return
        await self.update_elos(client, new_elo_A, new_elo_D)

    async def clear(self):
        for member in self.bracket.members:
            await member.remove_roles(self.bracket)
        await self.channel.purge()

    async def call_this_in(self, func, args, time):
        await asyncio.sleep(time)
        if inspect.iscoroutinefunction(func):
            return await func(args)
        return func(args)

    async def log_beats(self, client, winner):
        if winner == 'a':
            await client.usefulChannels['feed'].send('{} beats {} !'.format(self.attacker.name, self.defender.name))
        if winner == 'd':
            await client.usefulChannels['feed'].send('{} beats {} !'.format(self.defender.name, self.attacker.name))

    async def end_the_set(self, client):
        if self.done:
            return
        winner = await self.get_final_results()
        self.done = True
        if winner:
            await self.log_beats(client, winner)
            await self.calculate_elos(client, winner)
        await asyncio.sleep(10)
        await self.clear()
        #client.loop.create_task(self.call_this_in(self.delete_set, (), 10))

    async def ask_who_won(self, client):
        e = discord.Embed(color=discord.Color.green(),
                          title=START_GAME_TITLE.format(self.attacker.name, self.defender.name, self.game))
        e.add_field(name='Results', value=DUEL_RESULTS_MSG.format(self.game))
        msg = await self.channel.send(embed=e)
        await msg.add_reaction(client.usefulBasicEmotes['win'])
        await msg.add_reaction(client.usefulBasicEmotes['lose'])
        self.result_msgs[self.game - 1] = msg
        self.game += 1

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

    async def init_bracket(self, client):
        self.roomId, self.bracket = self.get_free_bracket(client)
        if not self.bracket:
            print('No free bracket to play {} vs {}', self.attacker, self.defender)
            return
        self.channel = client.usefulChannels[self.roomId]
        try:
            await self.attacker.add_roles(self.bracket)
            await self.defender.add_roles(self.bracket)
        except Exception as e:
            print("Can't give {} role to {} or {}. {}".format(
                self.bracket.name, self.attacker, self.defender, e)
            )

    def get_free_bracket(self, client):
        for role in client.BracketRoles:
            if not len(client.BracketRoles[role].members):
                return (role, client.BracketRoles[role])
        return None

    async def create(self, client):
        await self.init_bracket(client)
        await self.init_duel()
        await self.delete_request_msg()
        await self.ask_who_won(client)
