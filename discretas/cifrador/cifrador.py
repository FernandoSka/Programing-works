import pickle
import socket

TCP_IP = 'localhost'
TCP_PORT = 8000
BUFFER_SIZE = 1024
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

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
 s=random.randint(1000,9999)
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

#elevacion en binario
res2=[]
expbin=[]
expbin2=bin(e)
num=[]
str(expbin)
i=2
arrfin = []
print("El mensaje cifrado es:   ")
while i<len(expbin2):
    expbin.append(expbin2[i])
    i+=1
#print("El binario es :", expbin)
j=0
while j<len(men):

    num.append(men[j])
    res2.append(num[j])
    i=1
    a =['1']
#para el primer 1 binario

    res=(res2[j]**2)%n
    #print("Elevado al caudrado :",res)
#binarios intermedios
    while i<len(expbin)-1:
    
        if expbin[i] == a[0]:
            #print(res,"*",num[j],"** 2","mod ",n,"    el binario es 1")
            res=((res*num[j])**2)%n
            #print("res vale.    ",res) 
        
        else:
            #print(res," **2","   el binario fue 0")
            res=(res**2)%n
            #print("res vale:     ",res)
        i+=1

#ultimo binario     
    if expbin[len(expbin)-1] is a[0]:
        res=(res*num[j])%n
    j+=1
    print(res,"\n")
    arrfin.append(res)
    

     
        

#imprimir el mensaje cifrado
#print ("El mensaje cifrado es :\n")
#while i<len(men):
#   men_cif.append(((((men[i])**e)%n)%127)) 
#   print (men_cif[i],"\n")
#   i+=1

print("\n \t La calve publica es (", e, ",", n, ")")

arr = [arrfin, [e, n]]
data_string = pickle.dumps(arr)
conn.send(data_string)
conn.close