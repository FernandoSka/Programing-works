import math
numero = int(input("ingrese el numero: "))
num = numero
primos = []
rango = int(num) + 1
z = 0
lista = [[]]
for x in range(2, rango):
    ggg = False
    verdad = False
    count = True
    var = int(math.sqrt(numero)) + 1
    for y in range(2, var):
        mod = numero % y
        if mod == 0:
            count = False
    if count:
        verdad = True
    else:
        verdad = False
    if verdad:
        lista[z].append(numero)
        break
    count = True
    for y in range(2 , x):
        mod = x % y
        if mod == 0:
            count = False
    if count:
        while (numero % x) == 0:
            numero = int(numero / x)
            lista[z].append(x)
            rango = int(rango/x)
            
        z = z + 1
        lista.append([])
        if rango == 1:
            ggg = True
            break;
        
try:
    lista = list(filter(None, lista))
    for i in range(0, len(lista)):
        cuent = 0
        for j in range(0, len(lista[i])):
            cuent = cuent + 1
        print(lista[i][0], " ^ ", cuent)

except Exception:
    raise
