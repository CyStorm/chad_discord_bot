from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def smooth(self, ctx):
        await ctx.send("William is smooth")

    @commands.command()
    async def bdon(self, ctx):
        await ctx.send("bdon")