
print("mcm(a,b)")
a = int(input("introduzca a: "))
b = int(input("introduzca b: "))
valora = a
valorb = b
c = 0
if b > a:  # acomodar a "a" como el valo mas alto
    c = a
    a = b
    b = c
s = a
t = b
d = 0
while True:  # ecuacion
    if a <= 0 or b <= 0:
        break
    c = int(a / b)  # division entera
    d = a - (c * b)
    if d == 0:
        break
    a = b
    b = d
print("mcd(a,b): ", b)
print("mcm(a,b): ", int(valorb * (valora / b)))
