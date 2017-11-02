class Inventario:
    """Docstring for inventario."""
    idclave = 0

    def __init__(self, titulo, anio, precio, ubicacion, stock, vendidos):
        self._clave = Inventario.idclave
        self._titulo = titulo
        self._anio = anio
        self._precio = precio
        self._ubicacion = ubicacion
        self._stock = stock
        self._vendidos = vendidos
        Inventario.idclave += 1


class Libros(Inventario):
    """Docstring for Libros."""

    cuental = 0

    def __init__(
            self, titulo, anio, precio, ubicacion, stock,
            vendidos, autor, editorial, paginas, pais, edicion,
            ISBN, tiraje):
        fo = open("CLibros.txt", "a+")

        super(Libros, self).__init__(
            titulo, anio, precio, ubicacion, stock, vendidos)
        self._autor = autor
        self._editorial = editorial
        self._paginas = paginas
        self._pais = pais
        self._edicion = edicion
        self._ISBN = ISBN
        self._tiraje = tiraje
        fo.write(str(self._clave)+"/"+str(titulo)+"/"+ str(anio)+"/"+ str(precio)+"/"+ str(ubicacion)+"/"+ str(stock)+"/"+str(vendidos)+"/"+ str(autor)+"/"+ str(editorial)+"/"+ str(paginas)+"/"+ str(pais)+"/"+ str(edicion)+"/"+str(ISBN)+"/"+ str(tiraje)+"\n")
        Libros.cuental += 1
        fo.close()


class Peliculas(Inventario):
    """docstring for Peliculas"""

    cuentap = 0
    def __init__(
            self, titulo, anio, precio, ubicacion, stock,
            vendidos, director, actorp, ISBN, duracion, formato,
            genero, audioO, productora, subtitulos):
        fo = open("CPeliculas.txt", "a+")
        super(Peliculas, self).__init__(
            titulo, anio, precio, ubicacion, stock, vendidos)
        self._director = director
        self._actorp = actorp
        self._ISBN = ISBN
        self._duracion = duracion
        self._formato = formato
        self._genero = genero
        self._audioO = audioO
        self._productora = productora
        self._subtitulos = subtitulos
        fo.write(str(self._clave)+"/" +str(titulo) + "/" +str(anio) + "/" +str(precio) + "/" +str(ubicacion) + "/" +str(stock) + "/" +str(vendidos) + "/" +str(director) + "/" +str(actorp) + "/" +str(ISBN) + "/" +str(duracion) + "/" +str(formato) + "/" +str(genero) + "/" +str(audioO) + "/" +str(productora) + "/" +str(subtitulos)+"\n")
        Peliculas.cuentap += 1
        fo.close()


class Musica(Inventario):
    """docstring for Musica"""

    cuentam = 0

    def __init__(
            self, titulo, anio, precio, ubicacion, stock,
            vendidos, interprete, formato, pistas, productor,
            disquera, pais, genero):
        fo = open("CMusica.txt", "a+")
        super(Musica, self).__init__(
            titulo, anio, precio, ubicacion, stock, vendidos)
        self._interprete = interprete
        self._formato = formato
        self._pistas = pistas
        self._productor = productor
        self._disquera = disquera
        self._pais = pais
        self._genero = genero
        Musica.cuentam += 1
        fo.write(str(self._clave) + "/" + str(titulo) + "/" + str(anio) + "/" + str(precio) + "/" + str(ubicacion) + "/" + str(stock) + "/" + str(vendidos) + "/" + str(interprete) + "/" + str(formato) + "/" + str(pistas) + "/" + str(productor) + "/" + str(disquera) + "/" + str(pais) + "/" + str(genero)+"\n")
        fo.close()


