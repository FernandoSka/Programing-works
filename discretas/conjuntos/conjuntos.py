U1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
count = True
count2 = False
A = []
B = []
C = []
D = []
print("inserte cualquiera de los siguientes valores validos a los subconjuntos",U1)
print("anada valores a subconjunto A")
while count:
    alen = len(A)
    value = input("inserte valores: ")
    for x in range(0, len(U1)):
        if U1[x] == value:
            for y in range(0, len(A)):
                if not A[y] == value:
                    count2 = False
                else:
                    count2 = True
            if not count2:
                A.append(value)
            else:
                print("ese valor ya existe")
    if alen == len(A):
        print("introduzca un valor valido")
    opc = input("desea anadir otro valor? (y/n)")
    if not opc == "y":
        count = False
print(A)
count = True
count2 = False

print("inserte cualquiera de los siguientes valores validos a los subconjuntos",U1)
print("anada valores a subconjunto B")
while count:
    blen = len(B)
    value = input("inserte valores: ")
    for x in range(0, len(U1)):
        if U1[x] == value:
            for y in range(0, len(B)):
                if not B[y] == value:
                    count2 = False
                else:
                    count2 = True
            if not count2:
                B.append(value)
            else:
                print("ese valor ya existe")
    if blen == len(B):
        print("introduzca un valor valido")
    opc = input("desea anadir otro valor? (y/n)")
    if not opc == "y":
        count = False
print(B)
count = True
count2 = False

print("inserte cualquiera de los siguientes valores validos a los subconjuntos",U1)
print("anada valores a subconjunto C")
while count:
    clen = len(C)
    value = input("inserte valores: ")
    for x in range(0, len(U1)):
        if U1[x] == value:
            for y in range(0, len(C)):
                if not C[y] == value:
                    count2 = False
                else:
                    count2 = True
            if not count2:
                C.append(value)
            else:
                print("ese valor ya existe")
    if clen == len(C):
        print("introduzca un valor valido")
    opc = input("desea anadir otro valor? (y/n)")
    if not opc == "y":
        count = False
print(C)
count = True
count2 = False

print("inserte cualquiera de los siguientes valores validos a los subconjuntos",U1)
print("anada valores a subconjunto D")
while count:
    dlen = len(D)
    value = input("inserte valores: ")
    for x in range(0, len(U1)):
        if U1[x] == value:
            for y in range(0, len(D)):
                if not D[y] == value:
                    count2 = False
                else:
                    count2 = True
            if not count2:
                D.append(value)
            else:
                print("ese valor ya existe")
    if dlen == len(D):
        print("introduzca un valor valido")
    opc = input("desea anadir otro valor? (y/n)")
    if not opc == "y":
        count = False
print(D)
count = True
count2 = False

print("1.- (A* ∩ B*) U(C* ∩ D*)")
Acomp = []
Bcomp = []
Ccomp = []
Dcomp = []
AB = []
CD = []
tot1 = []
count3 = False
for x in range(0, len(U1)):
    Acomp.append(U1[x])
    Bcomp.append(U1[x])
    Ccomp.append(U1[x])
    Dcomp.append(U1[x])
for x in range(0, len(A)):
    Acomp.remove(A[x])
for x in range(0, len(B)):
    Bcomp.remove(B[x])
for x in range(0, len(C)):
    Ccomp.remove(C[x])
for x in range(0, len(D)):
    Dcomp.remove(D[x])
for x in range(0, len(Bcomp)):
    for y in range(0, len(Acomp)):
        if Acomp[y] == Bcomp[x]:
            count3 = True
    if count3:
        AB.append(Bcomp[x])
    count3 = False
for x in range(0, len(Ccomp)):
    for y in range(0, len(Dcomp)):
        if Dcomp[y] == Ccomp[x]:
            count3 = True
    if count3:
        CD.append(Ccomp[x])
    count3 = False
for x in range(0, len(AB)):
    tot1.append(AB[x])
for x in range(0, len(CD)):
    for y in range(0, len(tot1)):
        if tot1[y] == CD[x]:
            count3 = True
    if not count3:
        tot1.append(CD[x])
    count3 = False
print(tot1)
print("2.- (A U B) ∩ (C ∩ D)*")
AUB = []
tot2 = []
CinD = []
CDcomp = []
for x in range(0, len(A)):
    AUB.append(A[x])
for x in range(0, len(B)):
    for y in range(0, len(AUB)):
        if AUB[y] == B[x]:
            count3 = True
    if not count3:
        AUB.append(B[x])
    count3 = False
for x in range(0, len(C)):
    for y in range(0, len(D)):
        if D[y] == C[x]:
            count3 = True
    if count3:
        CinD.append(C[x])
    count3 = False
for x in range(0, len(U1)):
    CDcomp.append(U1[x])
for x in range(0, len(CinD)):
    CDcomp.remove(CinD[x])
for x in range(0, len(AUB)):
    for y in range(0, len(CDcomp)):
        if CDcomp[y] == AUB[x]:
            count3 = True
    if count3:
        tot2.append(AUB[x])
    count3 = False
print(tot2)
print("3.- (A ∩ C) U (A ∩ B) U (A ∩ D)")
AinB = []
AinC = []
AinD = []
UU1 = []
tot3 = []
for x in range(0, len(A)):
    for y in range(0, len(B)):
        if B[y] == A[x]:
            count3 = True
    if count3:
        AinB.append(A[x])
    count3 = False
for x in range(0, len(A)):
    for y in range(0, len(C)):
        if C[y] == A[x]:
            count3 = True
    if count3:
        AinC.append(A[x])
    count3 = False
for x in range(0, len(A)):
    for y in range(0, len(D)):
        if D[y] == A[x]:
            count3 = True
    if count3:
        AinD.append(A[x])
    count3 = False
for x in range(0, len(AinB)):
    UU1.append(AinB[x])
for x in range(0, len(AinC)):
    for y in range(0, len(UU1)):
        if UU1[y] == AinC[x]:
            count3 = True
    if not count3:
        UU1.append(AinC[x])
    count3 = False
for x in range(0, len(UU1)):
    tot3.append(UU1[x])
for x in range(0, len(AinD)):
    for y in range(0, len(tot3)):
        if tot3[y] == AinD[x]:
            count3 = True
    if not count3:
        tot3.append(AinD[x])
    count3 = False
print(tot3)
var = input("ok?")
