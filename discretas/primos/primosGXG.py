import math
import threading


def compute(num, var, ini):
    count = True
    for y in range(ini, var):
        if y < 2:
            y = 2
        mod = num % y
        if mod == 0:
            count = False
            break
    if count:
        print("hasta ahora es primo")
    else:
        print("ya no es primo")

num = int(input("escriba hasta que numero "))
var = int(math.sqrt(num)) + 1
varst = str(var)
var2 = str(num)
div = int(var / (len(var2) ** 2))
lista = list()
for x in range(0, len(var2) ** 2):
    fin = div * (x + 1)
    ini = div * x
    if x < (len(varst) - 1):
        hilo = threading.Thread(target=compute, args=(num, fin, ini))
    else:
        hilo = threading.Thread(target=compute, args=(num, var, ini))
    lista.append(hilo)
    hilo.start()
valor = True
for x in range(0, len(lista)):
    cuenta = True