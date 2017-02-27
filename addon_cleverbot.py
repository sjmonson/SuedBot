from isAllowed import *

CleverKey = tokens['CleverKey']       
cb = CleverWrap(CleverKey)

class CleverBotCommands():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Lets you talk to Cleverbot.')
    async def c(self, ctx, *, query : str):
        try:
            await self.bot.add_reaction(ctx.message, '👀')
            edit = None
        except:
            edit = await self.bot.say(waitmessage)

        response = cb.say(query)
        print("Taling to Cleverbot :: \n    %s\n    %s" % (query, response))
        await self.bot.say(response) if edit == None else await self.bot.edit_message(edit, response)
		
def setup(bot):
    bot.add_cog(CleverBotCommands(bot))