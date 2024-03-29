import os
from discord.ext import commands
from mysql import connector

from bot_class import ChadBot
from basic_commands import BasicCommands
from riot_api_commands import RiotApiCommands
from chess_commands import ChessCommands
from pasta_commands import PastaCommands
from mysql_db_connection import MySqlDbConnection
from riotwatcher import LolWatcher, TftWatcher


def test():
    import os
    print(os.environ("DB_HOST"))

def main():
    try:
        DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
        # DB_HOST = os.environ["DB_HOST"]
        # DB_NAME = os.environ["DB_NAME"]
        # DB_USER = os.environ["DB_USER"]
        # DB_PASSWORD = os.environ["DB_PASSWORD"]
    except KeyError:
        print("Please set proper variables in environment")
        raise

    # TODO add logic here to include different cog packages or not on CLI
    # db = MySqlDbConnection(DB_NAME, DB_HOST, DB_USER, DB_PASSWORD)
    # lol = LolWatcher(os.environ["RIOT_API_KEY"])
    # tft = TftWatcher(os.environ["RIOT_API_KEY"])
    client = ChadBot(command_prefix="!", db_connection=None, lolapi=None, tftapi=None)

    client.add_cog(BasicCommands(client))
    # client.add_cog(RiotApiCommands(client))
    client.add_cog(ChessCommands(client))
    client.add_cog(PastaCommands(client))
    client.run(DISCORD_TOKEN)

# code from SO
# def get_prefixes(bot, message):
#     cog_prefixes = (cog.prefix for cog in bot.cogs.values() if hasattr(cog, 'prefix'))
#     default_prefixes = ("!")
#     return (*cog_prefixes, *default_prefixes)

if __name__ == "__main__":
    main()
