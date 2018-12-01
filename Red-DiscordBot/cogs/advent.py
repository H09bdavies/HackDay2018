import discord
from discord.ext import commands
from random import randint
from random import choice

class Advent:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.pref = ["Merry", "Happy", "Have a spooky"]
        self.suff = ["Crimbo", "Christmas", "New Year", "Easter", "Halloween", "Birthday"]

    @commands.command()
    async def epic(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will punch anyone! >.<"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    @commands.command()
    async def crimbo(self):
        """Merry crimbo"""

        #Your code will go here
        await self.bot.say(choice(self.pref) + " " + choice(self.suff))


def setup(bot):
    bot.add_cog(Advent(bot))
