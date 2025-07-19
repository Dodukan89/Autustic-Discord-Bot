import discord
from discord.ext import commands
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

İMAGELER ="images"
os.makedirs(İMAGELER, exist_ok=True)

@bot.event
async def on_ready():
    print(f'Sunucuya giriş yaptık!{bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Selam! ben {bot.user}!')

@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(İMAGELER, file_name)

            try: #Hata yakalama bloğu
                await attachment.save(file_path)
                print(f"{file_name} Adlı dosya kaydedildi!")
                class_name , confidence_score= get_class(image_path=file_path)
                if class_name == "Absurd":
                    await ctx.send(f"ben bu konu hakkında konuşmak istemiyorum senin yüzünden şimdi gidip kablolarımı ısıracağım.")
                    await ctx.send(f"Doğruluk payı: {confidence_score}")
                elif class_name == "Stylized":
                    await ctx.send(f"Bu görsel gerçekten çok etkileyici ve çok güzel duruyor gözüm gönlüm açıldı")
            except Exception as e:
                await ctx.send(f"Dosyanız kabul edilemedi! {file_name}. Error: {e}")#Hata mesajı
    else:
        await ctx.send("Dostum yapay zekadan dosya göndermeyerek dosya kontrol etmemi bekledi 💀💀💀💀💀")

@bot.command()
async def kapat(ctx):
    await ctx.send("ben yatiyorum iyigeceler")
    await bot.close()


bot.run("lil bro try steal my bot🤣🤣🤣🐟🐟😭🙏🙏🙏")
