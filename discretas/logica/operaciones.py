"""docstring."""

from logica import Union, Condicional, Bicondicional, Interseccion

p = [True, True, True, True, True, True, True, True, False, False, False,
     False, False, False, False, False]
q = [True, True, True, True, False, False, False, False, True, True, True,
     True, False, False, False, False]
r = [True, True, False, False, True, True, False, False, True, True, False,
     False, True, True, False, False]
s = [True, False, True, False, True, False, True, False, True, False, True,
     False, True, False, True, False]
Lp = []
for x in range(0, len(p)):
    Lp.append(not p[x])
rYs = Interseccion(r, s)
settings = []
for x in range(0, 7):
    print("{([1]p [2] q) [3] [ [4]p [5] (rYs) ]} [6] [r->(s[7]p)]")
    print("")
    print("inserte simbolo para [", x + 1, "]")
    opc = True
    while opc:
        if (x == 0) | (x == 3):
            print("1: L")
            print("2: sin cambio")
            sel = int(input(":"))
            if (sel == 1) | (sel == 2):
                settings.append(sel)
                opc = False
            else:
                print("Seleccione una opcion valida")
        elif(x == 1) | (x == 2) | (x == 4) | (x == 5) | (x == 6):
            print("1: Y")
            print("2: O")
            print("3: ->")
            print("4: <->")
            sel = int(input(":"))
            if (sel == 1) | (sel == 2) | (sel == 3) | (sel == 4):
                settings.append(sel)
                opc = False
            else:
                print("Seleccione una opcion valida")

if settings[6] == 1:
    s7p = Interseccion(s, p)
elif settings[6] == 2:
    s7p = Union(s, p)
elif settings[6] == 3:
    s7p = Condicional(s, p)
elif settings[6] == 4:
    s7p = Bicondicional(s, p)

rconds7p = Condicional(r, s7p.result())


if settings[0] == 1:
    if settings[1] == 1:
        p2q = Interseccion(Lp, q)
    elif settings[1] == 2:
        p2q = Union(Lp, q)
    elif settings[1] == 3:
        p2q = Condicional(Lp, q)
    elif settings[1] == 4:
        p2q = Bicondicional(Lp, q)
else:
    if settings[1] == 1:
        p2q = Interseccion(p, q)
    elif settings[1] == 2:
        p2q = Union(p, q)
    elif settings[1] == 3:
        p2q = Condicional(p, q)
    elif settings[1] == 4:
        p2q = Bicondicional(p, q)

if settings[3] == 1:
    if settings[4] == 1:
        p5rys = Interseccion(Lp, rYs.result())
    elif settings[4] == 2:
        p5rys = Union(Lp, rYs.result())
    elif settings[4] == 3:
        p5rys = Condicional(Lp, rYs.result())
    elif settings[4] == 4:
        p5rys = Bicondicional(Lp, rYs.result())
else:
    if settings[4] == 1:
        p5rys = Interseccion(p, rYs.result())
    elif settings[4] == 2:
        p5rys = Union(p, rYs.result())
    elif settings[4] == 3:
        p5rys = Condicional(p, rYs.result())
    elif settings[4] == 4:
        p5rys = Bicondicional(p, rYs.result())

if settings[2] == 1:
    p2q3p5rys = Interseccion(p2q.result(), p5rys.result())
elif settings[2] == 2:
    p2q3p5rys = Union(p2q.result(), p5rys.result())
elif settings[2] == 3:
    p2q3p5rys = Condicional(p2q.result(), p5rys.result())
elif settings[2] == 4:
    p2q3p5rys = Bicondicional(p2q.result(), p5rys.result())

if settings[5] == 1:
    total = Interseccion(p2q3p5rys.result(), rconds7p.result())
elif settings[5] == 2:
    total = Union(p2q3p5rys.result(), rconds7p.result())
elif settings[5] == 3:
    total = Condicional(p2q3p5rys.result(), rconds7p.result())
elif settings[5] == 4:
    total = Bicondicional(p2q3p5rys.result(), rconds7p.result())

