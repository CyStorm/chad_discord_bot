from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot

from riotwatcher import LolWatcher
from requests.exceptions import HTTPError

class RiotApiCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def search(self, ctx: Context, username):
        summoner = self.bot.lolapi.summoner.by_name("na1", username)
        try:
            match = self.bot.lolapi.spectator.by_summoner("na1", summoner["id"])
            await ctx.send(match)
        except HTTPError as e:
            await ctx.send(e.response.status_code)
