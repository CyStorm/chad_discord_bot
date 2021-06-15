from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot


class BasicCommands(commands.Cog):

    def __init__(self, bot: ChadBot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def smooth(self, ctx: Context, arg=None):
        if (arg is None):
            message = "I love smooth"
        elif ("Chad".casefold() not in arg.casefold()):
            message = arg + " is smooth"
        else:
            message = "Imagine using my own bot to do this"
        await ctx.send(message)

    @commands.command()
    async def leodance(self, ctx: Context):
        await ctx.send("https://streamable.com/9kkogh")

    @commands.command()
    async def theylied(self, ctx: Context):
        await ctx.send("https://streamable.com/siv3xb")

    @commands.command()
    async def register(self, ctx: Context):
        author = ctx.author
        success = self.bot.register_to_member_db(author)
        if (success):
            await ctx.send("Registerd user with id {}".format(author.id))
        else:
            await ctx.send("Failed to register user, probably already registered")

    @commands.command()
    async def facts(self, ctx: Context):
        import random
        x = []
        for _ in range(0, 5):
            x.append(random.choice(["true", "facts"]))
        message = "\n".join(x)
        await ctx.send(message)
