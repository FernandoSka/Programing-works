import math
num = int(input("escriba hasta que numero "))
count = True
var = int(math.sqrt(num)) + 1
for y in range(2, var):
    mod = num % y
    if mod == 0:
        count = False
if count:
    print(num, " es primo")
else:
    print(num, " no es primo")
