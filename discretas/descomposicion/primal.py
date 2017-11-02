numero = int(input("ingrese el numero: "))
num = numero
primos = []
for x in range(2, int(num) + 1):
    count = True
    for y in range(2 , x):
        mod = x % y
        if mod == 0:
            count = False
    if count:
        primos.append(x)
lista = [[]]
try:
    z = 0
    while z < len(primos):
        if (numero % primos[z]) == 0:
            numero = numero / primos[z]
            lista[z].append(primos[z])
        else:
            z = z + 1
            lista.append([])
    lista = list(filter(None, lista))
    for i in range(0, len(lista)):
        cuent = 0
        for j in range(0, len(lista[i])):
            cuent = cuent + 1
        print(lista[i][0], " ^ ", cuent)

except Exception:
    raise
