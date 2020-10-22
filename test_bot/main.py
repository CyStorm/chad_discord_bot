from bot_class import ChadBot
from command_list import BasicCommands
from discord.ext import commands
from mysql import connector
from CONSTANTS import DISCORD_TOKEN


if __name__ == "__main__":
    client = ChadBot(command_prefix="!", db_connection=None)

    client.add_cog(BasicCommands(client))
    client.run(DISCORD_TOKEN)