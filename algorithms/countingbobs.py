"""n = 0
cadena = input("ingresa una cadena\n")
for element in range(0,len(cadena)-2):
    if cadena[element:(element+3)]=='bob':
    	n+=1
print (n)
"""
var=input("teclee una cadena")
numbob=var.count("bob")
print ("El numero de bob en la cadena es:")
print (numbob)