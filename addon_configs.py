from isAllowed import *

def normalize(toNormal):
    toNormal = toNormal.message.content.split(' ')[2].lower()
    if toNormal in ['bans', 'ban']:
        toNormal = 'Bans'
    elif toNormal in ['joins', 'enter', 'entry', 'join']:
        toNormal = 'Joins'
    elif toNormal in ['leaves', 'leave', 'disconnect']:
        toNormal = 'Leaves'
    elif toNormal in ['imgur', 'album', 'imguralbum', 'albums']:
        toNormal = 'ImgurAlbum'
    elif toNormal in ['channel', 'channelupdate', 'channelupdates']:
        toNormal = 'ChannelUpdates'
    elif toNormal in ['server', 'serverupdate', 'serverupdates']:
        toNormal = 'ServerUpdates'
    elif toNormal = ['profane', 'langfilter', 'languagefilter', 'profanity', 'swears']:
        toNormal = 'Swears'
    else:
        raise IOError(
            "The input from the user was not found in the configuration JSON.")

    return toNormal

class Configuration():

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, help=helpText['config'][1], brief=helpText['config'][0])
    async def config(self, ctx):
        """Parent command for config."""
        if allowUse(ctx) == False:
            await self.bot.say(notallowed)
            return
        elif ctx.invoked_subcommand is None:
            await self.bot.say("Please use `config help` to see how to use this command properly.")

    @config.command(name='enable', pass_context=True)
    async def configEnable(self, ctx):
        if allowUse(ctx) == False:
            return
        try:
            toEnable = normalize(ctx)
        except IOError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))
        currentAllow = giveAllowances(ctx)
        currentAllow[toEnable]['Enabled'] = 'True'
        writeAllow(ctx, currentAllow)
        await self.bot.say("Configs updated.")

    @config.command(name='disable', pass_context=True)
    async def configDisable(self, ctx):
        if allowUse(ctx) == False:
            return
        try:
            toEnable = normalize(ctx)
        except IOError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))
        currentAllow = giveAllowances(ctx)
        currentAllow[toEnable]['Enabled'] = 'False'
        writeAllow(ctx, currentAllow)
        await self.bot.say("Configs updated.")

    @config.command(name='set', pass_context=True)
    async def configSet(self, ctx):
        if allowUse(ctx) == False:
            return
        try:
            toEnable = normalize(ctx)
            if toEnable in ['ImgurAlbum', 'ChannelUpdates', 'Swears']:
                raise IOError(
                    "The input from the user was not found in the configuration JSON.")
        except IOError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))

        try:
            toSet = ctx.message.raw_channel_mentions[0]
        except IndexError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))

        currentAllow = giveAllowances(ctx)
        currentAllow[toEnable]['Channel'] = str(toSet)
        writeAllow(ctx, currentAllow)
        await self.bot.say("Configs updated.")

    @config.command(name='text', pass_context=True)
    async def configText(self, ctx, textstr:str):
        if allowUse(ctx) == False:
            return
        try:
            toEnable = normalize(ctx)
            if toEnable == ['ImgurAlbum', 'ChannelUpdates', 'ServerUpdates', 'Swears']:
                raise IOError(
                    "The input from the user was not found in the configuration JSON.")
        except IOError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))

        currentAllow = giveAllowances(ctx)
        currentAllow[toEnable]['Text'] = ctx.message.content.split(' ',3)[3]
        writeAllow(ctx, currentAllow)
        await self.bot.say("Configs updated.")
    
def setup(bot):
    bot.add_cog(Configuration(bot))
