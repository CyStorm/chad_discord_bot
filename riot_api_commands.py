from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot


class RiotApiCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def search(self, ctx: Context, username):
        pass