Tabla = [[""] * 17] * 11
Tabla[0] = p
Tabla[1] = q
Tabla[2] = r
Tabla[3] = s
Tabla[4] = p2q.result()
Tabla[5] = rYs.result()
Tabla[6] = s7p.result()
Tabla[7] = rconds7p.result()
Tabla[8] = p5rys.result()
Tabla[9] = p2q3p5rys.result()
Tabla[10] = total.result()
AA = ""
BB = ""
CC = ""
DD = ""
EE = ""
FF = ""
for x in range(0, 11):
    if x == 0:
        print("p")
    elif x == 1:
        print("q")
    elif x == 2:
        print("r")
    elif x == 3:
        print("s")
    elif x == 4:
        if settings[0] == 1:
            if settings[1] == 1:
                print("Lp Y q")
                AA = ("(Lp Y q)")
            elif settings[1] == 2:
                print("Lp O q")
                AA = ("(Lp O q)")
            elif settings[1] == 3:
                print("Lp -> q")
                AA = ("(Lp -> q)")
            elif settings[1] == 4:
                print("Lp <-> q")
                AA = ("(Lp <-> q)")
        else:
            if settings[1] == 1:
                print("p Y q")
                AA = ("(p Y q)")
            elif settings[1] == 2:
                print("p O q")
                AA = ("(p O q)")
            elif settings[1] == 3:
                print("p -> q")
                AA = ("(p -> q)")
            elif settings[1] == 4:
                print("p <-> q")
                AA = ("(p <-> q)")
    elif x == 5:
        print("r Y s")
        BB = "(r Y s)"
    elif x == 6:
        if settings[6] == 1:
            print("s Y p")
            CC = "(s Y p)"
        elif settings[6] == 2:
            print("s O p")
            CC = "(s O p)"
        elif settings[6] == 3:
            print("s -> p")
            CC = "(s -> p)"
        elif settings[6] == 4:
            print("s <-> p")
            CC = "(s <-> p)"
    elif x == 7:
        print("(r -> ", CC.replace("'", ""), ")")
        DD = "(r -> " + CC.replace("'", "") + ")"
    elif x == 8:
        if settings[3] == 1:
            if settings[4] == 1:
                print("(p Y ", BB.replace("'", ""), ")")
                EE = "(p Y " + BB.replace("'", "") + ")"
            elif settings[4] == 2:
                print("(p O ", BB.replace("'", ""), ")")
                EE = "(p O " + BB.replace("'", "") + ")"
            elif settings[4] == 3:
                print("(p -> ", BB.replace("'", ""), ")")
                EE = "(p -> " + BB.replace("'", "") + ")"
            elif settings[4] == 4:
                print("(p <-> ", BB.replace("'", "") + ")")
                EE = "(p <-> " + BB.replace("'", "") + ")"
        else:
            if settings[4] == 1:
                print("(p Y ", BB.replace("'", ""), ")")
                EE = "(p Y " + BB.replace("'", "") + ")"
            elif settings[4] == 2:
                print("(p O ", BB.replace("'", ""), ")")
                EE = "(p O " + BB.replace("'", "") + ")"
            elif settings[4] == 3:
                print("(p -> ", BB.replace("'", ""), ")")
                EE = "(p -> " + BB.replace("'", "") + ")"
            elif settings[4] == 4:
                print("(p <-> ", BB.replace("'", ""), ")")
                EE = "(p <-> " + BB.replace("'", "") + ")"
    elif x == 9:
        if settings[2] == 1:
            print("(", AA.replace("'", ""), " Y ", EE, ")")
            FF = ("(" + AA.replace("'", "") + " Y " + EE + ")")
        elif settings[2] == 2:
            print("(", AA.replace("'", ""), " O ", EE, ")")
            FF = ("(" + AA.replace("'", "") + " O " + EE + ")")
        elif settings[2] == 3:
            print("(", AA.replace("'", ""), " -> ", EE, ")")
            FF = ("(" + AA.replace("'", "") + " -> " + EE + ")")
        elif settings[2] == 4:
            print("(", AA.replace("'", ""), " <-> ", EE, ")")
            FF = ("(" + AA.replace("'", "") + " <-> " + EE + ")")
    elif x == 10:
        if settings[5] == 1:
            print(FF, " Y ", DD)
        elif settings[5] == 2:
            print(FF, " O ", DD)
        elif settings[5] == 3:
            print(FF, " -> ", DD)
        elif settings[5] == 4:
            print(FF, " <-> ", DD)

    for y in range(0, 16):
        print("|", (Tabla[x][y]) * (Tabla[x][y]), end=" ")
    print("")
    print("_______________________________________________________________")


var = input("ok?")
