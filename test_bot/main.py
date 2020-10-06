from test_bot import ChadBot
from command_list import BasicCommands
from discord.ext import commands

DISCORD_TOKEN = "NzYyNTE3NzYzMTEzMzUzMjI2.X3qUAQ.cnO-oH49oUItIrRZWsGZ0zwM_bg"

DB_HOST = "sql9.freesqldatabase.com:3306"
DB_NAME = "sql9369240"
DB_USER = "sql9369240"
DB_PASSWORD = "PGDE3kjzVa"


if __name__ == "__main__":
    client = ChadBot(command_prefix="!")

    client.add_cog(BasicCommands(client))
    client.run(DISCORD_TOKEN)