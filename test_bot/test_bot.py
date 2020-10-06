import discord
from discord.ext import commands

class ChadBot(commands.Bot):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(self.user.id)

    async def on_message(self, message: discord.Message):
        await super().on_message(message)
        if (self.user.id != message.author.id):
            if ("smooth" in message.content):
                await message.channel.send("Recieved message {}".format(message))
                await message.channel.send("William is smooth")