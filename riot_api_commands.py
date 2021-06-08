from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot

from riotwatcher import LolWatcher
from requests.exceptions import HTTPError

class RiotApiCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self.region = "na1"
        self._last_member = None

    @commands.command()
    async def search(self, ctx: Context, username, game="lol"):
        try:
            summoner = self.bot.lolapi.summoner.by_name(self.region, username)
        except HTTPError as e:
            if (e.response.status_code == 404):
                await ctx.send("404 summoner not found")
            else:
                raise e

        print(summoner)
        match = self.is_in_game(game, summoner)
        if (match):
            if (game == "lol"):
                await ctx.send(self.parse_lol_match(match, summoner))
            elif (game == "tft"):
                await ctx.send(self.parse_tft_match(match, summoner))
        else:
            await ctx.send("not in game")

    def parse_tft_match(self, match, summoner):
        for player in match["info"]["participants"]:
            if (player["puuid"] == summoner["puuid"]):
                traits = []
                for trait in player["traits"]:
                    traits.append(trait["name"].replace("Set5_", ""))
                comp = ", ".join(traits)
                message = summoner["name"] + " is currently number {placement}, with {gold_left} gold left and comp: ".format(**player) + comp
        return message

    def parse_lol_match(self, match, summoner):
        players = []
        for player in match["participants"]:
            players.append(player["summonerName"])
        message = "Currently in a {gameType} game with players: ".format(**match) + ", ".join(players)
        return message

    def is_in_game(self, game, summoner):
        if (game == "lol"):
            return self.is_in_game_lol(summoner["id"])
        elif (game == "tft"):
            return self.is_in_game_tft(summoner["puuid"])

    def is_in_game_lol(self, id):
        try:
            match = self.bot.lolapi.spectator.by_summoner(self.region, id)
        except HTTPError as e:
            if (e.response.status_code == 404):
                return False
            else:
                raise e
        return match

    def is_in_game_tft(self, puuid):
        try:
            ids = self.bot.tftapi.match.by_puuid("AMERICAS", puuid, count=1)
        except HTTPError:
            pass

        if (ids):
            match = self.bot.tftapi.match.by_id("AMERICAS", ids[0])
        if (match):
            if (self.is_match_current(match["info"]["game_datetime"], match["info"]["game_length"])):
                return match
        return False

    def is_match_current(self, start_time, length):
        time_now = datetime.timestamp(datetime.now())
        if (start_time + length + 120 > time_now):
            return True
        else:
            return False

if __name__ == "__main__":
    import os
    w = LolWatcher(os.environ["RIOT_API_KEY"])

