from const import rolesValues


async def clear_rank(client, player):
    for role in client.RankRoles:
        await player.remove_roles(client.RankRoles[role])


def get_rank(client, player):
    for role in client.RankRoles:
        if client.RankRoles[role] in player.roles:
            return client.RankRoles[role]


async def set_rank(client, player, player_elo):
    rank = None
    player_elo = int(player_elo)
    current_rank = get_rank(client, player)
    for rank, elo in rolesValues:
        if player_elo >= elo:
            rank = rank
            break
    if current_rank == rank:
        return
    await clear_rank(client, player)
    await player.add_roles(client.RankRoles[rank])
