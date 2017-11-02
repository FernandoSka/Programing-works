print("mapas de Karnaugh")
p = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
q = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
r = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
s = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
pq = ["00", "01", "10", "11"]
rs = ["00", "01", "10", "11"]
pqrs = []
count = []
for x in range(0, len(p)):
    pqrs.append(0)
    while True:
        print("ingrese le valor para", "p|", p[x], "| ", "q|", q[x], "| ",
              "r|", r[x], "| ", "s|", s[x], "| ",)
        pqrs[x] = int(input(": "))
        if pqrs[x] is 1 or pqrs[x] is 0:
            break
        else:
            "ingrese 1 o 0"
cadena = ""
for x in range(0, len(pqrs)):
    if pqrs[x] is 1:
        if p[x] is 1:
            cadena = "1"
        else:
            cadena = "5"
        if q[x] is 1:
            cadena += "2"
        else:
            cadena += "6"
        if r[x] is 1:
            cadena += "3"
        else:
            cadena += "7"
        if s[x] is 1:
            cadena += "4"
        else:
            cadena += "8"
        count.append(cadena)
vari = 0
var2 = 0
orden = [[0, 0, 0, 0], [0, 0, 0, 0]]
arrayval = [[1, 2, 3, 4], [5, 6, 7, 8]]
for y in range(0, 4):
    vari = 0
    var2 = 0
    for x in range(0, len(count)):
        if count[x][y] == str(arrayval[0][y]):
            vari += 1
        elif count[x][y] == str(arrayval[1][y]):
            var2 += 1
    orden[0][y] = vari
    orden[1][y] = var2
counter2 = 0
for x in range(0, 4):
    if orden[0][x] >= orden[1][x]:
        if orden[0][x] > counter2:
            counter2 = orden[0][x]
    elif orden[1][x] >= orden[0][x]:
        if orden[1][x] > counter2:
            counter2 = orden[1][x]
count2 = []
for x in range(0, 4):
    if orden[0][x] == counter2:
        for y in range(0, len(count)):
            if count[y][x] == str(arrayval[0][x]):
                count2.append(count[y])
        for y in range(0, len(count)):
            if count[y][x] == str(arrayval[1][x]):
                count2.append(count[y])
        break
    if orden[1][x] == counter2:
        for y in range(0, len(count)):
            if count[y][x] == str(arrayval[1][x]):
                count2.append(count[y])
        for y in range(0, len(count)):
            if count[y][x] == str(arrayval[0][x]):
                count2.append(count[y])
        break
print(count2)
Bandera = True
while Bandera:
    counter = 0
    Bandera = False
    cade = ""
    for x in range(0, len(count)):
        for y in range(0, len(count)):
            counter = 0
            for z in range(0, 4):
                if x != y:
                    if count[x][z] == count[y][z]:
                        counter += 1
            print(counter)
            if counter == 3:
                for z in range(0, 4):
                    if count[x][z] == count[y][z]:
                        cade += count[x][z]
                    else:
                        cade += "0"
                count.pop(x)
                count.pop(y - 1)
                count.append(cade)
                Bandera = True
            if Bandera:
                break
        if Bandera:
            break

cadena = ""
for x in range(0, len(count)):
    if x != len(count) - 1:
        cadena += count[x] + " + "
    else:
        cadena += count[x]
print(cadena)
