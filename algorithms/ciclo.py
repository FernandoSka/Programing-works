"""
variable = int(input("teclee algo numerico"))
maxi = 10
mini = 3
if variable > maxi:
    print("tu variable es mayor a 10")
elif variable < maxi and variable > mini:
    print("tu variable es mayor a 3 y menor a 10")
else:
    print("tu variable es menor a 3") #yolo
"""


arreglo = ["hola", "bebe", "como", "has", "estado", False]
for element in range(0, 6, 2):
    print(arreglo[element])