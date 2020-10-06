from test_bot import ChadBot
from command_list import BasicCommands
from discord.ext import commands

DISCORD_TOKEN = "NzYyNTE3NzYzMTEzMzUzMjI2.X3qUAQ.cnO-oH49oUItIrRZWsGZ0zwM_bg"

if __name__ == "__main__":
    client = ChadBot(command_prefix="!")

    client.add_cog(BasicCommands(client))
    client.run(DISCORD_TOKEN)