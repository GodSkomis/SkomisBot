from .shop import shop

def setup(bot):
    bot.add_cog(shop(bot))