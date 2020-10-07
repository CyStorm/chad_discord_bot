import discord
from discord.ext import commands
import os
from xml.etree import ElementTree

class ChadBot(commands.Bot):

    def __init__(self, command_prefix, db_connection):
        super().__init__(command_prefix)  # if no help command
        #need to add handeling for the help command TODO currently not needed
        self.db_connection = db_connection

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(self.user.id)

    async def on_message(self, message: discord.Message):
        #process commands (from bot super class)
        await super().on_message(message)
        #own evens on messages here
        # if (self.user.id != message.author.id):
        #     if ("smooth" in message.content):
        #         await message.channel.send("Recieved message {}".format(message))
        #         await message.channel.send("William is smooth")
 
    # def write_data_to_xml(self, file, data):
    #     tree = ElementTree.parse(file)
    #     root = tree.getroot()