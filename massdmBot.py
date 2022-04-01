import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "all?")

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

        self.reaction_role = None
        self.reaction_message = None

botdata = BotData()
@bot.event
async def on_ready():
    print("Your Bot Is Online :)")


@bot.command()
async def dm_all(ctx, *, arg=None):
    if arg != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "'to:"+member.name)

            except:
                print("Couldn't Send'"+ args + "' to:" + member.name)

    else:
         await ctx.channel.send("A Message was not Provided")

bot.run("Token")