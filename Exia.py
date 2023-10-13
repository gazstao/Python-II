import pyttsx3

print(" 8 8888888888   `8.`8888.      ,8'  8 8888          .8.")
print(" 8 8888          `8.`8888.    ,8'   8 8888         .888. ")
print(" 8 8888           `8.`8888.  ,8'    8 8888        :88888.")
print(" 8 8888            `8.`8888.,8'     8 8888       . `88888. ")
print(" 8 888888888888     `8.`88888'      8 8888      .8. `88888.  ")
print(" 8 8888             .88.`8888.      8 8888     .8`8. `88888.   ")
print(" 8 8888            .8'`8.`8888.     8 8888    .8' `8. `88888.    ")
print(" 8 8888           .8'  `8.`8888.    8 8888   .8'   `8. `88888.   ")
print(" 8 8888          .8'    `8.`8888.   8 8888  .888888888. `88888.  ")
print(" 8 888888888888 .8'      `8.`8888.  8 8888 .8'       `8. `88888. ")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# for voice in voices:
#    print(voice.id)

engine.setProperty('voice', 'brazil')


def fale(_texto, _velocidade=130):
    if _velocidade < 110:
        _velocidade = 110
    elif _velocidade > 270:
        _velocidade = 270

    print(f"Falando {_texto} na velocidade {_velocidade}.")
    engine.setProperty('rate', _velocidade)
    engine.say(_texto)
    engine.runAndWait()


while True:
    print("\nO que quer que eu fale? ", end='')
    el_texto=input()
    if (el_texto == "exit()"):
        break
    fale(el_texto, 150)
