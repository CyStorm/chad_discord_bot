from datetime import datetime
import random
from requests.exceptions import HTTPError

import chess as chess_module
from discord.ext import commands
from discord.ext.commands import Context, MemberConverter
from discord.ext.commands.errors import MemberNotFound

from bot_class import ChadBot
from chess_game import ChessGame

class ChessCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None
        self.game = None

    async def cog_check(self, ctx):
        '''function runs before each command in cog is called, checks permissions
        Returns: bool, if check succeed or fails'''
        print(ctx.prefix)
        return True

    @commands.command()
    async def chess(self, ctx: Context, subcommand, *args):
        # only command interface, process args here
        # or have different prefix for cogs
        subcommands = {
            "start": self.start,
            "play": self.play,
        }

        await subcommands[subcommand](ctx, *args)

    async def start(self, ctx: Context, opponent, *args):
        '''Starts a new game of chess
        TODO can add more aguments, such as, blind, allow illegal moves, ranked to store in database
        '''
        player = ctx.author
        try:
            opponent = await MemberConverter().convert(ctx, opponent)
        except MemberNotFound:
            await ctx.send("{} is not a valid opponent".format(opponent))
            return

        # TODO check if there is another game going on

        if (args):
            if (args[0] in ["white, black"]):
                side = args[0]
        else:
            side = random.choice(["white", "black"])

        op_side = "white" if side == "black" else "black"

        players = {
            side: player,
            op_side: opponent,
        }
        self.game = ChessGame(players["white"], players["black"], *args)
        await ctx.send("Started new game with {}: {} and {}: {}, game number".format(player.mention, side, opponent.mention, op_side))

    async def play(self, ctx: Context, move, *args):
        # TODO can add code to to find the correct game in multiple games
        game: ChessGame = self.game
        if (game is None):
            print("no game found")
            return

        player = ctx.author
        turn = game.turn
        if (game.players[turn] == player):
            success = game.make_move(move)
            if (success):
                game.check_result()
                if (game.is_ended):
                    pass    # TODO game ended code here
                if (not game.blind):
                    await ctx.send(game.board)
            else:
                await ctx.send("Illegal Move")
        else:
            await ctx.send("It is not your turn")

def debug():
    '''debug method'''
    b = chess_module.Board()
    print(b)
    while (1):
        move = str(input())
        try:
            b.push_san(move)
            print(b)
        except ValueError:
            print("illegal move")


if (__name__ == "__main__"):
    debug()
