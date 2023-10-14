import pyfiglet
import datetime
import time
import os
import random
import keyboard

listadefontes = pyfiglet.FigletFont.getFonts()
fonte = "basic"

while True:
    print("\n\n\n\n")
    hora_atual = datetime.datetime.now()
    hora_formatada_1 = hora_atual.strftime("%d %b %Y")
    hora_formatada_2 = hora_atual.strftime("%H %M %S")
    #hora_formatada_1 = f"{hora_atual.day} {hora_atual.month} {hora_atual.year}"
    #hora_formatada_2 = f"{hora_atual.hour} {hora_atual.minute} {hora_atual.second}"

    if (keyboard.is_pressed("enter")):
        fonte = random.choice(listadefontes)

    os.system('cls')
    pyfiglet.print_figlet(hora_formatada_1, fonte, "green", width=90, justify="center")
    pyfiglet.print_figlet(hora_formatada_2, fonte, "blue", width=90, justify="center")
    time.sleep(1)