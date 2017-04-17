import discord, asyncio, datetime, requests
from discord.ext.commands import Bot
from discord.ext import commands
prefix = "%";
bot = Bot(command_prefix=prefix, description="The FRC Discord Bot, now with 100% more snakes!")

t = datetime.datetime.now()

@bot.event
async def on_ready():
    bot.load_extension("cogs.utils")
    print('Cogs Loaded.')
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')
    print("Connected to:")
    print("{} servers".format(servers))
    print("{} channels".format(channels))
    print("{} users".format(users))
    print('-------------')
    await bot.change_presence(game=discord.Game(name='FIRST Steamworks 2017'))

@bot.event
async def on_message(msg):
    content = msg.content;
    await bot.process_commands(msg)

@bot.command(hidden=True, pass_context=True)
async def shutdown(ctx):
    if isOwner(ctx):
        await bot.say("Shutting Down!")
        print('\n\n\n\n\n------------------------------------------------')
        print('Shutting down under request of ' + ctx.message.author.display_name)
        print('------------------------------------------------')
        await bot.close()
    else:
        await bot.say("You do not have permission to shut me down.")

@bot.command(name='eval', pass_context=True, description='Evaluates Python Code')
async def e(ctx):
    if isOwner(ctx):
        code = ' '.join(ctx.message.content.split()[1:])
        print('Evaluating code ' + code)
        embed = discord.Embed()
        embed.type='rich'
        embed.add_field(name='Code', value='```py\n%s\n```' % code, inline=False)
        try:
            ret = eval(code)
            embed.title = 'Python Evaluation - Success'
            embed.color = 0x00FF00
            embed.add_field(name='Output', value='```py\n%s\n```' % str(ret), inline=False)
        except Exception as err:
            embed.title = 'Python Evaluation - Error'
            embed.color = 0xFF0000
            embed.add_field(name='Error', value='```\n%s\n```' % str(err))
        await bot.send_message(ctx.message.channel, embed=embed)
    else:
        await bot.send_message(ctx.message.channel, "You do not have permission to use this command!")

# Work on this
@bot.command()
async def ping():
    datetime = datetime.now()
    await bot.say('Pong!')

@bot.command(name='reload', hidden=True)
async def _reload(arg):
    c = "cogs."
    try:
        bot.unload_extension(c + arg)
        bot.load_extension(c + arg)
    except Exception as e:
        await bot.say('\N{PISTOL}')
        await bot.say('{}: {}'.format(type(e).__name__, e))
    else:
        await bot.say('Reloaded module ' + arg)

# Work on this
def isOwner(ctx):
    return ctx.message.author.id == '171319044715053057'

if __name__ == '__main__':
    with open('token.txt', 'r') as oauth_token_file:
        oauth_token = oauth_token_file.readline().strip()
    client.run(oauth_token)
