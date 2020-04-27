from discord.ext import commands
from mysql_params import *
from const import INIT_ELO
from Ranks import set_rank
import pymysql.cursors


class DBCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @staticmethod
    def connect_to_db():
        return pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS,
            db=DB_NAME, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
        )

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            self.client.db = self.connect_to_db()
            await self.client.log("Database connected")
            await self.add_all_user_to_db()
        except Exception as e:
            await self.client.log(e)

    async def update_elo(self, user_id, new_elo):
        try:
            with self.client.db.cursor() as cursor:
                sql = "UPDATE `players` SET `elo` = %s WHERE `user_id`=%s"
                cursor.execute(sql, (new_elo, user_id))
                self.client.db.commit()
        except Exception as e:
            await self.client.log("Error Updating user elo:", e)
        return None

    async def get_user(self, user_id):
        try:
            with self.client.db.cursor() as cursor:
                sql = "SELECT `*` FROM `players` WHERE `user_id`=%s"
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
                if not result:
                    return None
                else:
                    return result
        except Exception as e:
            await self.client.log("Error looking up user_id {}.\n{}".format(user_id, e))
        return None

    async def add_user_to_db(self, member):
        try:
            with self.client.db.cursor() as cursor:
                sql = "INSERT INTO `players` (`user_id`, `user_name`, `first_seen`, `avatar_url`, `elo`)" +\
                    " VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (member.id, member.name, member.joined_at, str(member.avatar_url), INIT_ELO))
            self.client.db.commit()
            await self.client.log("Added user: " + member.name)
            return await self.get_user(member.id)
        except Exception as e:
            await self.client.log("Error adding user:", e)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        user = await self.get_user(member.id)
        if not user:
            await self.add_user_to_db(member)
            await member.add_roles(self.client.RankRoles['Player'])
        else:
            await set_rank(self.client, member, user['elo'])

    async def add_all_user_to_db(self):
        for member in self.client.get_all_members():
            if not member.bot and not await self.get_user(member.id):
                await self.add_user_to_db(member)


def setup(client):
    client.add_cog(DBCog(client))
