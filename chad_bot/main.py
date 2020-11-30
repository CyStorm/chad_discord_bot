from discord.ext import commands
from mysql import connector

from bot_class import ChadBot
from command_list import BasicCommands
from CONSTANTS import DISCORD_TOKEN, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DB_PORT
from mysql_db_connection import MySqlDbConnection


if __name__ == "__main__":
    db = MySqlDbConnection(DB_NAME, DB_HOST, DB_USER, DB_PASSWORD)
    client = ChadBot(command_prefix="!", db_connection=db)

    client.add_cog(BasicCommands(client))
    client.run(DISCORD_TOKEN)