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
    print("5 - AsciiClock")
    print("\n9 - Sair")
    menu = input("\nQual sua escolha? ")
    if menu == "1":
        import asciibanner
        asciibanner

    if menu == "2":
        import Exia
        Exia

    if menu == "3":
        import ToDoList
        ToDoList

    if menu == "4":
        import RansomWhere

        eord = input("(E)ncrypt\n(D)ecrypt\nQual escolhe? ")
        if(eord.capitalize()[0]=="E"):
            RansomWhere.main("_AsciiArt","E")

        if (eord.capitalize()[0] == "D"):
            RansomWhere.main("_AsciiArt","D")

    if menu == "5":
        import clock
        clock.main()

    if menu == "9":
        break