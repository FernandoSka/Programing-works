#decifrar
import socket
import pickle
import math
HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(4096)
data_arr = pickle.loads(data)
s.close
men_cif = data_arr[0]
print(men_cif)
clav = data_arr[1]
e = clav[0]
n = clav[1]
nn=n
#introduccion del mensaje cifrado
men_cif=[]
let=1
#descomponer en primos
s=n

i=2
cont=0
while i<(n+1):
    if n%i == 0:
        n=n/i
        cont+=1
        i=1
    i+=1
        
n=s
z=1
v=[]
j=0
i=2
while i<n+1:
    if n%i==0:
        n=n/i
        v.append(i)
        j=j+1
        i=1
    i+=1
#print(v)
prim=[]
exp=[]
i=0
while i<len(v):
    
    veces=v.count(v[i])
    if v[i-1]!=v[i]:
        exp.append(veces)
        
    i+=1        
i=0
j=0     
while i<len(v):
    if v[i-1]!=v[i]:
        #print(v[i],"^",exp[j],"=\t")
        #print(v[i]**exp[j])
        prim.append(v[i]**exp[j])
        j+=1
    i+=1
i=0 
while i<len(prim):
    #print(prim[i])
    i+=1

p=prim[0]
q=prim[1]
fi=(p-1)*(q-1)
a=e
b=fi
#print("e y fi son :")
x=0
d=0
#ecuacion de bezout entre e y fi
while True:
    d = (1 - (x * b)) / a
    #print(d)
    if d % 1 == 0:
        break
    x = x - 1

h=math.floor(d)
d=h
#decifrado

#men = men_cif
i=0
n=nn
#elevacion en binario
res2=[]
expbin=[]
expbin2=bin(d)
num=[]
str(expbin)
i=2

print("El mensaje decifrado es:   ")
while i<len(expbin2):
    expbin.append(expbin2[i])
    i+=1
#print("El binario es :", expbin)
j=0

for j in range(0,len(men_cif)):

    num.append(men_cif[j])
    res2.append(men_cif[j])
    i=1
    a =['1']
    
#para el primer 1 binario

    res=(res2[j]**2)%n
    #print("El numero es  ",num[j],"  y n es    ",n)
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
    #pasar ascii a valor letra
    res22=chr(res)
    print(res)
    print(res22)