class Reporte(Libros, Peliculas, Musica):
    """docstring for Reporte"""

    def __init__(self):
        fo = open("CLibros.txt", "w")
        fo.close()
        fo = open("CPeliculas.txt", "w")
        fo.close()
        fo = open("CMusica.txt", "w")
        fo.close()

    def altas(self, tipo):
        if tipo is "NL":
            try:
                autor = input("ingrese el autor: ")
                editorial = input("ingrese la editorial: ")
                paginas = int(input("ingrese el numero de paginas: "))
                pais = input("ingrese el pais: ")
                edicion = input("ingrese la edicion: : ")
                ISBN = input("ingrese el ISBN: ")
                tiraje = int(input("ingrese el tiraje: "))
                titulo = input("ingrese el titulo: ")
                anio = int(input("ingrese el anio: "))
                precio = float(input("ingrese el precio: "))
                ubicacion = input("ingrese la ubicacion: ")
                stock = int(input("ingrese el stock: "))
                vendidos = 0
                Libros(
                    titulo, anio, precio, ubicacion, stock, vendidos,
                    autor, editorial, paginas, pais, edicion, ISBN, tiraje)
            except Exception:
                print("por favor teclee un dato adecuado")
        elif tipo is "NP":
            try:
                director = input("ingrese el director: ")
                actorp = input("ingrese el actor principal: ")
                ISBN = input("ingrese el ISBN: ")
                duracion = int(input("ingrese la duracion: "))
                formato = input("ingrese el formato: ")
                genero = input("ingrese el genero: ")
                audioO = input("ingrese el audio original: ")
                productora = input("ingrese la productora: ")
                subtitulos = input("ingrese los subtitulos: ")
                titulo = input("ingrese el titulo: ")
                anio = int(input("ingrese el anio: "))
                precio = float(input("ingrese el precio: "))
                ubicacion = input("ingrese la ubicacion: ")
                stock = str(input("ingrese el stock: "))
                vendidos = 0
                Peliculas(
                    titulo, anio, precio, ubicacion, stock,
                    vendidos, director, actorp, ISBN, duracion, formato,
                    genero, audioO, productora, subtitulos)
            except Exception:
                print("por favor teclee un dato adecuado")
        elif tipo is "NM":
            try:
                
                interprete = input("ingrese el interprete: ")
                formato = input("ingrese el formato: ")
                pistas = int(input("ingrese numero de pistas: "))
                productor = input("ingrese el productor: ")
                disquera = input("ingrese la disquera: ")
                pais = input("ingrese el pais: ")
                genero = input("ingrese el genero: ")
                titulo = input("ingrese el titulo: ")
                anio = int(input("ingrese el anio: "))
                precio = float(input("ingrese el precio: "))
                ubicacion = input("ingrese la ubicacion: ")
                stock = int(input("ingrese el stock: "))
                vendidos = 0
                Musica(
                    titulo, anio, precio, ubicacion, stock,
                    vendidos, interprete, formato, pistas, productor,
                    disquera, pais, genero)
            except Exception:
                print("por favor teclee un dato adecuado")

    def imprimir(self, clave):
        if clave < self.idclave:
            arreglo = buscar(clave, "CLibros.txt")
            if len(arreglo) is 0:
                arreglo = buscar(clave, "CPeliculas.txt")
                if len(arreglo) is 0:
                    arreglo = buscar(clave, "CMusica.txt")
                    if len(arreglo) is 0:
                        print("producto inexistente")
                    else:
                        arreglo[0] = "Clave: " + arreglo[0]
                        arreglo[1] = "Titulo: " + arreglo[1]
                        arreglo[2] = "Anio: " + arreglo[2]
                        arreglo[3] = "Ubicacion: " + arreglo[3]
                        arreglo[4] = "Stock: " + arreglo[4]
                        arreglo[5] = "Vendidos: " + arreglo[5]
                        arreglo[6] = "Interprete: " + arreglo[6]
                        arreglo[7] = "Formato: " + arreglo[7]
                        arreglo[8] = "Pistas: " + arreglo[8]
                        arreglo[9] = "Productor: " + arreglo[9]
                        arreglo[10] = "Disquera: " + arreglo[10]
                        arreglo[11] = "Pais: " + arreglo[11]
                        arreglo[12] = "Genero: " + arreglo[12]
                        for i in arreglo:
                            print(i)
                else:
                    arreglo[0] = "Clave: " + arreglo[0]
                    arreglo[1] = "Titulo: " + arreglo[1]
                    arreglo[2] = "Anio: " + arreglo[2]
                    arreglo[3] = "Ubicacion: " + arreglo[3]
                    arreglo[4] = "Stock: " + arreglo[4]
                    arreglo[5] = "Vendidos: " + arreglo[5]
                    arreglo[6] = "Director: " + arreglo[6]
                    arreglo[7] = "Actor principal: " + arreglo[7]
                    arreglo[8] = "ISBN: " + arreglo[8]
                    arreglo[9] = "Duracion: " + arreglo[9]
                    arreglo[10] = "Formato: " + arreglo[10]
                    arreglo[11] = "Genero: " + arreglo[11]
                    arreglo[12] = "Audio original: " + arreglo[12]
                    arreglo[13] = "Productora: " + arreglo[13]
                    arreglo[14] = "Subtitulos: " + arreglo[14]
                    for i in arreglo:
                        print(i)
            else:
                arreglo[0] = "Clave: " + arreglo[0]
                arreglo[1] = "Titulo: " + arreglo[1]
                arreglo[2] = "Anio: " + arreglo[2]
                arreglo[3] = "Ubicacion: " + arreglo[3]
                arreglo[4] = "Stock: " + arreglo[4]
                arreglo[5] = "Vendidos: " + arreglo[5]
                arreglo[6] = "Autor: " + arreglo[6]
                arreglo[7] = "Editorial: " + arreglo[7]
                arreglo[8] = "Paginas: " + arreglo[8]
                arreglo[9] = "Pais: " + arreglo[9]
                arreglo[10] = "Edicion: " + arreglo[10]
                arreglo[11] = "ISBN: " + arreglo[11]
                arreglo[12] = "Tiraje: " + arreglo[12]
                for i in arreglo:
                    print(i)
        else:
            print("producto inexistente")

    def ventas(self, clave):
        base = ""
        baseint = 0
        if clave < self.idclave:
            arreglo = buscar2(clave, "CLibros.txt")
            base = "CLibros.txt"
            baseint = 1
            if len(arreglo) is 0:
                arreglo = buscar2(clave, "CPeliculas.txt")
                base = "CPeliculas.txt"
                baseint = 2
                if len(arreglo) is 0:
                    arreglo = buscar2(clave, "CMusica.txt")
                    base = "CMusica.txt"
                    baseint = 3
                    if len(arreglo) is 0 and clave is not -1:
                        print("producto inexistente")
            elemento = []
            producto = []
            concat = ""
            ban = False
            pos = 0
            for i in arreglo:
                if i is "\n":
                    producto.append(elemento)
                    elemento = []
                else:
                    if i is not "/":
                        concat += i
                    else:
                        elemento.append(concat)
                        concat = ""
            count = 0
            for i in producto:
                i[0] = int(i[0])
                if i[0] is clave:
                    if int(i[5]) > 0:
                        pos = count
                        i[5] = int(i[5]) - 1
                        i[6] = int(i[6]) + 1
                        ban = True
                count += 1
            if ban:
                fo = open(base, "w")
                cadena = ""
                for i in producto:
                    for j in i:
                        cadena += str(j)
                        cadena += "/"
                    cadena += "\n"
                fo.write(cadena)
                fo.close()
                return([producto[pos], baseint])
            else:
                print("producto agotado")
                return([])
        else:
            print("producto inexistente")
            return([])

    def rlibros(self):
        fo = open("CLibros.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        total = 0
        ganancia = 0.0
        for i in producto:
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])
        print("Se vendieron ", total, " libros")
        print("Se ganaron $", ganancia, " pesos")

    def rpeliculas(self):
        fo = open("CPeliculas.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        total = 0
        ganancia = 0.0
        for i in producto:
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])
        print("Se vendieron ", total, " peliculas")
        print("Se ganaron $", ganancia, " pesos")

    def rmusica(self):
        fo = open("CMusica.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        total = 0
        ganancia = 0.0
        for i in producto:
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])
        print("Se vendieron ", total, " discos")
        print("Se ganaron $", ganancia, " pesos")

    def rgeneral(self):
        total = 0
        totlib = 0
        totpel = 0
        totmus = 0
        ganancia = 0.0
        fo = open("CLibros.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        for i in producto:
            totlib += int(i[6])
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])

        fo = open("CPeliculas.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        for i in producto:
            totpel += int(i[6])
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])

        fo = open("CMusica.txt", "r")
        concat = ""
        while True:
            caracter = fo.read(1)
            concat += caracter
            if not caracter:
                break
        fo.close()
        elemento = []
        producto = []
        concat2 = ""
        for i in concat:
            if i is "\n":
                producto.append(elemento)
                elemento = []
            else:
                if i is not "/":
                    concat2 += i
                else:
                    elemento.append(concat2)
                    concat2 = ""
        for i in producto:
            totmus += int(i[6])
            total += int(i[6])
            ganancia += float(i[3]) * int(i[6])
        print("Se vendieron ", total, " productos")
        print("Se ganaron $", ganancia, " pesos")
        pila = total / 10
        try:
            barratotal = int(total // pila)
        except Exception:
            barratotal = 0
        try:
            barralibro = int(totlib // pila)
        except Exception:
            barralibro = 0
        try:
            barrapelicula = int(totpel // pila)
        except Exception:
            barrapelicula = 0
        try:
            barramusica = int(totmus // pila)
        except Exception:
            barramusica = 0
        grafica = [[]]

        grafica[0].append("")
        grafica[0].append(" ")
        longitud = 0
        for i in range(1, 12):
            if(len(str(i * pila)) > longitud):
                longitud = len(str(i * pila))
        for i in range(1, 12):
            cade = str(i * pila)
            if(len(str(i * pila)) < longitud):
                for i in range(0, longitud - len(str(i * pila))):
                    cade += " "

            grafica[0].append(cade)

        grafica[0].append("")
        cadenaprimer = ""
        for i in range(0, longitud):
            cadenaprimer += " "
        grafica[0][0] = cadenaprimer
        grafica[0][1] = cadenaprimer

        grafica[0].reverse()

        grafica.append([])
        grafica[1].append(" ")
        for i in range(0, 11):
            grafica[1].append("|")
        grafica[1].append(" ")
        grafica[1].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[2].append(" ")
        grafica[2].append("_")
        grafica[2].append(" ")

        grafica.append([])
        grafica[3].append("T")
        grafica[3].append("_")
        for i in range(0, barratotal):
            grafica[3].append("H")
        for i in range(0, 12 - barratotal):
            grafica[3].append(" ")
        grafica[3].reverse()

        grafica.append([])
        for i in range(0, 12):
            grafica[4].append(" ")
        grafica[4].append("_")
        grafica[4].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[5].append(" ")
        grafica[5].append("_")
        grafica[5].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[6].append(" ")
        grafica[6].append("_")
        grafica[6].append(" ")

        grafica.append([])
        grafica[7].append("L")
        grafica[7].append("_")
        for i in range(0, barralibro):
            grafica[7].append("H")
        for i in range(0, 12 - barralibro):
            grafica[7].append(" ")
        grafica[7].reverse()

        grafica.append([])
        for i in range(0, 12):
            grafica[8].append(" ")
        grafica[8].append("_")
        grafica[8].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[9].append(" ")
        grafica[9].append("_")
        grafica[9].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[10].append(" ")
        grafica[10].append("_")
        grafica[10].append(" ")

        grafica.append([])
        grafica[11].append("P")
        grafica[11].append("_")
        for i in range(0, barrapelicula):
            grafica[11].append("H")
        for i in range(0, 12 - barrapelicula):
            grafica[11].append(" ")
        grafica[11].reverse()

        grafica.append([])
        for i in range(0, 12):
            grafica[12].append(" ")
        grafica[12].append("_")
        grafica[12].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[13].append(" ")
        grafica[13].append("_")
        grafica[13].append(" ")

        grafica.append([])
        for i in range(0, 12):
            grafica[14].append(" ")
        grafica[14].append("_")
        grafica[14].append(" ")

        grafica.append([])
        grafica[15].append("M")
        grafica[15].append("_")
        for i in range(0, barramusica):
            grafica[15].append("H")
        for i in range(0, 12 - barramusica):
            grafica[15].append(" ")
        grafica[15].reverse()

        grafica.append([])
        for i in range(0, 12):
            grafica[16].append(" ")
        grafica[16].append("_")
        grafica[16].append(" ")

        for i in range(0, 14):
            cadgraf = ""
            for j in range(0, 17):
                cadgraf += grafica[j][i]
            print(cadgraf)
        print("")
        print("T = Total")
        print("L = Libros")
        print("P = Peliculas")
        print("M = Musica")



def buscar(clave, archivo):
    fo = open(archivo, "r")
    concat = ""
    arreglo = []
    while True:
        caracter = fo.read(1)
        if not caracter:
            break
        if caracter is not "/":
            concat += caracter
        else:
            if int(concat) is clave:
                arreglo.append(concat)
                concat = ""
                while True:
                    caracter = fo.read(1)
                    if caracter is "\n":
                        break
                    elif caracter is not "/":
                        concat += caracter
                    else:
                        arreglo.append(concat)
                        concat = ""
                return(arreglo)
            else:
                while True:
                    caracter = fo.read(1)
                    if caracter is "\n":
                        break
                    concat = ""
    fo.close()
    return([])


def buscar2(clave, archivo):
    fo = open(archivo, "r")
    concat = ""
    while True:
        caracter = fo.read(1)
        if not caracter:
            break
        if caracter is not "/":
            concat += caracter
        else:
            if int(concat) is clave:
                fo.close()
                fo = open(archivo, "r")
                concat = ""
                while True:
                    caracter = fo.read(1)
                    concat += caracter
                    if not caracter:
                        break

                return(concat)
            else:
                while True:
                    caracter = fo.read(1)
                    if caracter is "\n":
                        break
                    concat = ""
    fo.close()
    return("")
    