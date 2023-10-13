#
# ASCIIBANNER is a Python program that takes user input and uses the
# pyfiglet module to create an HTML file with all the available font options.

import os

import pyfiglet
import re

dir_padrao = "_AsciiArt"
html_font_size = "10px"
html_background_color = "black"
html_color = "green"

def html_template(banner):
    return('<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8">\n<meta name="viewport" '
           f'content="width=device-width, initial-scale=1.0"><title>{banner}</title></head>\n<body>'
           f'<pre style="font-size: {html_font_size}; background-color: {html_background_color};'
           f'color: {html_color};>"')


print("\n\n  :::.     .::::::.   .,-:::::  ::::::  :::::::.    :::.   :::.    :::.:::.    :::..,:::::: :::::::..")
print("  ;;`;;   ;;;`    ` ,;;;'````'  ;;;;;;   ;;;'';;'   ;;`;;  `;;;;,  `;;;`;;;;,  `;;;;;;;'''' ;;;;``;;;;")
print(" ,[[ '[[, '[==/[[[[,[[[         [[[[[[   [[[__[[\. ,[[ '[[,  [[[[[. '[[  [[[[[. '[[ [[cccc   [[[,/[[['")
print("c$$$cc$$$c  '''    $$$$         $$$$$$   $$""""Y$$c$$$cc$$$c $$$ "Y$c$$  $$$ "Y$c$$ $$""""   $$$$$$c")
print(' 888   888,88b    dP`88bo,__,o, 888888  _88o,,od8P 888   888,888    Y88  888    Y88 888oo,__ 888b "88bo,')
print(' YMM   ""`  "YMmMY"   "YUMMMMMP"MMMMMM  ""YUMMMP"  YMM   ""` MMM     YM  MMM     YM """"YUMMMMMMM   "W" \n')

while True:

    # Entrada do usuário
    banner = input("\nTexto: ")

    # Se escreveu exit sai fora
    if (banner=="exit"):
        break

    # ajusta o nome de arquivo para conter somente caracteres validos
    banner_name = re.sub('[^A-Za-z0-9]+ ', '', banner)

    # Obtem o número de fontes disponiveis e exibe para o usuário o que será feito
    n = len(pyfiglet.FigletFont.getFonts())
    print(f"Criando arquivo {banner_name} com banners de {banner} em {n} fontes.")

    # Cria diretorio para arquivos caso não existe e o arquivo
    try:
        os.makedirs(dir_padrao)
        print(f"Criando diretório {dir_padrao}")
    except Exception as e:
        pass

    file = open(f"{dir_padrao}/_ascii_pure_art_banner_{banner_name}_.html","w")
    file.write(html_template(banner))

    # Para cada fonte
    for font in pyfiglet.FigletFont.getFonts():

        # Cria banner para a fonte selecionada
        print(f"Criando banner de  {banner} com a fonte {font}.")
        try:

            file.write(f"\n\n_________________ FONTE: {font} _________ BANNER: {banner} _________ \n\n")
            art = pyfiglet.figlet_format(banner, font, width=500)
            file.write(art)

        # Caso de erro, trata a excecao para manter o programa em execucao
        except Exception as e:
            print(f"ERRO: {e}")
    print("\n\n\n"+pyfiglet.figlet_format(banner,'big_money-sw', width=250))
    # grava o arquivo
    file.write("</pre></body></html>")
    file.close()
