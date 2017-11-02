import math
import random
import socket
letra = ""
numero = ""
men = []
s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host, port))
s.listen(5)
c, addr = s.accept()

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
envio = [men_cif, [e, n]]
c.send(bytes(envio))
c.close()