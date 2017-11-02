import math
import socket

s = socket.socket()
host = socket.gethostname()
port = 8000


def coe1(a, b):
    if (a % b) is 0:
        return 0
    else:
        return(coe2(b, a % b))


def coe2(a, b):
    if (a % b) is 0:
        return 1
    else:
        return(coe1(b, a % b) - (int(a / b) * coe2(b, a % b)))


def numeros(numero):
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
        for y in range(2, x):
            mod = x % y
            if mod == 0:
                count = False
        if count:
            while (numero % x) == 0:
                numero = int(numero / x)
                lista[z].append(x)
                rango = int(rango / x)
            z = z + 1
            lista.append([])
            if rango == 1:
                break
    try:
        lista = list(filter(None, lista))
        retorno = [lista[0][0], lista[1][0]]
        return(retorno)

    except Exception:
        raise
s.connect((host, port))
arre = s.recv(1024)
s.close()
men_cif = arre[0]
llave = arre[1]
n = llave[1]
c = int(men_cif[0])
array = numeros(n)
n2 = array[0] * array[1]
p = array[0] - 1
q = array[1] - 1
print(p, "   ", q)
b = p * q
a = llave[0]
print("mcd(a,b)")
print("d = ", coe1(a, b))
print("t = ", coe2(a, b))
print("mcd = ", (a * coe1(a, b)) + (b * coe2(a, b)))
print("hola")
x = 0
d = 0
while True:
    d = (1 - (x * b)) / a
    print(d)
    if d % 1 == 0:
        break
    x = x - 1
# #inserte algoritmo del modulo y añadir a la variable dec
print(c, " ** ", d, " % ", n2)
dec = int((c ** d) % n2)

print(chr(dec))
