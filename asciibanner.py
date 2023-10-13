#
#        ▄▄▄        ██████  ▄████▄   ██▓ ██▓ ▄▄▄▄    ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███
#       ▒████▄    ▒██    ▒ ▒██▀ ▀█  ▓██▒▓██▒▓█████▄ ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
#       ▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▒██▒▒██▒▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
#       ░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒░██░░██░▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
#        ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░░██░░██░░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
#        ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░▓  ░▓  ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
#         ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒    ▒ ░ ▒ ░▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
#         ░   ▒   ░  ░  ░  ░         ▒ ░ ▒ ░ ░    ░   ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░
#             ░  ░      ░  ░ ░       ░   ░   ░            ░  ░         ░          ░    ░  ░   ░
#                          ░                      ░
#
# ASCIIBANNER is a Python program that takes user input and uses the pyfiglet module to create a file with
# ascii art from the desired word, with all the available fonts.
#

import pyfiglet
import random
import re
import os

dir_padrao = "_AsciiArt"
html_font_size = "12px"
html_background_color = "black"
html_color = "blue"
largura = 300
listadefontes = pyfiglet.FigletFont.getFonts()


def html_template(_banner):
    return('<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8">\n<meta name="viewport" '
           f'content="width=device-width, initial-scale=1.0"><title>{_banner}</title></head>\n'
           f'<body style="background-color: {html_background_color}; color: {html_color};">'
           f'<pre style="font-size: {html_font_size};"')


while True:

    fontealeatoria = random.choice(listadefontes)
    print(f"Fonte: {fontealeatoria}\n")
    pyfiglet.print_figlet("asciibanner", fontealeatoria, "green", width=largura)

    # Entrada do usuário
    banner = input("Texto: ")

    # Se escreveu exit sai fora
    if banner == "exit()":
        break
    elif banner == '':
        pass
    else:
        # ajusta o nome de arquivo para conter somente caracteres validos
        banner_name = re.sub('[^A-Za-z0-9]', '', banner)

        # Obtem o número de fontes disponiveis e exibe para o usuário o que será feito
        n = len(listadefontes)
        print(f"Criando arquivo {banner_name} com banners de {banner} em {n} fontes.")

        # Cria diretorio para arquivos caso não existe e o arquivo
        try:
            os.makedirs(dir_padrao)
            print(f"Criando diretório {dir_padrao}")
        except Exception as e:
            pass

        file = open(f"{dir_padrao}/_ascii_pure_art_banner_{banner_name}_.html", "w")
        file.write(html_template(banner))

        # Para cada fonte
        for font in listadefontes:

            # Cria banner para a fonte selecionada
            print(f"Criando banner de  {banner} com a fonte {font}.", end="\r")
            try:

                file.write(f"\n\n_____ FONTE: {font} _____ BANNER: {banner} _____ SIZE: {html_font_size} _____\n\n")
                art = pyfiglet.figlet_format(banner, font, direction='auto', justify='auto', width=largura)
                file.write(art)

            # Caso de erro, trata a excecao para manter o programa em execucao
            except Exception as e:
                print(f"ERRO: {e}", end="\r")
        print("                                                               ")
        print("\n\n\n")
        pyfiglet.print_figlet(banner, fontealeatoria, "blue", width=250)

        # grava o arquivo
        file.write("</pre></body></html>")
        file.close()
