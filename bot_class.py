import os

import discord
from discord.ext import commands

from mysql_db_connection import MySqlDbConnection
from riotwatcher import LolWatcher, TftWatcher

class ChadBot(commands.Bot):

    def __init__(self, command_prefix, db_connection: MySqlDbConnection, lolapi: LolWatcher, tftapi: TftWatcher):
        super().__init__(command_prefix)  # if no help command
        # need to add handeling for the help command TODO currently not needed
        self.db_connection = db_connection
        self.lolapi = lolapi
        self.tftapi = tftapi

    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))
        print(self.user.id)

    async def on_message(self, message: discord.Message):
        await super().on_message(message)

    def register_to_member_db(self, user):
        '''Puts the user in database if not already exists
        '''
        values = (user.id, user.name, 0)
        columns = self.db_connection.get_colum_names("members")
        try:
            self.db_connection.insert_in_table("members", columns, values)
        except:
            return False
        return True
