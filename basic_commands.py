from discord.ext import commands
from discord.ext.commands import Context
from bot_class import ChadBot
import random


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
    async def register(self, ctx: Context):
        author = ctx.author
        success = self.bot.register_to_member_db(author)
        if (success):
            await ctx.send("Registerd user with id {}".format(author.id))
        else:
            await ctx.send("Failed to register user, probably already registered")

    @commands.command()
    async def facts(self, ctx: Context):
        x = []
        for _ in range(0, 5):
            x.append(random.choice(["true", "facts"]))
        message = "\n".join(x)
        await ctx.send(message)

    @commands.command()
    async def flip_coin(self, ctx: Context):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @commands.command()
    async def random_choose(self, ctx: Context, args):
        if (args is None):
            await ctx.send("please provide a comma seperated list of options to randomly choose from")
        else:
            options = args.split(",")
            await ctx.send(random.choice(options))

    @commands.command()
    async def chad_help(self, ctx: Context, command_type=None):
        """
        Sends a very straightforward command manual

        args:
        command_type : the type of command the user wishes to learn about, defaults to basic commands

        return: None
        """
        if (command_type is None):
            await ctx.send('''
                            !facts
                            !generate_artifact <num_artifacts=1> - generates a maximum of 10 artifacts randomly
                            !leodance
                            !op
                            !register - registers the user who invoked this command with Chadbot
                            !smooth <person=None>
                            !theylied
                            *use !chad_help game for a list of LoL commands
                            ''')
        elif command_type.lower() == "lol":
            await ctx.send('''
                            ?search <username> <game=LoL> - Prints out info regarding the specific user
                            *use !chad_help for a list of basic commands
                            ''')

    @commands.command()
    async def generate_artifact(self, ctx: Context, num_artifacts=1):
        """
        Given the number of artifacts the user wishes to generate, randomly generate that number of artifacts (caps at 10)

        args:
        command_type : the type of command the user wishes to learn about, defaults to basic commands

        return: None
        """
        import artifact
        if num_artifacts > 10:
            num_artifacts = 10
        for _ in range(num_artifacts):
            a = artifact.Artifact()
            await ctx.send(a)
