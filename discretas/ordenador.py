nombre = ["Octavio Ivan Hernandez Salinas", "Pineda Vieyra Itzcoatl Rodrigo",
    "Sergio Gabriel Sanchez Valencia", "Berenice Emazine Maya Calderon",
    "Enrique Ramos Diaz", "Fernando Lopez Perez", "Yael Ali Lima Pascual",
    "Jesus Arturo Araiza Grijalva", "Justo Vizcarra Jaime Alejandro",
    "Diego Garcia Ibanez", "Alejandro Guerrero Aniel",
    "Jose Daniel Perez Zamarripa", "Gibran Armando Ramos Guerrero",
    "Arturo Lara Cazares", "Izaird Alexander Mothelet Delgado",
    "David Josue Rodriguez Chavez"]
edad = [19, 20, 19, 22, 18, 19, 19, 19, 19, 23, 18, 19, 18, 18, 20, 18]
hermanos = [1, 1, 1, 2, 2, 2, 2, 3, 2, 1, 1, 0, 1, 0, 4, 2]
delegacion = ["Azcapotzalco", "Cuahutemoc", "GAM", "GAM", "Tlanepantla", "GAM",
    "Azcapotzalco", "GAM", "GAM", "Cuahutemoc", "GAM", "GAM", "Azcapotzalco",
    "Miguel Hidalgo", "Nezahualcoyotl", "Ecatepec"]
estatura = [1.61, 1.75, 1.69, 1.73, 1.86, 1.73, 1.71, 1.84, 1.72, 1.71, 1.65,
    1.75, 1.78, 1.69, 1.80, 1.79]
peso = [58, 57, 67, 58, 80, 70, 70, 58, 82, 63, 73, 59, 89, 70, 72, 78]
tabla = [nombre, edad, hermanos, delegacion, estatura, peso]
for x in range(0, len(tabla[0])):
    var = ""
    for y in range(0, len(tabla)):
        var += str(tabla[y][x])
        var += " | "
    print(var)
while True:
    print("Seleccione: ")
    print("1) para ordenar x <= y")
    print("2) para ordenar x = y ")
    print("3) para ordenar x coincide en 2 campos con y")
    print("4) para mostrar tabla")
    print("5) para salir")
    var = int(input("teclee una opcion: "))
    print("usted eligio ", var)
    if var is 1:
        print("Seleccione el campo que desee ordenar")
        print("1) para edad")
        print("2) para numero de hermanos")
        print("3) para estatura")
        print("4) para peso")
        print("")
        var = int(input(""))
        if var == 1 or var == 2:
            array = []
            for x in range(0, len(tabla[0])):
                array.append([tabla[var][x], tabla[0][x]])
            array.sort()
            array.reverse()
            for x in array:
                print(x)
        elif var == 3 or var == 4:
            array = []
            for x in range(0, len(tabla[0])):
                array.append([tabla[var + 1][x], tabla[0][x]])
            array.sort()
            array.reverse()
            for x in array:
                print(x)
        else:
            print("opcion invalida")
    elif var is 2:
        print("Seleccione el campo que desee ordenar")
        print("1) para edad")
        print("2) para numero de hermanos")
        print("3) para delegacion")
        print("4) para estatura")
        print("5) para peso")
        print("")
        var = int(input(""))
        if var >= 1 and var <= 5:
            array = []
            for x in range(0, len(tabla[0])):
                array.append([tabla[var][x], tabla[0][x]])
            bandera = True
            bandera2 = True
            counter = 0
            counter2 = 0
            arre = []
            for x in range(0, len(array)):
                for y in range(0, len(array)):
                    if array[x][0] == array[y][0]:
                        arre.append([array[x], array[y]])
            for x in arre:
                print(x)
        else:
            print("opcion invalida")
    elif var is 3:
        array = []
        count = 0
        for x in range(0, len(tabla[0])):
                for y in range(0, len(tabla[0])):
                    count = 0
                    for z in range(0, len(tabla)):
                        if tabla[z][x] is tabla[z][y]:
                            count += 1
                    if count == 2:
                        array.append([tabla[0][x], tabla[0][y]])
        for x in array:
            print(x)

    elif var is 4:
        for x in range(0, len(tabla[0])):
            var = ""
            for y in range(0, len(tabla)):
                var += str(tabla[y][x])
                var += " | "
            print(var)
    elif var is 5:
        break
    else:
        print("teclee una opcion valida")
        print("")
