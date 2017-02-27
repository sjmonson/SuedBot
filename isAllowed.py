from botImports import *

# Set Messages
notallowed = "You are not allowed to use that command."
waitmessage = "Please wait..."

# Set the paths
workingDirectory = os.path.dirname(os.path.realpath(__file__)) + \
    "/botTxtFiles/"
serverConfigs = os.path.dirname(os.path.realpath(__file__)) + \
    "/botTxtFiles/serverConfigs/"
try:
    with open('%sdiscordTokens.json' % serverConfigs) as data_file:
        tokens = json.load(data_file)
except FileNotFoundError:
    sys.exit()

# Set up the start time for the restart command
startTime = datetime.datetime.now()


# Load up all the help text for every command.
with open('%shelpText.json' % workingDirectory) as data_file:
    helpText = json.load(data_file)


defSerCon = \
    {
        "Bans": {
            "Enabled": "False",
            "Channel": "",
            "Text" : "{mention} has been banned."
        },
        "RSS": {},
        "Joins": {
            "Enabled": "False",
            "Channel": "",
            "Text" : "{mention} hi welcome i love you"
        },
        "Leaves": {
            "Enabled": "False",
            "Channel": "",
            "Text" : "{mention} lol rip"
        },
        "ChannelUpdates": {
            "Enabled": "False"
        },
        "ServerUpdates": {
            "Enabled": "False",
            "Channel": ""
        },
        "CustomCommands": {},
        "ImgurAlbum": {
            "Enabled": "False"
        },
        "Streams" : {
            "Channel" : "",
            "TwitchTV" : {},
            "Game" : {}
        },
        "Youtube" : {
            "Channel" : "",
            "DoLive" : "True",
            "Channels" : {}
        },
        "Quotes" : {
            
        }
    }


def giveAllowances(ctx):
    if type(ctx) == str:
        serId = ctx
    else:
        try:
            serId = ctx.message.server.id
        except AttributeError:
            serId = ctx.id
    serverConStuff = None
    try:
        with open(serverConfigs + serId + '.json') as a:
            serverConStuff = json.load(a)
    except FileNotFoundError:
        with open(serverConfigs + serId + '.json', 'w') as a:
            serverConStuff = defSerCon
            a.write(json.dumps(serverConStuff, indent=4))
    return serverConStuff


# Fixes a dictionary according to a reference. Pushes all keys into the input
def fixJson(inputDictionary, referenceDictionary=defSerCon):
    # inputDictionary = {"Joins": {"Enabled": "False","Channel": ""}}
    # referenceDictionary = {"Joins": {"Enabled": "False","Channel": "","Text" : "{mention} hi welcome i love you"}}
    for i in referenceDictionary:
        if type(referenceDictionary[i]) == dict:
            if i not in inputDictionary:
                inputDictionary[i] = referenceDictionary[i]
            else:
                inputDictionary[i] = fixJson(inputDictionary[i], referenceDictionary[i])
        else:
            if i in inputDictionary:
                pass
            else:
                inputDictionary[i] = referenceDictionary[i]
    return inputDictionary
    # writeAllow(ctx, inputDictionary)


# Meant for use with the config commands, soon to be removed
# Writes the configuration changes to file.
def writeAllow(ctx, jsonToWrite):
    if type(ctx) == str:
        serId = ctx
    else:
        try:
            serId = ctx.message.server.id
        except AttributeError:
            serId = ctx.id

    with open(serverConfigs + serId + '.json', 'w') as a:
        a.write(json.dumps(jsonToWrite, indent=4))


# Returns the permissions of a given user.
def givePerms(ctx):
    return ctx.message.channel.permissions_for(ctx.message.author)


# Input a ctx and a list of permissions that the user will need..
# This will return true if a user has a certain permission, as asked for by
# the command call.
def allowUse(ctx, listOfNeeds=['admin'], needsAll=False):
    the_master = False
    if (ctx.message.author.id == '145355740851339273' or ctx.message.author.id == tokens['master_id']):
        the_master = True
    allowLst = []
    permList = givePerms(ctx)
    convertDict = {
        'manage_messages': permList.manage_messages or the_master,
        'admin': permList.administrator or the_master,
        'kick_members': permList.kick_members or the_master,
        'kick': permList.kick_members or the_master,
        'ban_members': permList.ban_members or the_master,
        'ban': permList.ban_members or the_master,
        'manage_nicknames': permList.manage_nicknames or the_master,
        'manage_channels': permList.manage_channels or the_master,
        'manage_roles': permList.manage_roles or the_master,
        'manage_emoji':permList.manage_emojis or the_master,
        'emoji':permList.manage_emojis or the_master,
        'emojis':permList.manage_emojis or the_master,
        'manage_server':permList.manage_server or the_master,
        'is_master': the_master
    }
    for i in listOfNeeds:
        allowLst.append(convertDict[i])

    if convertDict['admin'] and 'is_master' not in listOfNeeds:
        return True
    if needsAll:
        if False in allowLst:
            return False
        else:
            return True
    else:
        if True in allowLst:
            return True
        else:
            return False
