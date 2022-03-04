from .onjoin import onjoin

def setup(bot):
    bot.add_cog(onjoin(bot))