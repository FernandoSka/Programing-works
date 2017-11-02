class Mamifero():
    """docstring for Mamifero"""
    cuenta = 0
    def __init__(self):
        self.__alimentacion = "carnivoro"
    def respirar(self):
        print("inhala....exhala...")
    def mostrar_ali(self):
        print(self.__alimentacion)
        

class Prro(Mamifero):
    cuenta = 0
    def __init__(self, ojos, pelo, estatura):
        self.ojos = ojos
        self.pelo = pelo
        self.estatura = estatura
        Prro.cuenta += 1
        Mamifero.cuenta += 1
        super(Prro, self).__init__()
        
    def raza(self, raza):
        self.raza = raza

    def ladra(self):
        print(" guau guau")

class Gato(Mamifero):
    cuenta = 0
    def __init__(self, ojos, pelo, estatura):
        self.ojos = ojos
        self.pelo = pelo
        self.estatura = estatura
        Gato.cuenta += 1
        Mamifero.cuenta += 1
        
    def raza(self, raza):
        self.raza = raza

    def ladra(self):
        print(" miau miau")