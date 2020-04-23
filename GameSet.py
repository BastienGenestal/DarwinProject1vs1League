class GameSet:
    def __init__(self):
        self.signUpMsg = None
        self.bracket = None

    async def create(self, client):
        self.bracket = None
        await self.init_set(client)
        return self

    def init_bracket(self, client):
        for role in client.BracketRoles:
            if not len(client.BracketRoles[role].members):
                self.bracket = client.BracketRoles[role]
                break
        if not self.bracket:
            raise Exception("No Free Bracket")
    @staticmethod
    def is_player_already_in_a_bracket(player):
        for role in player.roles:
            if "Bracket" in role.name:
                return True
        return False

    async def end(self, client):
        print("ENDING", self.bracket.name)
        for player in self.bracket.members:
            await player.remove_roles(client.usefulRoles['activeRole'], self.bracket)
        self.bracket = None
        pass
