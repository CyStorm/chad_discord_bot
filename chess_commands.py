from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot

from requests.exceptions import HTTPError

class ChessCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None
        self.prefix = "chess"

    async def cog_check(self, ctx):
        return ctx.prefix == self.prefix

    @commands.command()
    async def chess(self, ctx, subcommand, *args):
        # only command interface, process args here?
        # or have different prefix for cogs
        await ctx.send("here")