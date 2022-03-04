from redbot.core import commands
from redbot.core import data_manager

from discord.utils import get
import string
import sqlite3


start_money = 0
role_cost = 50
datapath = "c:/db/cashdata.db" 
#data_manager.cog_data_path(self)

    
class shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        base = sqlite3.connect(datapath)
        cur = base.cursor()
        base.execute('CREATE TABLE IF NOT EXISTS {}(id PRIMARY KEY, cash)'.format("cashdata"))
        members = self.bot.get_all_members()
        for member in members:
            r = cur.execute('SELECT id FROM cashdata WHERE id == ?', (member.id,)).fetchone()
            if r == None:
                cur.execute('INSERT INTO cashdata VALUES(?, ?)', (member.id, start_money))
        base.commit()
        base.close()
        
   
    """   
    async def create_table(self, id):
        base = sqlite3.connect(datapath / "tst.db")
        cur = base.cursor()
        cur.execute('INSERT INTO cashdata VALUES(?, ?)', (id, start_money))
        base.commit()
        return
    """
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await shop.create_table(self, member.id)
        return


    
    @commands.command()
    async def tst(self, ctx, arg):
        check = self.bot.get_all_members()
        trans_table = str.maketrans({'<': None, '>': None, '@': None, '!': None})
        m = arg.translate(trans_table)
        m = int(m)
        for i in check:
            if m == i.id:
                await ctx.channel.send("Yes!")
                return


    


    @commands.command()
    @commands.admin()
    async def bankset(self, ctx, arg, arg2):
        if arg.isnumeric() and arg2.isnumeric() and int(arg2) >= 0:
            check = self.bot.get_user(int(arg))
            if check != None:
                base = sqlite3.connect(datapath)
                cur = base.cursor()
                cur.execute("UPDATE cashdata SET cash == ? WHERE id == ?", (int(arg2), int(arg)))
                await ctx.channel.send(f"Set!")
                base.commit()
                base.close() 
                return
            else:
                await ctx.channel.send("Wrong member id")
                return
        else:
            await ctx.channel.send("Wrong incoming data")
            return







    @commands.command()
    async def bank(self, ctx):
        global start_money
        base = sqlite3.connect(datapath)
        cur = base.cursor()
        id = ctx.author.id
        r = cur.execute('SELECT id FROM cashdata WHERE id == ?', (id,)).fetchone()
        x = cur.execute('SELECT cash FROM cashdata WHERE id == ?', (id,)).fetchone()
        await ctx.channel.send(f"U have **{x[0]}** *coins*")
        base.close() 
        return




    @commands.command()
    @commands.cooldown(1, 30) 
    async def cd(self, ctx):
        await ctx.channel.send("dick")
        return



    @commands.command()
    async def create(self, ctx, arg=None):
        base = sqlite3.connect(datapath)
        cur = base.cursor()
        id = ctx.author.id
        r = cur.execute('SELECT cash FROM cashdata WHERE id == ?', (id,)).fetchone()
        if r[0] >= role_cost: 
            c = r[0] - role_cost
            cur.execute('UPDATE cashdata SET cash == ? WHERE id == ?', (c, id))
            base.close()
            await ctx.author.guild.create_role(name = arg)
            await ctx.channel.send(f"U create role**{arg}**")
        else:
            base.close()
            await ctx.channel.send("U don't have requirement coins") 
        return

