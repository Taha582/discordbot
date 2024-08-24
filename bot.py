import discord
import random
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$nasılsın'):
        await message.channel.send("iyim sorduğun için teşekkürler:)")
    elif message.content.startswith('/sorduğum tüm sorulara cevap verebilirmisin'):
        await message.channel.send("bilimsel sorulara cevap veremem")
    elif message.content.startswith('/ne işe yararsın'):
        await message.channel.send("ben bir sohbet botu olduğum için pek bir işe yaramam")
    elif message.content.startswith('adın ne'):
        await message.channel.send("bir bot olduğum için insanlar gibi bir adım yok")
    elif message.content.startswith('Trabzonspor en son ne zaman şampion oldu'):
        await message.channel.send("trabzonspor enson 2021-2022 sezonunda şampiyon oldu")
    elif message.content.startswith('dolar kaç tl oldu'):
        await message.channel.send("mağlesef güncel bilgi veremediğimden  bir cevap veremem")
    elif message.content.startswith('ne kadar bilgilisin'):
        await message.channel.send("geliştiricim ne kadar bilgi yüklerse okadar bilgiliyim")
    elif message.content.startswith('Osmanlının 7. padişahı kimdir'):
        await message.channel.send("Osmanlının 7. padişahı Fatih Sultan Mehmeddir")
        
    
    else: 
        await message.channel.send(message.content)
client.run("MTI3NjI0NzUwMTc3ODcxODczMA.GlJUf2.bbDijoD6BnquxfOI29ua00WqEFtEfe9JzeAfK0")
