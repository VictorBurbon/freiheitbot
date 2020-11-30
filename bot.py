import discord
from discord.ext import commands 
from discord import utils
import random
from discord.ext.commands import Bot
from random import choice
import asyncio
import datetime
from itertools import cycle
import os
from Cybernator import Rolegator

prefix = '/'

Bot = commands.Bot(command_prefix= prefix)

Bot.remove_command('help')

        

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('FREIHEIT (by Viktor Bag)'))
    print("Bot is online")


@Bot.command(pass_context= True)
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))


@Bot.command(pass_context= True)
async def info(ctx, member: discord.Member):
    """Информация о юзере """
    emb = discord.Embed(title= "Информация о {}".format(member.name), colour= 0x39d0d6)
    emb.add_field(name= "Ник", value= member.name)
    emb.add_field(name= "ID юзера", value= member.id)
    emb.add_field(name= "Создал аккаунт", value= str(member.created_at)[:16])
    emb.add_field(name= "Вошёл на сервер", value= str(member.joined_at)[:16])
    emb.set_thumbnail(url= member.avatar_url)
    emb.set_author(name= "Freiheit Bot", url= member.avatar_url)
    emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

    

@Bot.command(pass_context= True)
async def aboutserver(ctx):
    """Приветствие"""
    emb = discord.Embed(title= "Добро пожаловать на оф. дискорд сервер Freiheit", description= "`Доброго времени суток, приветствуем Вас на discord-сервере Freiheit.`                                                        `Freiheit - это свободное геймерское сообщество сплочённых игроков, где Вы можете найти себе напарника для любой игры.`                                       `Желаем Вам приятного времяпровождения, в нашей дружной компании.`                                                   `С уважением, Freiheit Team.`", colour= 0x39d0d6)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot • 29.11.20", icon_url= Bot.user.avatar_url)
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def autorole1(ctx):
    """Приветствие"""
    emb = discord.Embed(title= "Автовыдача роли по нажатию эмоции.", description= "`В данном канале Вы можете получить роль, той игры, в которую Вы играете.`", colour= 0x39d0d6)
    emb.add_field(name= "**Для того, чтобы получить роль, Вам нужно нажать по определённой эмоции ОДИН раз. Для того, чтобы СНЯТЬ роль, нужно снова нажать по определённой эмоции ОДИН раз.**", value= ".", inline=True)
    emb.add_field(name= "🧠 - DOTA ", value= "🔫 - CS GO", inline=True)
    emb.add_field(name= "🌳 - MINECRAFT", value= "🏃 - Escape from Tarkov", inline=True)
    emb.add_field(name= "🧤 - Rainbow Six Siege", value= "✈️ - War Thunder", inline=True)
    emb.add_field(name= "🌰 - Apex", value= "👽 - Paladins", inline=True)
    emb.add_field(name= "💀 - Killing Floor 2", value= "😈 - Among Us", inline=True)
    emb.add_field(name= "🤖 - Overwatch", value= "👑 - GTA 5", inline=True)
    emb.add_field(name= "👞 - RDR 2", value= "👨‍💻 - Watch Dogs 2", inline=True)
    emb.add_field(name= "☢️ - STALKER", value= "🚚 - ETS 2", inline=True)
    emb.set_footer(text= "Freiheit Bot • 29.11.20", icon_url= Bot.user.avatar_url)
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def autorole2(ctx):
    """Приветствие"""
    emb = discord.Embed(title= "Автовыдача роли по нажатию эмоции.", description= "`Продолжение.`", colour= 0x39d0d6)
    emb.add_field(name= "🤠 - Command and Conquer Generals ", value= "🧙‍♀️ - Warframe", inline=True)
    emb.add_field(name= "🧙‍♂️ - Destiny 2", value= "🦸 - PUBG", inline=True)
    emb.add_field(name= "🧟‍♀️ - Witcher 3", value= "🧝‍♂️ - Skyrim", inline=True)
    emb.add_field(name= "💪 - Arma", value= "👮 - Garry’s Mod", inline=True)
    emb.add_field(name= "🤘 - PayDay 2", value= "👌 - WILDLANDS", inline=True)
    emb.add_field(name= "🍏 - Team Fortress", value= "🍆 - Titanfall", inline=True)
    emb.set_footer(text= "Freiheit Bot • 29.11.20", icon_url= Bot.user.avatar_url)
    await ctx.send(embed= emb)




