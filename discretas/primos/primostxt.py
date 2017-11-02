def creartxt():
    archi = open('datos.txt', 'w')
    archi.close()


def grabartxt(x):
    archi = open('datos.txt', 'a')
    x = str(x)
    archi.write(x + ' es primo\n')
    archi.close()

creartxt()
num = int(input("escriba hasta que numero "))
for x in range(2, num + 1):
    count = True
    for y in range(2, x):
        mod = x % y
        if mod == 0:
            count = False
    if count:
        grabartxt(x)
