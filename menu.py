import pyfiglet
import random

listadefontes = pyfiglet.FigletFont.getFonts()

while True:
    fontealeatoria =  random.choice(listadefontes)
    pyfiglet.print_figlet("Python-II Menu", fontealeatoria,"green", width=150)
    print("1 - asciibanner")
    print("2 - Exia")
    print("3 - ToDoList")
    print("4 - RansomWhere")
    menu = input("\nQual sua escolha? ")
    match menu:
        case "1":
            import asciibanner
            asciibanner

        case "2":
            import Exia
            Exia

        case "3":
            import ToDoList
            ToDoList

        case "4":
            import RansomWhere

            eord = input("(E)ncrypt\n(D)ecrypt\nQual escolhe? ")
            match eord.capitalize()[0]:
                case "E":
                    RansomWhere.main("_AsciiArt","E")

                case "D":
                    RansomWhere.main("_AsciiArt","D")

        case "exit()":
            break