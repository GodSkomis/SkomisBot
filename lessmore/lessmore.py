from redbot.core import commands
import discord
from discord.utils import get
import random
import string
import math
import asyncio

i = 0
n = 0
rand_bot = 0
rand1 = 0
rand2 = 0
rand_bot_bool = 0
penl = 5




async def timer():
   await asyncio.sleep(60)
   global i
   i = 0
   return


class game(commands.Cog):

    def __init__(self, bot):
        self.bot = bot








    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            global i
            global n
            global rand_bot
            global rand1
            global rand2
            global rand_bot_bool

            if i == 1:

                if message.content.strip().lower() == "less":
                    if rand2-rand1 > 0:
                        rand_bot = random.randint(rand1, rand1+50)
                        if rand_bot_bool == 0:
                            await message.channel.send(f"{message.author.mention}**More!**', Bot and You say *less*")
                            n = 0

                        else:
                            await message.channel.send(f"{message.author.mention}**More!**', You get penalty")
                            n = n + penl

                    elif rand2-rand1 < 0:
                        rand_bot = random.randint(rand1-50, rand1)
                        if rand_bot_bool == 0:
                            await message.channel.send(f"{message.author.mention}**Less!**', Bot and You say *less*")
                            n = 0

                        else:
                            await message.channel.send(f"{message.author.mention}**Less!**', Bot get penalty")
                            n = n - penl
                    else:
                        await message.channel.send(f"{message.author.mention}**Draw!**'")
                        i = 0 
                        return
                        
                        
                elif message.content.strip().lower() == "more":
                    if rand2-rand1 > 0:
                        rand_bot = random.randint(rand1, rand1+50)
                        if rand_bot_bool == 0:
                            await message.channel.send(f"{message.author.mention}**More!**', Bot and You say *less*")
                            n = 0

                        else:
                            await message.channel.send(f"{message.author.mention}**More!**', Bot get penalty")
                            n = n - penl

                    elif rand2-rand1 < 0:
                        rand_bot = random.randint(rand1-50, rand1)
                        if rand_bot_bool == 0:
                            await message.channel.send(f"{message.author.mention}**Less!**', Bot and You say *less*")
                            n = 0

                        else:
                            await message.channel.send(f"{message.author.mention}**Less!**', You get penalty")
                            n = n + penl
                    else:
                        await message.channel.send(f"{message.author.mention}**Draw!**'")
                        i = 0 
                        return
                elif message.content.strip().lower() == "stop":
                    await message.channel.send(f"{message.author.mention}**Stop!**'")
                    i = 0
                else:
                    await message.channel.send(f"{message.author.mention}**send (n)game <less or more>**")
                    return

                i = i + 1
                return
    
    
    
            elif i == 2:
                if message.content.isnumeric():
                    dif = abs(rand2-int(message.content))+n
                    bot_dif = abs(rand2-rand_bot)
                    if dif < bot_dif:
                        await message.channel.send(f"{message.author.mention}**You win!** value={rand2}, you difference={dif} with penalty {n}, bot diff={bot_dif}")
                        i = 0
                        return
                    elif dif == bot_dif or message.content == rand_bot:
                        await message.channel.send(f"{message.author.mention}**Draw!** value={rand2}")
                        i = 0
                        return
                    else:
                        await message.channel.send(f"{message.author.mention}**You loose!** value={rand2}, you difference={dif} with penalty {n}, bot diff={bot_dif}")
                        i = 0
                        return
                else:
                    await message.channel.send(f"{message.author.mention}send (n)game <value>")
                    return





    @commands.command()
    async def game(self, ctx):
        global i
        global rand_bot
        global rand1
        global rand2
        global rand_bot_bool
        
        if i == 0:

                random.seed()
                rand1 = random.randint(50, 100)
                rand_bot_bool = random.randint(0, 1)
                rand2 = random.randint(rand1-50, rand1+50)
                await ctx.channel.send(f"{ctx.author.mention}First value is **{rand1}**, send (n)game <less or more>" )
                i = i + 1
                #await timer()
                return