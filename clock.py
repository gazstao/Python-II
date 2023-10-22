import pyfiglet
import datetime
import time
import os
import random
import keyboard


def main():

    listadefontes = pyfiglet.FigletFont.getFonts()
    fonte = "basic"
    largura = 150

    while True:
        print("\n\n\n\n")
        hora_atual = datetime.datetime.now()
        hora_formatada_1 = hora_atual.strftime("%d %b %y")
        hora_formatada_2 = hora_atual.strftime("%H %M %S")

        if (keyboard.is_pressed("enter") | keyboard.is_pressed(" ")):
            fonte = random.choice(listadefontes)
            print(f"\nalterando fonte aleatoriamente para {fonte}\npressione Q para sair")
            time.sleep(2)

        if (keyboard.is_pressed("q")):
            break

        os.system('cls')
        pyfiglet.print_figlet(hora_formatada_1, fonte, "green", width=largura, justify="center")
        pyfiglet.print_figlet(hora_formatada_2, fonte, "blue", width=largura, justify="center")
        time.sleep(1)