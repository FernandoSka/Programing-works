def orden(array, n):
    abc = " abcdefghijklmnñopqrstuvwxyz"
    valor = 0
    counter = 0
    flag = True
    arre = []
    arre2 = []
    x = 0
    for z in range(0, len(array)):
        if abc.index(array[z][n]) > valor:
            valor = abc.index(array[z][n])
    for z in range(0, len(array)):
        if abc.index(array[z][n]) == valor:
            counter += 1
            arre.append(array[z])
    while x < len(array):
        flag = False
        if abc.index(array[x][n]) == valor:
            array.remove(array[x])
            x = 0
            flag = True
        if not flag:
            x += 1
    if len(array) != 0:
        arre2 = orden(array, n)
    if counter <= 1:
        return(arre + arre2)
    else:
        return(orden(arre, n + 1))

abc = " abcdefghijklmnñopqrstuvwxyz"
var = []
var2 = []
var.append(input("introduzca palabra 1 : "))
var.append(input("introduzca palabra 2 : "))
var.append(input("introduzca palabra 3 : "))
var.append(input("introduzca palabra 4 : "))
var.append(input("introduzca palabra 5 : "))
var.append(input("introduzca palabra 6 : "))
var.append(input("introduzca palabra 7 : "))
var.append(input("introduzca palabra 8 : "))
var.append(input("introduzca palabra 9 : "))
var.append(input("introduzca palabra 10 : "))
tokens = [0]
valor = 0
bandera = True
for x in range(0, len(var)):
    tokens.append(len(var[x]))
tokens.remove(0)
tokens = dict.fromkeys(tokens)
tokens = list(tokens.keys())
while bandera:
    bandera = False
    c = 0
    for x in range(0, len(tokens)):
        if x is not len(tokens) - 1:
            if tokens[x] > tokens[x + 1]:
                c = tokens[x + 1]
                tokens[x + 1] = tokens[x]
                tokens[x] = c
                bandera = True
for x in tokens:
    for y in var:
        if x == len(y):
            var2.append(y)
var2.reverse()
longitud = len(var2[0])
for x in range(1, len(var2)):
        if len(var2[0]) - len(var2[x]) > 0:
            for y in range(0, len(var2[0]) - len(var2[x])):
                var2[x] += " "
counts = []
t = 0
for x in range(0, len(var2)):
    counts.append([])
    for y in range(0, len(var2[0])):
        counts[t].append(abc.index(var2[x][y]))
    t += 1
counts.sort()
var = []
letra = ""
for x in range(0, len(var2)):
    letra = ""
    for y in range(0, len(var2[0])):
        letra += abc[counts[x][y]]
    var.append(letra)
var.reverse
print(var)
var = orden(var2, 0)
