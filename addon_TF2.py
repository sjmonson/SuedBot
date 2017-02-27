from isAllowed import *


class TeamFortress():

    def __init__(self, bot):
        self.bot = bot
        self.sleeptime = 0.5

    @commands.group(pass_context=True, help='Types out a "Meet the Team" video script.')
    async def meethe(self, ctx):
        pass
    
    @meethe.command(name='scout', pass_context=True, description='Types out the "Meet the Scout" script. Add a parameter to replace "hurt people" with your entry.')
    async def meethescout(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "hurt people"
        if word == None:
            word = "hurt people"
        message = "Um... I don't even know where to start with you. I mean, do you even know who you're talkin' to?"
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*tap-tap \"Yo, what's up?\"*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nD-Do you have any idea, any idea who I am?"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*AHHH-YAAA-HAAHAA!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nBasically - kind of a big deal!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*GHAAAAA!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nOh man, that's beautiful. Heh!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*HA-AHH!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nYa' listenin'? OK. Grass grows, birds fly, sun shines, and brotha'- I {}.".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*AHH- BOINK!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nI'm a force a' nature!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nBONK!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nIf you were from where I was from, you'd be fuckin' dead!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*GHAA-AAA BONG!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nWOOO!"
        await self.bot.edit_message(edit, message)
        
        
    @meethe.command(name='soldier', pass_context=True, description='Types out the "Meet the Soldier" script. Add a parameter to replace "fight" with your entry.')
    async def meethesoldier(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "fight"
        if word == None:
            word = "fight"
        message = "'If {}ing is sure to result in victory, then you must {}!'".format(word, word)
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nSun Tzu said that, and I'd say he knows a little more about {}ing than you do, pal, because he invented it, and then he perfected it so that no living man could best him in the ring of honor.".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*AHHH-AAHH POW! POW! OHW BOOM! \n\"To the left!\"\n\"Maggots!\"\nBOOM! BOOM!\n\"Right up! Right up!\"\n\"Go, go, go!\"*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nThen, he used his {} money...".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...to buy two of every animal on earth, and then he herded them onto a boat..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...and then he beat the **crap** out of every single one."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*BOOM!\n\"Sentry up there!\"\nBOOM! BO-AYAAA \"HA HA HA HA\" BOOM! PINGGGG!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nMe-hehehehehe And from that day forward any time a bunch of animals are together in one place it's called a '**zoo**'!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*.........flop*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nUnless it's a farm!"
        await self.bot.edit_message(edit, message)
    
    @meethe.command(name='pyro', pass_context=True, description='Types out the "Meet the Pyro" script. Add a parameter to replace "" with your entry.')
    async def meethepyro(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "magic"
        if word == None:
            word = "magic"
        message = "**Heavy:** I fear no man. But that... thing... it scares me."
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n**Scout:** No, I... I ain't, I ain't talking about that freak. All right?"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n    He's not here, is she?"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n    How do I get this fucking thing off?!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n**Spy:** One shudders to imagine what inhuman thoughts lie behind that mask..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n    ...what dreams of chronic and sustained cruelty?"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: Do you believe in {}?\nIn a young girls heart\nHow the music can free her\nWhenever it starts :musical_note:".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: And it's {}\nIf the music is groovy\nIt's makes you feel happy like an old time movie :musical_note:".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: I'll tell ya about the {}\nIt'll free your soul\nBut it's like trying to tell a stranger 'bout rock n roll :musical_note:".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*AHHHHHH*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: If you believe in {}, don't bother to choose\nIf it's just band music or rhythm and blues :musical_note:".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*POW-AHHHHHH*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: Your feet start tapping\nAnd you can't seem to find\nHow you got there\nSo just blow your mind :musical_note:"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*MHHHMHH-NO!-AHHHHHH!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n:musical_note: Do you believe in {}?\nCome along with me\nWe'll dance until morning, just you and me\nAnd maybe, if the music the righ... :musical_note:".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*FOOM! AHHHHHHH! UMF! HELP! EEEHHAAAAAH!*"
        await self.bot.edit_message(edit, message)
        
    @meethe.command(name='demoman', pass_context=True, description='Types out the "Meet the Demoman" script. Add a parameter to replace "Demoman" with your entry.')
    async def meethedemoman(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "Demoman"
        if word == None:
            word = "Demoman"
        message = "What makes me a good {}?".format(word)
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nIf I were a bad {}, I wouldn't be sittin' here, discussin' it with you now would I?".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*Let's do it!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*Not one of ya's gonna' survive this.\nBOOM! BOOM! POW!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nOne crossed wire, one wayward pinch of potassium chlorate, one errant twitch... and ***kablooie!***"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*BONK! BINK! Click, BOOM!*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*Gulp, gulp*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nPEW, PEW, PEW, PEW, PEW!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nGulp"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nPEW, PEW, BINK... BINK... BINK, BINK, PEW, PEW, PEW, BOOOM!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nI got a manky eye. I'm a black, Scottish cyclops."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nThey've got more f-*************************-s than they've got the likes of me."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nSo...."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...T'all you fine dandies so proud, so cocksure."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nPrancin' aboot with your heads full of eyeballs! Come and get me I say! I'll be waiting on ya with a whiff of the 'ol brimstone. I'm a grim bloody fable... with an unhappy bloody end!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nClick, BOOM, BOOM, BOOM, BAM!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nOh, they're going to have to glue you back together... ***in hell!***"
        await self.bot.edit_message(edit, message)
        
    @meethe.command(name='heavy', pass_context=True, description='Types out the "Meet the Heavy" script. Add a parameter to replace "bullet" with your entry.')
    async def meetheheavyweapons(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "bullet"
        if word == None:
            word = "bullet"
        message = "I am Heavy Weapons Guy...and *this*... ...is my weapon. She weighs one hundred fifty kilograms and fires two hundred dollar, custom-tooled cartridges at ten thousand rounds per minute. It costs four hundred thousand dollars to fire this weapon...for twelve seconds."
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*OH-HA-HA-snort-OH-HO-HO-HO*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nOh my God, who touched Sascha? Alright...*Who touched my gun!?*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nSome people think they can outsmart me. Maybe, maybe. I've yet to meet one that can outsmart {}.".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*whirrrrrrr*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nWaaaaahhhhh! Uwaaaaaaah! ***Ahahahahaha!*** Cry some more!"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nHeheh, cry some more."
        await self.bot.edit_message(edit, message)

    @meethe.command(name='engineer', pass_context=True, description='Types out the "Meet the Engineer" script. Add a parameter to replace "gun" with your entry.')
    async def meethengie(self, ctx):
        try:
            word = ctx.message.content.split(' ', 2)[2]
        except IndexError:
            word = "gun"
        if word == None:
            word = "gun"
        message = "Hey look, buddy, I'm an Engineer. That means I solve problems."
        edit = await self.bot.say(message)
        await asyncio.sleep(self.sleeptime)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*PING*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nNot problems like \"What is beauty?\", because that would fall within the purview of your conundrums of philosophy."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*PING, POW*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nI solve practical problems."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*whirrrr, DING, AHHHHHHH*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nFr'instance..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...How am I going to stop some big mean mother hubbard from tearing me a structurally superfluous new behind?"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*DING, DING, DING, OHH*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nThe answer..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*PEW, PEW, PEW, PEW, PEW, AHHHHH*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...use a {}. And if that don't work....".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*CHUUU*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...use more {}.".format(word)
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*BOOM \"my arm!\"\nDING, DING*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\nLike this heavy caliber, tripod-mounted, little ol' number designed by me..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*DING... PING, PING*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n...Built by me..."
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n*whirrrr, PING, PING*"
        await self.bot.edit_message(edit, message)
        await asyncio.sleep(self.sleeptime)
        message += "\n\n..and you'd best hope... not pointed at you."
        await self.bot.edit_message(edit, message)

    @meethe.command(name='medic', pass_context=True, description='Types out the "Meet the Medic" script. Add a parameter to replace "" with your entry.')
    async def meethemedic(self, ctx):
        pass
    
    @meethe.command(name='sniper', pass_context=True, description='Types out the "Meet the Sniper" script. Add a parameter to replace "" with your entry.')
    async def meethesniper(self, ctx):
        pass
        
    @meethe.command(name='spy', pass_context=True, description='Types out the "Meet the Spy" script. Add a parameter to replace "" with your entry.')
    async def meethespy(self, ctx):
        pass
        
    @meethe.command(name='sandvich', pass_context=True, description='Types out the "Meet the Sandvich" script. Add a parameter to replace "" with your entry.')
    async def meethesandvich(self, ctx):
        pass

def setup(bot):
    bot.add_cog(TeamFortress(bot))
