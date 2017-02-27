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
    else:
        raise IOError(
            "The input from the user was not found in the configuration JSON.")

    return toNormal
    
youtubeData = yapi.YoutubeAPI(tokens['YoutubeData'])

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
            if toEnable in ['ImgurAlbum', 'ChannelUpdates']:
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
            if toEnable == ['ImgurAlbum', 'ChannelUpdates', 'ServerUpdates']:
                raise IOError(
                    "The input from the user was not found in the configuration JSON.")
        except IOError as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            await self.bot.say("Something went wrong :: {}".format(exc))

        currentAllow = giveAllowances(ctx)
        currentAllow[toEnable]['Text'] = ctx.message.content.split(' ',3)[3]
        writeAllow(ctx, currentAllow)
        await self.bot.say("Configs updated.")

    @commands.group(pass_context=True)
    async def twitch(self, ctx):
        if allowUse(ctx, ['manage_server']):
            pass
        else:
            await self.bot.say(notallowed)

    @twitch.command(pass_context=True,name='add')
    async def twitchAdd(self, ctx, channelName:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Streams']['TwitchTV']
        except KeyError:
            i['Streams'] = defSerCon['Streams']
            strm = i['Streams']['TwitchTV']
        if channelName.lower() in strm:
            await self.bot.say("This user has already been added to the streamer list for this server.")
            return
        url = str('https://api.twitch.tv/kraken/users?login='+channelName)
        streamID = -1
        respose = requests.get(url,headers={'Client-ID':tokens['TwitchTV'],'Accept':'application/vnd.twitchtv.v5+json'})
        html = respose.text
        data = json.loads(html)
        if data['_total'] == 1:
            try:
                channelID = data['users'][0]['_id']
            except:
                await self.bot.say("This user does not exist.")
                return
        else:
            await self.bot.say("This user does not exist.")
            return
        
        strm[channelName.lower()] = channelID
        i['Streams']['TwitchTV'] = strm
        writeAllow(ctx, i)
        await self.bot.say("This user has now been added to the streamer list for this server.")

    @twitch.command(pass_context=True,name='del',aliases=['delete','rem','remove'])
    async def twitchDel(self, ctx, channelID:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Streams']['TwitchTV']
        except KeyError:
            i['Streams'] = defSerCon['Streams']
            writeAllow(ctx, i)
            strm = i['Streams']['TwitchTV']
        if channelID.lower() not in strm:
            await self.bot.say("This user isn't in the streamer list for this server.")
            return
        del strm[channelID.lower()]
        i['Streams']['TwitchTV'] = strm
        writeAllow(ctx, i)
        await self.bot.say("This user has now been removed from the streamer list for this server.")
        
    @twitch.command(pass_context=True,name='list',aliases=['users'])
    async def twitchList(self, ctx):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Streams']['TwitchTV']
        except KeyError:
            i['Streams'] = defSerCon['Streams']
            writeAllow(ctx, i)
            strm = i['Streams']['TwitchTV']
        users_list = "Twitch Users:"
        if len(strm) != 0:
            for item in strm:
                users_list += ('\n\t' + str(item))
        else:
            users_list += '\nNone'
        await self.bot.say(users_list)

    @twitch.command(pass_context=True,name='set')
    async def twitchSet(self, ctx, channelID:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            chan = ctx.message.raw_channel_mentions[0]
        except IndexError:
            await self.bot.say("Please provide a channel.")
            return
        try:
            i['Streams']['Channel'] = chan
        except KeyError:
            i['Streams'] = defSerCon['Streams']
            i['Streams']['Channel'] = chan
        writeAllow(ctx, i)
        await self.bot.say("The stream announcements have now been set to <#{}>".format(chan))
        
    @commands.group(pass_context=True)
    async def youtube(self, ctx):
        if allowUse(ctx, ['manage_server']):
            pass
        else:
            await self.bot.say(notallowed)
    
    @youtube.command(pass_context=True,name='add')
    async def youtubeAdd(self, ctx, channelURL:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Youtube']['Channels']
        except KeyError:
            i['Youtube'] = defSerCon['Youtube']
            strm = i['Youtube']['Channels']
        for channel in strm:
            if channelURL.lower() == strm[channel]['ChannelURL']:
                await self.bot.say("This user has already been added to the channel list for this server.")
                return
        findChannel = youtubeData.get_channel_by_name(channelURL)
        if len(findChannel.items) == 0:
            findChannel = youtubeData.get_channel_by_id(channelURL)
            if len(findChannel.items) == 0:
                await self.bot.say("This channel does not exist.")
                return
        channel = findChannel.items[0]
        try:
            customUrl = channel.snippet.customUrl
        except AttributeError:
            customUrl = channel.id
        strm[str(channel.snippet.title).lower()] = \
            {
                "Name" : str(channel.snippet.title), 
                "ID" : str(channel.id), 
                "ChannelURL" : str(customUrl), 
                "UploadsPlaylist" : str(channel.contentDetails.relatedPlaylists.uploads), 
                "lastPostDate" : str(datetime.datetime.now().isoformat())
            }
        i['Youtube']['Channels'] = strm 
        writeAllow(ctx, i)
        await self.bot.say("The channel `{}` has now been added from the channel list for this server.".format(str(channel.snippet.title)))
        
    
    @youtube.command(pass_context=True,name='del',aliases=['delete','rem','remove'])
    async def youtubeDel(self, ctx, ChannelName:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Youtube']['Channels']
        except KeyError:
            i['Youtube'] = defSerCon['Youtube']
            writeAllow(ctx, i)
            strm = i['Youtube']['Channels']
        if ChannelName.lower() not in strm:
            await self.bot.say("This channel isn't in the channel list for this server.")
            return
        del strm[ChannelName.lower()]
        i['Youtube']['Channels'] = strm
        writeAllow(ctx, i)
        await self.bot.say("This channel has now been removed from the channel list for this server.")
        
    
    @youtube.command(pass_context=True,name='list',aliases=['users'])
    async def youtubeList(self, ctx):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            strm = i['Youtube']['Channels']
        except KeyError:
            i['Youtube'] = defSerCon['Youtube']
            writeAllow(ctx, i)
            strm = i['Youtube']['Channels']
        users_list = "Youtube Channels:"
        if len(strm) != 0:
            for item in strm:
                users_list += ('\n\t' + str(strm[item]['Name']))
        else:
            users_list += '\nNone'
        await self.bot.say(users_list)
    
    @youtube.command(pass_context=True,name='set')
    async def youtubeSet(self, ctx, channelID:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        try:
            chan = ctx.message.raw_channel_mentions[0]
        except IndexError:
            await self.bot.say("Please provide a channel.")
            return
        try:
            i['Youtube']['Channel'] = chan
        except KeyError:
            i['Youtube'] = defSerCon['Youtube']
            i['Youtube']['Channel'] = chan
        writeAllow(ctx, i)
        await self.bot.say("The new video announcements have now been set to <#{}>".format(chan))
        
    @youtube.command(pass_context=True,name='toggle')
    async def youtubeToggle(self, ctx, toggle:str):
        if not allowUse(ctx, ['manage_server']):
            return
        i = giveAllowances(ctx)
        if toggle == None or toggle == "":
            self.bot.say("Please provide a toggle (True/False)")
            return
        if toggle.lower() in ['f', 'false']:
            chan = "False"
        elif toggle.lower() in ['t', 'true']:
            chan = "True"
        try:
            i['Youtube']['DoLive'] = chan
        except KeyError:
            i['Youtube'] = defSerCon['Youtube']
            i['Youtube']['DoLive'] = chan
        writeAllow(ctx, i)
        await self.bot.say("Live video announcements have now been set to `{}`".format(chan))
    
def setup(bot):
    bot.add_cog(Configuration(bot))
