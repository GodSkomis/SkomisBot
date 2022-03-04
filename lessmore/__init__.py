from .lessmore import game

def setup(bot):
    bot.add_cog(game(bot))