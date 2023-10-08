#!/usr/bin/python3

print(" ####  #        ##    ####   ####   ####   ####  #    #  ####  ###### #####  #####  ####")
print("#    # #       #  #  #      #      #    # #    # ##   # #    # #      #    #   #   #      ")
print("#      #      #    #  ####   ####  #      #    # # #  # #      #####  #    #   #    ####  ")
print("#      #      ######      #      # #      #    # #  # # #      #      #####    #        # ")
print("#    # #      #    # #    # #    # #    # #    # #   ## #    # #      #        #   #    # ")
print(" ####  ###### #    #  ####   ####   ####   ####  #    #  ####  ###### #        #    ####  ")

class Humano:
    def __init__(self):
        pass


    # accessors
    def set_altura(self, altura):
        self.altura = altura
    def get_altura(self):
        return self.altura

    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso

def main():
    ramu = Humano()
    ramu.set_altura(1.74)
    ramu.set_peso(70.0)

    print(ramu)
    print(ramu.peso)
    print(ramu.altura)
    print(ramu.get_peso())
    print(ramu.get_altura())
    print(type(ramu))

if __name__ == "__main__":
    main()