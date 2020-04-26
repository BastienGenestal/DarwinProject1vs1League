import shlex
import textwrap
from subprocess import call

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
from mysql_params import *

from datetime import datetime

DUMP_TEMPLATE = "mysqldump -h {host} -u {user} -p{passw} {db} > dumps/{filename}.sql"

class AdminDBCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @staticmethod
    def make_backup():
        time = datetime.now().strftime("%y_%m_%d-%H_%M_%S")
        os.system(DUMP_TEMPLATE.format(
            host=DB_HOST,
            user=DB_USER,
            passw=DB_PASS,
            db=DB_NAME,
            filename=DB_NAME + '-' + time
        ))

    async def try_make_backup(self, ctx):
        try:
            self.make_backup()
        except Exception as e:
            await ctx.channel.send("**Backup failed !**\nError: {}".format(e))
            return False
        return True



    @staticmethod
    def format_results(cursor):
        result = cursor.fetchone()
        response = 'Response:\n'
        msg = ''
        while result:
            for elem in result:
                mywrap = textwrap.TextWrapper(width=500, placeholder="...", initial_indent='\t')
                wrap = mywrap.wrap("{} : {}\n".format(elem, str(result[elem])))
                for line in wrap:
                    msg += line + "\n"
            msg += '\n'
            result = cursor.fetchone()
        if not msg:
            return ''
        return response + msg

    @commands.command()
    @has_permissions(administrator=True)
    async def db(self, ctx, arg):
        if not self.client.db or ctx.channel.id != self.client.usefulChannels['db'].id:
            return
        if not await self.try_make_backup(ctx):
            return
        try:
            with self.client.db.cursor() as cursor:
                temp = cursor.execute(arg)
                result = self.format_results(cursor)
                self.client.db.commit()
                await ctx.channel.send("Success on : {}\n```\nReturn status: {}\n{}```".format(arg, temp, result))
            return True
        except Exception as e:
            await ctx.channel.send(e)
            await self.client.log(e)
        return False

def setup(client):
    client.add_cog(AdminDBCog(client))
