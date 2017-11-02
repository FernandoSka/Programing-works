from abc import ABCMeta, abstractmethod
class Mamifero( ):
    __metaclass__ = ABCMeta
    cuenta = 0
    @abstractmethod
    def __init__(self, alimentacion):
        self.alimentacion = alimentacion
        Mamifero.cuenta += 1

    @abstractmethod
    def respirar(self):
        print("inhala...exhala")

class Gato(Mamifero):
    cuenta = 0
    def __init__(self, ojos, pelo, estatura):
        self.ojos = ojos
        self.pelo = pelo
        self.__estatura = estatura
        Gato.cuenta += 1
        super(Gato, self).__init__("carnivoro")
    def maulla(self):
        print("miau miau mdfk")

class Prro(Mamifero):
    cuenta = 0
    def __init__(self, ojos, pelo, estatura):
        self.ojos = ojos
        self.pelo = pelo
        self.estatura = estatura
        Prro.cuenta += 1
        super(Prro, self).__init__("omnivoro")
    def maulla(self):
        print("guau guau mdfk")

misifus = Gato("verdes", "rojo", 54)
misifus2 = Gato("", "naranja", 48)
misifus.maulla()
misifus.respirar()
print(misifus.ojos)
print(misifus.alimentacion)
print(Mamifero.cuenta)
