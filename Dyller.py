#Dyller bot by Declan

import discord
import random
from discord.ext import commands



#Prefix

client = commands.Bot(command_prefix='.')

#Commands

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Dylanland, Who will win?'))
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print(client.user.created_at)
    print('--------------')
    print('Bot is Ready')
    print('--------------')





                   
@client.command()
async def echo(*args):
    output = '' 
    for word in args:
        output += word
        output += ' '
    await client.say(output)

#Network Connection

@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def ping(ctx):
    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, f'Pong! That took {1000*diff.total_seconds():.1f}ms.')



@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def add(ctx, a: int, b: int):
    await client.say(a+b)

#Other

@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def multiply(ctx, a: int, b: int):
    await client.say(a*b)

@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def greet(ctx):
    await client.say(":smiley: :wave: Hello, there and welcome!")



@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def info(ctx):
    await client.say("This bot is owned by Deccyboy#1083. Report any bugs to him")

@client.command(pass_context=True)
async def clear(ctx, amount=2000):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted! :white_check_mark:')


@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def flip():
    choice = (random.choice(["heads", "tails"]))
    await client.say("It is: " + choice)


@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def dice():
    choice = (random.choice(["1", "2", "3", "4","5","6"]))
    await client.say("You rolled: " + choice)

@client.command(pass_context=True)
async def servers(ctx, n: int=10):
    servers = list(client.servers)
    n = min(n, len(servers))
    embed = discord.Embed(title=f"Top {n} servers")
    for server in sorted(servers, key=lambda x: x.member_count, reverse=True)[:n]:
        embed.add_field(name=server.name, value=f"{server.member_count} members", inline=False)
    await client.say(embed=embed)



@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def invite():
    await client.say("Join the offcial help discord using this invite code: https://discord.gg/VyHjr4P")

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def dylanland():
    await client.say("You can join Dylanland by using this code:https://discord.gg/vPFdg8X ")

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def Help():
    await client.say("@Hosts Please help me. I am having trouble! ")

@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def userinfo(ctx, user: discord.Member):
    emb2 = (discord.Embed(description='' + format(user.name) + ' Information :', color=0xff65a6))
    emb2.set_author(name="User Info",
                    icon_url="")
    emb2.set_thumbnail(url=user.avatar_url)
    emb2.add_field(name="**Username**", value=format(user.name))
    emb2.add_field(name="**User ID**", value=format(user.id))
    emb2.add_field(name="**User Status**", value=format(user.status))
    emb2.add_field(name="** User Highest Role**", value=format(user.top_role))
    emb2.add_field(name="** User Joined At   **", value=format(user.joined_at))
    await client.say(embed=emb2)


#Autoroling

@client.event
@commands.cooldown(1, 15, commands.BucketType.user)
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='ALPHA')
    await client.add_roles(member, role)



client.run("NDYyOTE4NjI2Nzc4MDIxODg4.Dms3vg.ABeOaGCXDM8b6321A4xADaLBM28")
