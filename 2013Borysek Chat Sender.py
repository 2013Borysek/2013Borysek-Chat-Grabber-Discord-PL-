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
