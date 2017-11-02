
letra = ""
numero = ""
 
men =[]


letra=input("\n\tIntroduce el mensaje a cifrar\n")

i=0
while i< len(letra):
	ord(letra[i]) #Con esto lo que hago es que muestre el valor ascii de la variable
	letra2 = ord(letra[i]) #Copio el valor a otra variable
	men.append(letra2)
	i=i+1    

#arreglo con el mensaje en ascii
i=0
while i<len(men):
	i=i+1

#generar primos opcion de tenerlos en el arreglo 

i=1
cont=0
cont2=0
primos=[] 
import random
while cont2<2:
 s=random.randint(1000,100000)
 while 1<2: 
  i=1
  cont=0	  
  if s%2==0:
    s+=1
    
  else: 
   
   while i <= s:
    if s%i==0:
     cont+=1
    i+=1
	 
   if cont==2:
	  
    primos.append(s) 
    cont2=cont2+1
    break
   else :    
    s=s+2


i=0	 
while i < len(primos):
	p=primos[i]
	i+=1


#cifrado

men_cif=[]
e=13
p=primos[0]
q=primos[1]
n=p*q
i=0
print ("El mensaje cifrado es :\n")
while i<len(men):
	men_cif.append((((men[i])**e)%n)) 
	print (men_cif[i],"\n")
	i+=1



	
 
 
 
  
