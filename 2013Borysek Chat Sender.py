'''
from Global import *

TOKEN = "MTM1MDA3NDgwMzc1OTA4NzY2OA.GVAkK7.Mz9kYiDpv9QDhz4cc5rzSfW4sDZ20yx_z86tY8"
CHANNEL_ID = input("Podaj ID kanału Discord (BOT MUSI BYĆ NA TYM KANALE): ")  # Podmień na ID kanału, na który bot ma wysłać wiadomość
MESSAGE = "Cześć! Jestem botem! 🤖"

intents = discord.Intents.default()
intents.message_content = True  # <-- To pozwala botowi czytać wiadomości!
bot = commands.Bot(command_prefix="!", intents=intents)

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE)
    else:
        print("Nie znaleziono kanału!")
bot.add_cog(BasicCommands(bot))  # Dodanie klasy komend
bot.run(TOKEN)
'''
from Global import *
print('UWAGA! Jeśli masz w planach wysyłanie emoji, przeczytaj plik readmePL.txt!!!')


# Tworzymy instancję bota
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

    # Znajdź kanał, na który chcesz wysłać wiadomość
    channel = bot.get_channel(CHANNEL_ID)

    # Wyślij wiadomość
    while True:
        to_send = input(f"Nowa wiadomość: ")
        await channel.send(to_send)
        print(f"""--------------------------------------------------------------
{bot.user.display_name}: {to_send}
---------------------------------------------------------------------------""")


# Uruchomienie bota
bot.run(TOKEN)
