import pyfiglet
import random
import datetime
import time

listadefontes = pyfiglet.FigletFont.getFonts()

while True:
    print("\n\n\n\n")
    hora_atual = datetime.datetime.now()
    hora_formatada_1 = f"{hora_atual.day} {hora_atual.month} {hora_atual.year}"
    hora_formatada_2 = f"{hora_atual.hour} {hora_atual.minute} {hora_atual.second}"

    fonte = random.choice(listadefontes)
    pyfiglet.print_figlet(hora_formatada_1, fonte, "green", width=80)
    pyfiglet.print_figlet(hora_formatada_2, fonte, "blue", width=80)
    time.sleep(13)