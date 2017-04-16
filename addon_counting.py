from isAllowed import *


class Counting():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def usrcount(self, ctx):
        try:
            toCount = ctx.message.content.split(' ', 1)[1].lower()
        except IndexError:
            count = 0
            for member in ctx.message.server.members:
                if member.bot == False:
                    count += 1
            if ctx.message.server.id == "220307654885638145":
                await self.bot.say("There are **{}** users on this server and again this doesn't count bots you fucking idiot.".format(count))
            else:
                await self.bot.say("There are **{}** users on this server. (Not counting bots.)".format(count))
            return
        count = 0
        usersOnServer = 0
        for member in ctx.message.server.members:
            if toCount in member.display_name.lower():
                count += 1
            usersOnServer += 1
        dp = 2
        while True:
            percentUsers = format((count / usersOnServer) * 100, '.%sf' % dp)
            if percentUsers[-1] == '0':
                dp += 1
            else:
                break
            if dp >= 10:
                break
        await self.bot.say("There are **%s** users with '%s' in their display name on this server. That makes up **%s** percent of users on the server." % (str(count), toCount, percentUsers))

    @commands.command(pass_context=True)
    async def gamecount(self, ctx):
        try:
            toCount = ctx.message.content.split(' ', 1)[1].lower()
            toCountGame = "'" + toCount + "'"
        except IndexError:
            toCount = ""
            toCountGame = "games"
        count = 0
        usersOnServer = 0
        for member in ctx.message.server.members:
            try:
                if member.bot == False:
                    if toCount in member.game.name.lower():
                        count += 1
            except AttributeError:
                pass
            usersOnServer += 1
        dp = 2
        while True:
            percentUsers = format((count / usersOnServer) * 100, '.%sf' % dp)
            if percentUsers[-1] == '0':
                dp += 1
            else:
                break
            if dp >= 10:
                break
        await self.bot.say("There are **%s** users playing %s on this server. That makes up %s percent of users on the server." % (str(count), toCountGame, percentUsers))


def setup(bot):
    bot.add_cog(Counting(bot))
