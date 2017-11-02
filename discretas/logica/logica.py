
"""Matematicas Discretas.

Documentation:

This library is designed to calculate the four basic operations of
propositional logic :

Union
Intersection
Conditional
biconditional

We only need to declare an array with the same length and put only boolean
 characters
after we can do the operations calling the class and pass off the parameters
-----------------------------
Clases:

Interseccion():
return the intersection

Union():
return the Union

Condicional():
return the Conditional

Bicondicional():
return the bicondicional
--------------------------
Methods:

show(): print the result array in the console

result(): return the result value


---------------------------
Example:
from logica import Union

X = [False, True]
Y = [True, True]

XUY = Union(X, Y)//create the instance
XUY.show()//call the function "show()" and print the result


"""


class Interseccion(object):
    """Clase Interseccion."""

    def __init__(self, conj1, conj2):
        """Paso de parametros."""
        interseccion = []
        for x in range(0, len(conj1)):
            interseccion.append(conj1[x] & conj2[x])
        self.interseccion = interseccion

    def show(self):
        """Mostrar la interseccion."""
        print(self.interseccion)

    def result(self):
        """Regreso el parametro."""
        return(self.interseccion)


class Union(object):
    """Clase Interseccion."""

    def __init__(self, conj1, conj2):
        """Paso de parametros."""
        union = []
        for x in range(0, len(conj1)):
            union.append(conj1[x] | conj2[x])
        self.union = union

    def show(self):
        """Mostrar la interseccion."""
        print(self.union)

    def result(self):
        """Regreso el parametro."""
        return(self.union)


class Condicional(object):
    """Clase Interseccion."""

    def __init__(self, conj1, conj2):
        """Paso de parametros."""
        condicional = []
        conj1neg = []
        for x in range(0, len(conj1)):
            conj1neg.append(not conj1[x])
        for x in range(0, len(conj1neg)):
            condicional.append(conj1neg[x] | conj2[x])
        self.condicional = condicional

    def show(self):
        """Mostrar la interseccion."""
        print(self.condicional)

    def result(self):
        """Regreso el parametro."""
        return(self.condicional)


class Bicondicional(object):
    """Clase Interseccion."""

    def __init__(self, conj1, conj2):
        """Paso de parametros."""
        bicondicional = []
        for x in range(0, len(conj1)):
            if conj1[x] == conj2[x]:
                bicondicional.append(True)
            else:
                bicondicional.append(False)
        self.bicondicional = bicondicional

    def show(self):
        """Mostrar la interseccion."""
        print(self.bicondicional)

    def result(self):
        """Regreso el parametro."""
        return(self.bicondicional)
