from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot

from riotwatcher import LolWatcher, ApiError

class RiotApiCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def search(self, ctx: Context, username):
        self.bot.lolapi.summoner.by_name("na1", username)
        
