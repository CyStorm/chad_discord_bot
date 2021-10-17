from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot
import copypasta

class PastaCommands(commands.Cog):
    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    def get_pasta(self, key):
        return copypasta.pasta[key]

    @commands.command()
    async def leodance(self, ctx: Context):
        await ctx.send("https://streamable.com/9kkogh")

    @commands.command()
    async def theylied(self, ctx: Context):
        await ctx.send("https://streamable.com/siv3xb")

    @commands.command()
    async def benma(self, ctx: Context):
        message = self.get_pasta("benma")
        await ctx.send(message)
