num = int(input("escriba hasta que numero "))
count = True
for y in range(2,num):
    mod = num%y
    if mod == 0:
        count = False
if count:
    print(num, " es primo")
else:
    print(num, " no es primo")