import math
import random
letra = ""
numero = ""
men = []


letra = input("\n\tIntroduce el mensaje a cifrar\n")

for i in range(0, len(letra)):
    print(ord(letra[i]))  # Con esto lo que hago es que muestre el valor ascii de la variable
    letra2 = ord(letra[i])  # Copio el valor a otra variable
    men.append(letra2)

# arreglo con el mensaje en ascii
# generar primos opcion de tenerlos en el arreglo

i = 1
cont = 0
cont2 = 0
primos = []
while cont2 < 2:
    s = random.randint(1000, 10000)
    while True:
        i = 1
        cont = 0
        if s % 2 == 0:
                s += 1
        else:
            while i <= s:
                if s % i == 0:
                    cont += 1
                i += 1
            if cont == 2:
                primos.append(s)
                cont2 = cont2 + 1
                break
            else:
                s = s + 2
# Cifrado
men_cif = []
e = 13
p = primos[0]
q = primos[1]
n = p * q
print("El mensaje cifrado es :\n")
for i in range(0, len(men)):
    men_cif.append((((men[i])**e) % n))
    print(men_cif[i], "\n")

#decifrado
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
c = int(men_cif[0])
array = numeros(n)
n2 = array[0] * array[1]
p = array[0] - 1
q = array[1] - 1
print(p, "   ", q)
b = p * q
a = 13
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
