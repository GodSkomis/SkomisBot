from .autoroom import autoroom


def setup(bot):
    bot.add_cog(autoroom(bot))