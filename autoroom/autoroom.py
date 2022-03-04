from redbot.core import commands
import discord
from discord.utils import get
import asyncio





table_number = 0
table_mas = [0] * 100

size_id = [0] * 100
size_count = [0] * 100


async def timer(i, channel):
   global size_id
   global size_count
   await asyncio.sleep(30)
   size_id[i] = 0
   size_count[i] = 0
   return


class autoroom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        global table_number
        global table_mas
        global size_id
        global size_count

        table = get(member.guild.channels, name = "Table-creator")
        cat = get(member.guild.categories, name= "Pub")   
        
        if before.channel in cat.channels:
            if len(before.channel.members) == 0:
                i = 0
                for x in table_mas:
                    if x == before.channel.id:
                        await before.channel.delete()
                        table_mas[i] = 0
                        break

                    else:
                        i = i + 1
        
        if after.channel == table:
            l = 0
            for k in size_id:
                if k == member.id:
                    i = 0 
                    for x in table_mas:
                        if x == 0:
                            nme = "Table#"+str(i+1)
                            chnl = await member.guild.create_voice_channel(nme, category=cat, bitrate = 128000, user_limit = size_count[i])
                            await member.move_to(chnl)
                            table_mas[i] = get(member.guild.channels, name = nme).id
                            tt = get(member.guild.channels, name = nme)
                            size_id[l] = 0
                            size_count[l] = 0
                            await tt.edit(reason = None, position = 0)
                            flag = True
                            return
                        else:
                            i = i + 1
                else:
                    l = l + 1

            i = 0
            for x in table_mas:
                if x == 0:
                    nme = "Table#"+str(i+1)
                    chnl = await member.guild.create_voice_channel(nme, category=cat, bitrate = 128000)
                    await member.move_to(chnl)
                    table_mas[i] = get(member.guild.channels, name = nme).id
                    tt = get(member.guild.channels, name = nme)
                    await tt.edit(reason = None, position = 0) 
                    return
                else:
                    i = i + 1


    @commands.command()
    async def size(self, ctx, arg=0):
        global size_id
        global size_count

        if arg > 0:
            i = 0
            for x in size_id:
                if x == 0:
                    size_id[i] = ctx.author.id
                    size_count[i] = arg
                    await ctx.message.delete()
                    await ctx.channel.send(f"count={arg}")
                    await timer(i, ctx.channel)
                    return
                else:
                    i = i + 1
        else:
            await ctx.message.delete()
            await ctx.channel.send("Wrong count")
            return
