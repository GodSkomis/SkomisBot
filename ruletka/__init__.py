from .ruletka import ruletka

def setup(bot):
    bot.add_cog(ruletka(bot))