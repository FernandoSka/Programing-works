a = 0
e = 0
i = 0
o = 0
u = 0
text = input("dame un texto plz\n")
for letter in text:
    if letter is "a":
        a += 1
    if letter is "e":
        e += 1
    if letter is "i":
        i += 1
    if letter is "o":
        o += 1
    if letter is "u":
        u += 1
print("That text have", a, "letter a")
print("That text have", e, "letter e")
print("That text have", i, "letter i")
print("That text have", o, "letter o")
print("That text have", u, "letter u")
