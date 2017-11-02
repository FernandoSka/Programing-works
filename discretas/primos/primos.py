num = int(input("escriba hasta que numero "))
for x in range(2, num+1):
    count = True
    for y in range(2,x):
        mod = x%y
        if mod == 0:
            count = False
    if count:
        print(x, " es primo")