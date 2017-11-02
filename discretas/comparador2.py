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
cuenta = 0
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
for x in range(1, len(var2)):
        if len(var2[0]) - len(var2[x]) > 0:
            for y in range(0, len(var2[0]) - len(var2[x])):
                var2[x] += " "
var3 = []
counts = []
bandera2 = True
counter = 0
t = 0
if len(var2) != 0:
    for x in range(0, len(var2[0])):
        counts.append([])
        for y in range(0, len(var2)):
            counts[t].append(abc.index(var2[y][x]))
        t += 1
print(counts)