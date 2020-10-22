from discord.ext import commands
from bot_class import ChadBot

class BasicCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def smooth(self, ctx, arg: str):
        if (arg is None):
            message = "I love smooth"
        elif ("Chad".casefold() not in arg.casefold()):
            message = arg + " is smooth"
        else:
            message = "Imagine using my own bot to do this"
        await ctx.send(message)

    @commands.command()
    async def bdon(self, ctx):
        await ctx.send("bdon")

    @commands.command()
    async def leodance(self, ctx):
        await ctx.send("https://streamable.com/9kkogh")

    @commands.command()
    async def theylied(self, ctx):
        await ctx.send("https://streamable.com/siv3xb")