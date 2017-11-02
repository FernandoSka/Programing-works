def factorial(numero):
	if numero<2:
		return(numero)
	return(numero*factorial(numero-1))
print(factorial(3))
"""
def funcion(num,cont):
	cont -= 1
	if cont>=1:
		num *= cont
		funcion(num,cont)
	else:
		print(num)
funcion(5,5)
"""