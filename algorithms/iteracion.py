maxi = int(input("teclee un numero "))
mini = int(input("teclee un numero "))
temp = 0
if maxi < mini:
    temp = maxi
    maxi = mini
    mini = temp
counter = 0
while True:
    counter += 1
    if mini != maxi:
        mini += 1
        if mini != maxi:
            maxi = maxi - 1
        else:
            break
    else:
        break
print(counter)