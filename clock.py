import pyfiglet
import random
import datetime
import time

listadefontes = pyfiglet.FigletFont.getFonts()

while True:
    print("\n\n\n\n")
    hora_atual = datetime.datetime.now()
    hora_formatada_1 = (str(hora_atual.day)+" "+str(hora_atual.month)+" "+str(hora_atual.year))
    hora_formatada_2 = (str(hora_atual.hour) + " " + str(hora_atual.minute) + " " + str(hora_atual.second))

    fonte = random.choice(listadefontes)
    pyfiglet.print_figlet(hora_formatada_1, fonte, "green", width=80)
    pyfiglet.print_figlet(hora_formatada_2, fonte, "green", width=80)
    time.sleep(5)