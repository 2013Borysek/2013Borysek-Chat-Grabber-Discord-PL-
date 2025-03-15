from Global import *

intents = discord.Intents.default()
intents.message_content = True  # Włącz, aby bot mógł czytać wiadomości

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    print(f'Nasłuchuję wiadomości na kanale {CHANNEL_ID}')

@bot.event
async def on_message(message):
    # Ignorujemy wiadomości od samego bota, żeby nie robił pętli
    if message.author == bot.user:
        return message.content

    # Sprawdzamy, czy wiadomość pochodzi z określonego kanału
    if int(message.channel.id) == int(CHANNEL_ID):
        print(f'{message.author.display_name}: {message.content}')

    # Pozwalamy na dalsze przetwarzanie komend przez bota
    await bot.process_commands(message)

bot.run(TOKEN)
