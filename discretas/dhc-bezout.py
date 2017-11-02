

a=int(input("Valor de a"))


b=int(input("Valor de b"))

x=0
y=0
bandera=0
while bandera<1:
	
	while y<99999:
		if ((a*x)-(b*y)) is 1:
			print("La ecuacion de Bezout es :",a,"(",x,")","+",b,"(-",y,")")
			bandera+=1
			break
		else:
			y+=1
	x+=1
	y=0
	
