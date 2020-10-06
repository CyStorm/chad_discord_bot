from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def smooth(self, ctx, arg: str):
        if ("Chad".casefold() not in arg.casefold()):
            message = arg + " is smooth"
        else:
            message = "No insulting the Fuhrer"
        await ctx.send(message)

    @commands.command()
    async def bdon(self, ctx):
        await ctx.send("bdon")

    async def funcname(self, ctx):
        pass