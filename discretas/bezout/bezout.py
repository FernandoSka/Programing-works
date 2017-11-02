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

def coe3(a, b):
    if (b % a) is 0:
        return 0
    else:
        return(coe2(a, b % a))


def coe4(a, b):
    if (b % a) is 0:
        return 1
    else:
        return(coe1(a, b % a) - (int(b / a) * coe2(a, b % a)))

print("mcd(a,b)")
a = int(input("introduzca a: "))
b = int(input("introduzca b: "))
print("s = ", coe1(a, b))
print("t = ", coe2(a, b))
print("mcd = ", (a * coe1(a, b)) + (b * coe2(a, b)))
print("mcd = ", (coe3(a, b)), (coe4(a, b)))
