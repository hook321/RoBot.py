import discord, aiohttp, bs4
from bs4 import BeautifulSoup
from discord.ext import commands

class utils:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def isup(self, ctx):
        temp = ctx.message.content.split(' ', 1)
        if len(temp) == 1:
            await self.bot.say("I'm sorry, but you need to give me a site to check.")
        else:
            site = temp[1]
            if not site:
                await self.bot.say("I'm sorry, but you need to give me a site to check.")

            if '://' in site:
                site = site.split('://')[1]
            if not '.' in site:
                site += ".com"
            actualsite = site
            try:
                site = "http://isup.me/" + site
                with aiohttp.ClientSession() as session:
                    async with session.get(site) as resp:
                        data = await resp.read()
                    soup = BeautifulSoup(data, "lxml")
                status = soup.find("div", {"id": "container"}).get_text()
                if "It's just you." in status:
                    await self.bot.say("It's just you. " + actualsite + " is up for me.")
                else:
                    await self.bot.say("Nope. " + actualsite + " is down for me.")
            except Exception as e:
                await self.bot.say("Hmm, something went wrong. Feel free to try again.")
                print(e)

def setup(bot):
    bot.add_cog(utils(bot))
