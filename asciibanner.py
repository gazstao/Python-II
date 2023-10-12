import pyfiglet

while True:
    banner = input("Texto: ")
    if (banner=="exit"):
        break

    file = open(f"asciibanner_{banner}_.txt","w")
    for font in pyfiglet.FigletFont.getFonts():
        try:
            ascii_banner = pyfiglet.figlet_format(banner, font)
            file.write(ascii_banner+"\n\n")
            print(ascii_banner+"\n\n")
        except Exception as e:
            print(f"ERRO: {e}")

    file.close()

