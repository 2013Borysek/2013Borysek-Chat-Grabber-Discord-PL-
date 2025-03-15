import discord
from discord.ext import commands
TOKEN = ""  #<--- Tu wpisz TOKEN swojego bota Discord
while True:
    try:
        CHANNEL_ID = int(input("Podaj ID kanału Discord (BOT MUSI BYĆ NA TYM KANALE): "))  # Podmień na ID kanału, na który bot ma wysłać wiadomość
        break
    except ValueError:
        print('to nie liczba!')
