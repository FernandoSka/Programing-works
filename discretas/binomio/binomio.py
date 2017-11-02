print("(ax+by)^n")
a = int(input("introduzca a diferente de 0: "))
b = int(input("introduzca b diferente de 0: "))
n = int(input("introduzca n mayor a 0: "))
n2 = 1
for y in range(1, n + 1):
    n2 = n2 * y
if a != 0:
    if b != 0:
        if n > 0:
            for x in range(0, n + 1):
                x2 = 1
                for z in range(1, x + 1):
                    x2 = x2 * z
                try:
                    j = 1
                    for e in range(1, n - x + 1):
                        j = j * (e)
                    c = (n2) / (x2 * (j))
                except ZeroDivisionError:
                    c = 1
                if a > 0:
                    if b > 0:
                        if x > 0:
                            if x == n:
                                print((b), "y^", (n - (n - x)))
                            else:
                                print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                        else:
                            print((a), "x^", (n))
                        if (n - (n - x)) == 4:
                            print("↑↑↑this↑↑↑")
                    else:
                        if x > 0:
                            if x == n:
                                if ((n - (n - x)) % 2) == 0:
                                    print((b * -1), "y^", (n - (n - x)))
                                else:
                                    print((b), "y^", (n - (n - x)))
                            else:
                                if ((n - (n - x)) % 2) == 0:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                                else:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                        else:
                            print((a), "x^", (n))
                        if (n - (n - x)) == 4:
                            print("↑↑↑this↑↑↑")
                else:
                    if b > 0:
                        if x > 0:
                            if x == n:
                                print((b), "y^", (n - (n - x)))
                            else:
                                if ((n - x) % 2) == 0:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                                else:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                        else:
                            if (n % 2) == 0:
                                print((a * -1), "x^", (n))
                            else:
                                print((a), "x^", (n))
                        if (n - (n - x)) == 4:
                            print("↑↑↑this↑↑↑")
                    else:
                        if (n % 2) == 0:
                            if x > 0:
                                if x == n:
                                    print((b * -1), "y^", (n - (n - x)))
                                else:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                            else:
                                print((a * -1), "x^", (n))
                            if (n - (n - x)) == 4:
                                print("↑↑↑this↑↑↑")
                        else:
                            if x > 0:
                                if x == n:
                                    print((b), "y^", (n - (n - x)))
                                else:
                                    print((c * (a**(n - x)) * (b**(n - (n - x)))), "x^", (n - x), "y^", (n - (n - x)))
                            else:
                                print((a), "x^", (n))
                            if (n - (n - x)) == 4:
                                print("↑↑↑this↑↑↑")



holo = (input("ok?"))
