import discord
from discord.ext import commands
from random import randint
from random import choice
import datetime

try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class Advent:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.pref = ["Merry", "Happy", "Have a spooky"]
        self.suff = ["Crimbo", "Christmas", "New Year", "Easter", "Halloween", "Birthday"]
        self.nice = [True, False]

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

    @commands.command()
    async def advent(self):
        """advent"""

        #Your code will go here
        now = datetime.datetime.now()

        if now.month == 12 and now.day < 26:
            await self.bot.say("It's day " + str(now.day) + ", that means it's " + str(25-now.day) + " days until Christmas!")

    @commands.command()
    async def NorN(self):
        """Naughty or Nice?"""

        #Your code will go here
        dab = choice(self.nice)
        if dab:
            await self.bot.say("You've been nice!")
        else:
            await self.bot.say("You've been naughty (ಠ益ಠ)")

    @commands.command()
    async def test(self):
        """Merry crimbo"""

        #Your code will go here
        url = "https://steamdb.info/app/570/graphs/" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
            await self.bot.say(online + ' players are playing this game at the moment')
        except:
            await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")



def setup(bot):
    if soupAvailable:
        bot.add_cog(Advent(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
