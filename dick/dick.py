from redbot.core import commands
import discord
from discord.utils import get
import random
class dick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def dick(self, ctx):
        rand = random.randint(-5, 30)
        await ctx.channel.send(f"U dick are **{rand}**cm" )
        return