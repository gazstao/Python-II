import pyfiglet
import datetime
import time
import os
import random
import keyboard

listadefontes = pyfiglet.FigletFont.getFonts()
fonte = "basic"
largura = 150
banner = "gazstao       "
tam = len(banner)

while True:
    print("\n\n\n\n")
    hora_atual = datetime.datetime.now()
    hora_formatada_1 = hora_atual.strftime("%d %b %y")
    hora_formatada_2 = hora_atual.strftime("%H %M %S")
    #hora_formatada_1 = f"{hora_atual.day} {hora_atual.month} {hora_atual.year}"
    #hora_formatada_2 = f"{hora_atual.hour} {hora_atual.minute} {hora_atual.second}"

    if (keyboard.is_pressed("enter") | keyboard.is_pressed(" ")):
        fonte = random.choice(listadefontes)

    os.system('cls')
    pyfiglet.print_figlet(hora_formatada_1, fonte, "green", width=largura, justify="center")
    pyfiglet.print_figlet(hora_formatada_2, fonte, "blue", width=largura, justify="center")
    pyfiglet.print_figlet(banner, fonte, "red", width=largura, justify="center")
    # rolling banner
    banner = f"{banner[tam-1:]}{banner[0:tam-1]}"
    time.sleep(1)