from random import random

from discord.ext import commands
from mysql_params import *
from const import INIT_ELO
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
            self.db = self.connect_to_db()
            print("Database connected")
            self.add_all_user_to_db()
        except Exception as e:
            print(e)

    def get_user(self, user_id):
        try:
            with self.db.cursor() as cursor:
                sql = "SELECT `id` FROM `players` WHERE `user_id`=%s"
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
                if not result:
                    print("User does not exist: %s" % user_id)
                else:
                    return result
        except Exception as e:
            print("Error looking up user_id %s.\n%s" % (user_id, e))
        return None

    def add_user_to_db(self, member):
        if self.get_user(member.id):
            return -1
        try:
            with self.db.cursor() as cursor:
                sql = "INSERT INTO `players` (`user_id`, `user_name`, `first_seen`, `avatar_url`, `elo`)" +\
                    " VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (member.id, member.name, member.joined_at, str(member.avatar_url), INIT_ELO + random()*10))
            self.db.commit()
            print("Added used: ", member.name)
        except Exception as e:
            print("Error adding user:", e)
            exit(0)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("{} Joined the server !".format(member.name))
        if self.add_user_to_db(member) != -1:
            print("Added {} to the Database".format(member.name))

    def add_all_user_to_db(self):
        for member in self.client.get_all_members():
            if not member.bot:
                self.add_user_to_db(member)


def setup(client):
    client.add_cog(DBCog(client))