@Bot.command(pass_context= True)
async def rules(ctx):
    """Правила"""
    emb = discord.Embed(title= "Правила Discord-сервера Freiheit. [RUS]", description= "`За нарушение любого из перечисленных правил, Вы будете предупреждены, при повторном нарушении получите БАН.`", colour= 0x4f545c)
    emb.add_field(name= "**Не оскорблять, издеваться, унижать кого - либо.**", value= "Переход на личности, в присутствии более чем 2 людей, не учитывая конфликтные стороны, имеет возможность оспорения. Если есть притензии к кому-то, то беседа 1/1 в отдельной комнате.", inline=True)
    emb.add_field(name= "**Если стоит необходимость замутить, забанить либо кикнуть нарушителя - пишите модерации Main Invoice.**", value= ".", inline=True)
    emb.add_field(name= "**Не спамить, не мутить без причины, не кикать без причины из комнаты.**", value= "Личный мут возможен с предупреждением админов.", inline=True)
    emb.add_field(name= "**Порнография, реклама, продажа игровых ценностей/аккаунтов в общем чате запрещена.. **", value= ".", inline=True)
    emb.add_field(name= "**Участники нашего сообщества которые будут использовать читы, софты будут забанены(предупреждены)**", value= ".", inline=True)
    emb.add_field(name= "**Запрещено использовать команды casino в других каналах, кроме casino-spam**", value= ".", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)


@Bot.command(pass_context= True)
async def rules_eng(ctx):
    """Правила"""
    emb = discord.Embed(title= "Rules of Discord-server Freiheit. [ENG]", description= "`For violation of any of the listed rules, you will be warned, if the BAN is violated again.`", colour= 0x4f545c)
    emb.add_field(name= "**No one can't use bad language, humiliate, mock**", value= "(the transition to a person, in the presence of more than 2 people, not taking into account the frustration owns the possibility of contesting) (if there are prints to someone, the conversation 1/1 in a separate room).", inline=True)
    emb.add_field(name= "**If you want to ban somebody, kick them out, mute them,  write in  Main invoce.**", value= ".", inline=True)
    emb.add_field(name= "**Do not spam, do not mute for no reason (general mute), do not kick without reason (from the room)**", value= "(personal mute is possible with a warning from admins)", inline=True)
    emb.add_field(name= "**Pornography is forbidden, advertising is forbidden, selling game values/accounts in general chat is forbidden.**", value= ".", inline=True)
    emb.add_field(name= "**The people on our server who will use cheats, the software will be banned**", value= ".", inline=True)
    emb.add_field(name= "**You can use command casino-bot only in casino-spam**", value= ".", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)




