from redbot.core import commands
import discord
from discord.utils import get



join_role_name = "Newborn"
join_channel_name = "main"
sent_message = None
message_id = 0
emoji = "🏠"
role1 = "Newborn"
role2 = "Resident"


class onjoin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def onjoin(self, ctx):
        emb = discord.Embed(title = f"**Onjoin cog commands:**", color = 0x9A9A9A)
        emb.add_field(name = "(n)<command>", value = f"<onjoinset>\n<rec>", inline = False)
        await ctx.send( embed = emb )
        return
        

 

    @commands.command()
    async def onjoinset(self, ctx, arg = None, *, arg2 = None):
        global join_role_name
        global join_channel_name
        if arg == None:
            emb = discord.Embed(title = "**(n)onjoinset <command>:**", color = 0x9A9A9A)
            emb.add_field(name = f"<role> <*role name*>", value = "Set start role for new users")
            emb.add_field(name = "<channel> <*channel name*>", value = "Set new member notification channel", inline =False)
            await ctx.send( embed = emb )
            return
        if arg == "role":
            if arg2 == None: 
                await ctx.channel.send("(n)onjoinset role <role name>")
                return
            else:
                gg = get(ctx.guild.roles, name=str(arg2))
                if gg == None:
                    await ctx.channel.send("**Wrong role name**")
                    return
                else:
                    join_role_name = arg2
                    await ctx.channel.send(f"New start role is **{join_role_name}**")
                    return

        if arg == "channel":
            if arg2 == None: 
                await ctx.channel.send("(n)onjoinset channel <channel name>")
                return
            else:
                gg = get(ctx.guild.channels, name=str(arg2))
                if gg == None:
                    await ctx.channel.send("**Wrong channel name**")
                    return
                else:
                    join_channel_name = arg2
                    await ctx.channel.send(f"Notification channel is **{join_channel_name}**")
                    return
                

    @commands.Cog.listener()
    async def on_member_join(self, member):
        newr = get(member.guild.roles, name=join_role_name)
        chl = get(member.guild.channels, name=join_channel_name)
        if newr not in member.roles:
                    await member.add_roles(newr)
                    await chl.send(f' {member.mention}**Welcome in city**')
                    return

    @commands.command()
    async def rec(self, ctx, arg = None, arg2 = None):
        global sent_message
        global emoji
        global role1
        global role2

        if arg == None:
            emb = discord.Embed(title = "**(n)rec <command>:**", color = 0x9A9A9A)
            emb.add_field(name = "<open>", value = f"For open recruitment")
            emb.add_field(name = "<close>", value = "For close recruitment", inline =False)
            emb.add_field(name = "<emoji>", value = "For set emoji reaction", inline =False)
            emb.add_field(name = "<erole1>", value = "For set before.role", inline =False)
            emb.add_field(name = "<erole2>", value = "For set after.role", inline =False)
            await ctx.send( embed = emb )
            return


        elif arg == "open":
            chl = get(ctx.guild.channels, name=join_channel_name)
            emb = discord.Embed(title = "**Open**", color = discord.Color.green())
            emb.set_image( url = "https://i.ibb.co/H2X6kfk/pngtree-vector-house-icon-png-image-708543.jpg")
            

            if sent_message == None:
                sent_message = await chl.send( embed = emb )

                if emoji != None:
                    await sent_message.add_reaction(emoji)

                await ctx.send("**Recruitment opened!**")
                return

            else:
                await sent_message.edit( embed = emb )
                await sent_message.clear_reactions()

                if emoji != None:
                    await sent_message.add_reaction(emoji)

                await ctx.channel.send("**Reloaded**")
                return

        elif arg == "close":

            if sent_message == None:
                await ctx.channel.send("**Already closed**")
                return

            else:
                await sent_message.delete()
                sent_message = None
                await ctx.send("**Recruitment closed!**")
                return

        elif arg == "emoji":
            
            if arg2 == None:

                await ctx.channel.send(f"Use *(n)rec emoji <emoji>* to set new emoji\nNow emoji is: {emoji}")
                return

            else:

                emoji = arg2
                await ctx.send("**Emoji reaction have updated!**")
                return

        elif arg == "role1":
            
            if arg2 == None:

                await ctx.channel.send(f"Use *(n)rec role1 <role>* to set new role\nNow role1 is: **{role1}**")
                return

            else:

                role1 = arg2
                await ctx.send("**Before role have updated!**")
                return

        elif arg == "role2":
            
            if arg2 == None:

                await ctx.channel.send(f"Use *(n)rec role2 <role>* to set new role\nNow role2 is: **{role2}**")
                return

            else:

                role2 = arg2
                await ctx.send("**Before role have updated!**")
                return

        else:
            await ctx.send("Wrong argument, call **(n)rec** for info")
            return



    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        global emoji
        global sent_message
        if sent_message != None:

            if payload.member.bot: 
                return

            else: 

                if payload.message_id == sent_message.id:

                    if payload.emoji.name == emoji:

                        role = get(payload.member.guild.roles, name = role1)

                        if role in payload.member.roles:

                            role11 = get(payload.member.guild.roles, name = role1)
                            role22 = get(payload.member.guild.roles, name = role2)
                            await payload.member.remove_roles(role11)
                            await payload.member.add_roles(role22)
                            chl = get(payload.member.guild.channels, name=join_channel_name)
                            await chl.send(f"Now {payload.member.mention} are {role2}")

                            return