import os
from discord.ext import commands
from mysql import connector

from bot_class import ChadBot
from basic_commands import BasicCommands
from mysql_db_connection import MySqlDbConnection


def test():
    import os
    print(os.environ("DB_HOST"))

def main():
    try:
        DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
        DB_HOST = os.environ["DB_HOST"]
        DB_NAME = os.environ["DB_NAME"]
        DB_USER = os.environ["DB_USER"]
        DB_PASSWORD = os.environ["DB_PASSWORD"]
    except KeyError:
        print("Please set proper variables in environment")
        raise

    db = MySqlDbConnection(DB_NAME, DB_HOST, DB_USER, DB_PASSWORD)
    client = ChadBot(command_prefix="!", db_connection=db)

    client.add_cog(BasicCommands(client))
    client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()
