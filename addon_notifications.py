from isAllowed import *

    
youtubeData = yapi.YoutubeAPI(tokens['YoutubeData'])

# Returns streamID if channel live, otherwise -1
def IsTwitchLive(streamID):
    url = str('https://api.twitch.tv/kraken/streams/'+streamID)
    respose = requests.get(url,headers={'Client-ID':tokens['TwitchTV'],'Accept':'application/vnd.twitchtv.v5+json'})
    html = respose.text
    data = json.loads(html)
    if str(data['stream']) == str(None):
        return -1
    try:
        return str(data['stream']['game'])
    except:
        return 'unknown'
    return -1


async def twitchChecker(bot):
    await bot.wait_until_ready()
    print("Twitch check starting")
    fmt = 'The channel `{0}` is live on Twitch playing `{1}`! Check it out! <http://twitch.tv/{0}>'
    while True:
        for i in bot.servers:
            serverStuff = giveAllowances(i.id)
            if serverStuff['Streams']['Channel'] != '':
                toPostTo = discord.Object(serverStuff['Streams']['Channel'])
            else:
                toPostTo = i
            streams = serverStuff['Streams']['TwitchTV']
            for o in streams:
                q = IsTwitchLive(streams[o][0])
                if streams[o][1] != str(q) and str(q) != '-1':
                    await bot.send_message(toPostTo, fmt.format(o, str(q)))
                streams[o][1] = str(q)
                    # await bot.send_message(toPostTo, 'The channel `{0}` does not exist or has more then one result; please delete from config.'.format(o))
            serverStuff['Streams']['TwitchTV'] = streams
            writeAllow(i.id, serverStuff)
        await asyncio.sleep(60)
        
# Returns list of new video if any
def NewYoutubeVid(channelItem, doLive):
    newVids = {'vids' : {}, 'max_date' : ""}
    dates = []
    lastFive = youtubeData.get_playlist_items_by_playlist_id(channelItem['UploadsPlaylist'], max_results=5)
    for video in lastFive.items:
        if video.snippet.publishedAt > channelItem['lastPostDate']:
            dates.append(str(video.snippet.publishedAt))
            #if doLive == "False":
            #    if video.snippet.liveBroadcastContent.lower() == "none":
            #        newVids['vids'][str(video.id.videoId)] = video.snippet.liveBroadcastContent
            #else:
            newVids['vids'][str(video.snippet.resourceId.videoId)] = 'none' #video.snippet.liveBroadcastContent
    if len(dates) != 0:
        newVids['max_date'] = max(dates)
    return newVids


async def youtubeChecker(bot):
    await bot.wait_until_ready()
    print("Youtube check starting")
    fmt = 'The channel `{}` has posted a {} video on youtube! Check it out! <https://youtu.be/{}>'
    while True:
        for i in bot.servers:
            serverStuff = giveAllowances(i.id)
            try:
                serverStuff['Youtube']
            except KeyError:
                serverStuff['Youtube'] = defSerCon['Youtube']
            if serverStuff['Youtube']['Channel'] != '':
                toPostTo = discord.Object(serverStuff['Youtube']['Channel'])
            else:
                toPostTo = i
            channels = serverStuff['Youtube']['Channels']
            for c in channels:
                newVids = NewYoutubeVid(channels[c], serverStuff['Youtube']['DoLive'])
                for video in newVids['vids']:
                    if newVids['vids'][video] == 'none':
                        await bot.send_message(toPostTo, fmt.format(channels[c]['Name'], "new", str(video)))
                    else:
                        await bot.send_message(toPostTo, fmt.format(channels[c]['Name'], "live", str(video)))
                        # await bot.send_message(toPostTo, 'The channel `{0}` does not exist or has more then one result; please delete from config.'.format(o))
                    serverStuff['Youtube']['Channels'][c]['lastPostDate'] = newVids['max_date']
            writeAllow(i.id, serverStuff)
        await asyncio.sleep(300)
        
class NotificationsCommands():

    def __init__(self, bot):
        self.bot = bot

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
        
        strm[channelName.lower()] = [channelID, '-1']
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
    bot.loop.create_task(twitchChecker(bot))
    bot.loop.create_task(youtubeChecker(bot))
    bot.add_cog(NotificationsCommands(bot))