@Bot.command(pass_context= True)
async def predlog(ctx):
    """Предложения по улучшению"""
    emb = discord.Embed(title= "Предложения по улучшению Discord-сервера Freiheit.", description= "`Уважаемые участники сообщества Freiheit, если у Вас есть предложения по улучшению и развитию нашего Discord-сервера, Вы можете изложить их в этом канале. Рассматриваются любые разумные предложения и нововведения.`", colour= 0x39d0d6)
    emb.add_field(name= "**Запрещенны любые проявления offtop`a. Форма подачи предложения по улучшению свободная, главное чёткое и обоснованое объяснение цели и необходимость нововведения. Чтобы вашу идею приняли потребуется 7 позитивных голосов.**", value= "С уважением, Freiheit Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def meme(ctx):
    """Приколы"""
    emb = discord.Embed(title= "Screenshots and Memes.", description= "`Уважаемые участники сообщества Freiheit, если у Вас есть интересные скриншоты, либо смешные мемы, Вы можете поделиться ими в этом текстовом канале.`", colour= 0x39d0d6)
    emb.add_field(name= "**Offtop/flood в данном канале карается длительным mute`ом.**", value= "С уважением, Freiheit Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def razdat(ctx):
    emb = discord.Embed(title= "Раздачи и конкурсы", description= "`Уважаемые участники Freiheit, в данном текстовом канале будут проходить разнообразные раздачи (Giveaway) и конкурсы.`", colour= 0x39d0d6)
    emb.add_field(name= "**Если Вы хотите стать спонсором или организатором любой раздачи либо конкурса, отписывайте модераторам Freiheit Team.**", value= "С уважением, Freiheit Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= "Freiheit Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)


@Bot.command(pass_context= True) 
async def help(ctx): 
    emb = discord.Embed(title= "Команды", colour= 0x39d0d6)
    emb.add_field(name= "Информация про команды", value= "`{}help`".format(prefix))
    emb.add_field(name= "Проверить ping", value= "`{}ping`".format(prefix))
    emb.add_field(name= "Игра Coin", value= "`{}coin`".format(prefix))
    emb.add_field(name= "Посмотреть аватарку юзера", value= "`{}avatar @username`".format(prefix))
    emb.add_field(name= "Игра 8-ball", value= "`{}ball`".format(prefix))
    emb.add_field(name= "Правила сервера", value= "`{}rules`".format(prefix))
    emb.add_field(name= "Информация о юзере", value= "`{}info @username`".format(prefix))
    emb.add_field(name= "Команды для модератора:", value= "`/petuh`,`/say <channel> <text>`,`/update_channel <channel>`,`/update_channel2 <channel>`,`/giveaway <channel> <msgid>`,`/cmd`,`/ban`,`/mute`,`/unmute`,`/kick`,`/clear`", inline=True)
    emb.set_image(url= "https://i.imgur.com/GtJtvm6.png")
    emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command()
@commands.has_permissions(manage_messages = True) 
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() 
   embed = discord.Embed(description = cnt, colour = 0x00ff80) 
   await channel.send(embed=embed) 

@Bot.command(pass_context=True, name= 'ping', brief= 'Показать текущую задержку')
@commands.cooldown(1, 1, commands.BucketType.user)
async def ping(ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        emb = discord.Embed(title= '**Текущая задержка:**', description= f'``{Bot.ws.latency * 1000:.0f} ms``', colour= 0x00ff80)
        emb.set_author(name= f'Ping', icon_url= Bot.user.avatar_url)
        emb.set_footer(text= f'{ctx.author}', icon_url= ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)

@commands.has_permissions(administrator=True)
@Bot.command()
async def petuh(ctx):

    role = ctx.guild.get_role(657904038913900573) 

    balbes = "Ghetto Петухов"
    bot = "бота"
    bots = "бота"
    member = "участников"
    members = "участников"

    members_counter = len(ctx.guild.members)
    role_counter = len([m for m in ctx.guild.members if role in m.roles])
    bots_counter = len([m for m in ctx.guild.members if m.bot])
    valid_members = [m for m in ctx.guild.members if not m.bot and role not in m.roles]

    if members_counter - bots_counter < 2:
        return await ctx.send(f'{ctx.author.mention} Ты один на сервере, {"не считая меня!" if bots_counter == 1 else f"не считая {bots_counter} {bot}!"}')

    elif not valid_members:
        return await ctx.send('**ой, все пользователи уже Ghetto Петушня!** :smirk:')

    elif len(valid_members) is 1:
        await ctx.send(f'{ctx.author.mention} Ну тут выбор очевиден! На сервере остался только один человек без роли :smirk:')
        random_member = valid_members[0]
    else:
        await ctx.send(f'{ctx.author.mention} Немного подожди, я выбераю рандомного Ghetto Петуха среди **{members_counter}** {member}! :smirk:'
                       f'\nА если быть точнее то из **{members_counter - bots_counter - role_counter}**, т.к на сервере ' + \
                       (f'**{bots_counter}** {bots}' if bots_counter > 1 else 'есть я, а я не считаюсь') + \
                       f' и у **{role_counter}** {members} уже есть роль!')

        try:
            await asyncio.sleep(5)
            random_member = choice(valid_members)
            await random_member.add_roles(role)
        except Exception as error:
            return await ctx.send(f'**Произошло GG **{type(error).__name__}**:\n{error}')

    embed = discord.Embed(
        color=0x99ff99,
        description=f'Роль {role.mention} присуждается {random_member.mention}\nТеперь на сервере **{role_counter + 1}** {balbes}')
    embed.set_footer(text= f"Вызвал(а): {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    await ctx.send(embed=embed)


@Bot.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
    embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@Bot.command()
async def coin(ctx):
    num=random.randint(1,2)
    if (num == 1):
           await ctx.send("Вым выпал - Орёл")
           print("[?coin] - done")
    if(num == 2):    
           await ctx.send("Вам выпала - Решка")
           print("[?coin] - done")
        



@Bot.command()
@commands.has_permissions(administrator = True) 
async def cmd(ctx):
    await ctx.message.delete() 
    role = ctx.guild.get_role(635146252543066122) 
    emb = discord.Embed(title= "GIVEAWAY начат", description=f" {role.mention} **Для участия нажмите на реакцию ниже. Приз: unknown_argument.**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсор: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb) 

@Bot.command()
@commands.has_permissions(administrator = True) 
async def giveaway(ctx, channel: discord.TextChannel, msgid: int):
    await ctx.message.delete() 
    await asyncio.sleep(20)
    message = await channel.fetch_message(msgid)
    users = set([user for reaction in message.reactions for user in await reaction.users().flatten()])
    random_member = random.sample(users, 1)[0] 
    emb = discord.Embed(title= "GIVEAWAY закончен", description=f"**Участник {random_member.mention} выиграл приз! Поздравляем!**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсором был: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb)


@Bot.command()
async def update_channel(ctx, channel: discord.VoiceChannel, *, new_name):
 members_counter = len(ctx.guild.members)
 channel = Bot.get_channel(658049586501255168)
 await channel.edit(name=f" 📌 Нас: {members_counter}")

@Bot.command()
async def update_channel2(ctx, channel: discord.VoiceChannel, *, new_name):
 guild=ctx.message.guild
 total_text_channels = len(guild.text_channels + guild.voice_channels)
 channel = Bot.get_channel(658058242559311882)
 await channel.edit(name=f" 📌 Всего каналов: {total_text_channels}")

class Messages:

    def __init__(self, Bot):
        self.Bot = Bot

    async def number_messages(self, member):
        n_messages = 0
        for guild in self.Bot.guilds:
            for channel in guild.text_channels:
                try:
                    async for message in channel.history(limit = None):
                        if message.author == member:
                            n_messages += 1
                except (discord.Forbidden, discord.HTTPException):
                    continue
        return n_messages

@Bot.command(name = "messages")
async def msg(ctx, member: discord.Member = None):
    user = ctx.message.author if (member == None) else member
    messages = Messages(Bot)
    number = await messages.number_messages(user)
    embed = discord.Embed(description = f"Количество сообщений на сервере от **{user.name}** — **{number}**!")
    await ctx.send(embed = embed)



Rolegator(bot=Bot,
          emoji_role={'🧠': 782699702868377611, #dota
                      '🔫': 782700088698470421, #cs_go
                      '🌳': 782700168013021224,  #minecraft
                      '🏃': 782700242135023667, #tarkov
                      '🧤': 782700356983324692, #six siege
                      '✈️': 782700456098791465, #war thunder
                      '🌰': 782700526671495169,  #apex
                      '👽': 782700606585831435, #paladins
                      '💀': 782700678854344759, #killing flor 2
                      '😈': 782700744045494302, #among us
                      '🤖': 782700800413138975, #overwatch
                      '👑': 782700864636715018, #GTA5
                      '👞': 782700948279394314, #RDR2
                      '👨‍💻': 782701004402720818, #WATCH DOGS 2
                      '☢️': 782701092349149215, #STALKER
                      '🚚': 782701221390581782 #ETC2
          },
          message_id=782708834815705128,
          channel_id=782708075115053096,
          role_remove=True, 
          role_member_join=False).start()


Rolegator(bot=Bot,
          emoji_role={'🧙‍♂️': 782701513977102336, #desteny2
                      '🦸': 782701601496104990, #PUBG
                      '🧟‍♀️': 782701676406636585, #Witcher 3
                      '🧝‍♂️': 782701768693121025, #SkyRim
                      '💪': 782702227143131168, #ARMA
                      '👮': 782702267635335208, #GarrysMode
                      '🤠': 782701330199347260, #GENERALS 
                      '🧙‍♀️': 782701403914240021, #warframe
                      '🤘': 782702776459329586, #payday
                      '👌': 782702336350486589, #breackpoint
                      '🍏': 782702446144520212, #team fortress
                      '🍆': 782702532417945621 #titan
          },
          message_id=782708867120496661,
          channel_id=782708075115053096,
          role_remove=True, 
          role_member_join=False).start()





@Bot.command()
async def clear(ctx, *,number:int=None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send("**Используй: /clear 'количество сообщений'**")
            else:
                deleted = await ctx.message.channel.purge(limit=number)
                await ctx.send(f'Модератор {ctx.author.mention} стёр: `{len(deleted)}` сообщений')
        except:
            await ctx.send("Я не могу очистить сообщение")
    else:
        await ctx.send('Вы не имеете право использовать эту команду!')


@Bot.command()
async def kick(ctx, member: discord.User = None, reason= None):
    if ctx.message.author.guild_permissions.administrator:
        try:
            if member == None:
                await ctx.send("**Используй: /kick '@username' 'причина'**")
            elif reason == None:
                await ctx.send("Используй: /kick '@username' 'причина'")
            else:
                await ctx.guild.kick(member)
                emb = discord.Embed(title= f"Участник {member}, был кикнут.", description= f"По причине: {reason}", color= 0x000000)
                await ctx.send(embed= emb)
        except:
            await ctx.send("Ошибка.")
    else:
        await ctx.send('Вы не имеете право использовать эту команду!')

    
@Bot.command()
async def mute(ctx, member: discord.Member = None, seconds = None, reason = None):
    if ctx.message.author.guild_permissions.administrator:
        try:
            if member == None:
                await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
            elif seconds == None:
                await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
            elif reason == None:
                await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
            else:
                role = ctx.guild.get_role(782970037274411060) 
                sec = float(seconds)
                emb = discord.Embed()
                await member.add_roles(role)
                emb.set_author(name = "{} замучен на {} секунд по причине: {}".format(member, seconds, reason))
                await ctx.send(embed = emb)
                await asyncio.sleep(sec)
                await member.remove_roles(role)
                embed = discord.Embed()
                embed.set_author(name = "{} размучен по истечении времени.".format(member))
                await ctx.send(embed = embed)
        except:
            await ctx.send("Ошибка.")
    else:
        await ctx.send('Вы не имеете право использовать эту команду!')


@Bot.command(pass_context= True)
async def ban(ctx, member: discord.User = None, reason = None):
    if ctx.message.author.guild_permissions.administrator:
        try:
            if member == None:
                await ctx.send("**Используй: /ban '@username' 'причина'**")
            elif reason == None:
                await ctx.send("**Используй: /ban '@username' 'причина'**")
            else:
                await ctx.guild.ban(member)
                emb = discord.Embed(title= f"**Участник {member}, был забанен.**", description= f"**По причине: {reason}**", color= 0x000000)
                await ctx.send(embed= emb)
        except:
            await ctx.send("Ошибка.")
    else:
        await ctx.send('Вы не имеете право использовать эту команду!')

@Bot.command()
async def unmute(ctx, member : discord.Member = None):
    if ctx.message.author.guild_permissions.administrator:
        try:
            if member == None:
                await ctx.send("**Используй: /unmute '@username'**")
            else:
                membern = member.nick
            if member.nick == None:
                membern = member.name
                unmute_cnt = f"Пользователь {membern} быз раззамучен модератором {ctx.author}!"
                emb = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x000000)
                role = ctx.guild.get_role(782970037274411060)
                await member.remove_roles(role)
                await ctx.send(embed= emb)
        except:
            await ctx.send("Ошибка.")
    else:
        await ctx.send('Вы не имеете право использовать эту команду!')


@Bot.command()
async def ball(ctx, text: str=None):
     if not text:
             return await ctx.send('**Используй: /ball "Вопрос"**')
     try:
             num=random.randint(1,4)
             if (num == 1):
                await ctx.send("Однозначно - да :ok_hand_tone5: ")
                print("[?coin] - done")
             if(num == 2):    
                 await ctx.send("Мой ответ - нет :thumbsdown_tone5: ")
                 print("[?coin] - done")
             if (num == 3):
                 await ctx.send("Скорее всего :smiling_imp: ")
                 print("[?coin] - done")
             if (num == 4):
                 await ctx.send("Даже не думай :skull_crossbones: ")
                 print("[?coin] - done")
                 await ctx.message.add_reaction("✅")
     except Exception as e:
         await ctx.message.add_reaction("❌")
         await ctx.author.send(e)


           
token = os.environ.get('BOT_TOKEN')                

Bot.run(str(token))
