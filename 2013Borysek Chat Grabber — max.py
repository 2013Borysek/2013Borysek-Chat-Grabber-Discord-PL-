import discord
from discord.ext import commands
TOKEN = "MTM1MDA3NDgwMzc1OTA4NzY2OA.GVAkK7.Mz9kYiDpv9QDhz4cc5rzSfW4sDZ20yx_z86tY8"

intents = discord.Intents.default()
intents.message_content = True  # Włącz, aby bot mógł czytać wiadomości

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    print(f'Nasłuchuję wiadomości na wszystkich kanałach')

@bot.event
async def on_message(message):
    # Ignorujemy wiadomości od samego bota, żeby nie robił pętli
    if message.author == bot.user:
        return message.content

    # Sprawdzamy, czy wiadomość pochodzi z określonego kanału
    print(f'''---------------------------------------------------------------------------------------------
{message.author.display_name}: {message.content}
Wiadomość napisana na kanale (ID): {message.channel.id}
------------------------------------------------------------------------------------------------------------''')

    # Pozwalamy na dalsze przetwarzanie komend przez bota
    await bot.process_commands(message)

bot.run(TOKEN)
