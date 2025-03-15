import discord
from discord.ext import commands
TOKEN = ""  #<--- Tu wpisz TOKEN swojego Bota Discord
while True:
    try:
        TARGET_USER_ID = int(input("Podaj ID profilu Discord: "))  # Podmień na ID kanału, na który bot ma wysłać wiadomość
        break
    except ValueError:
        print('to nie liczba!')
print('UWAGA! Jeśli masz w planach wysyłanie emoji, przeczytaj plik readmePL.txt!!!')



# Tworzymy instancję bota
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    user = await bot.fetch_user(TARGET_USER_ID)

    # Znajdź kanał, na który chcesz wysłać wiadomość

    # Wyślij wiadomość
    while True:
        to_send = input(f"Nowa wiadomość: ")
        await user.send(to_send)
        print(f"""--------------------------------------------------------------
{bot.user.display_name}: {to_send}
---------------------------------------------------------------------------""")


# Uruchomienie bota
bot.run(TOKEN)
