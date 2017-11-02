from random import randint
def h(k, n, arr):
	arr[k % n].append(k)
def h2(k, n, arr):
	pos = k % n
	if k in arr[pos]:
		print("se encontro dato")
	else:
		print("no se encontro nada")

n = int(input("Ingrese cuantos datos: "))
arreglo = []
for x in range(0, n):
	r = randint(0,10000)
	arreglo.append(r)
arr2 = []
for x in range(0, n):
	arr2.append([])
for x in range(0, n):
	h(arreglo[x], n, arr2)
for x in arr2:
	print(x)
n2 = int(input("Ingrese dato a buscar: "))
h2(n2, n, arr2)
"""

hash(arreglo**, k,n){
	int mod = k % n
	arreglo[mod]
	if (arreglo[mod][0]){

	}
	else{

	}

}

int **arreglo, arreglo2[n];
arreglo = (int**)calloc(n, sizeof(int))
for(int i = 0; i<n; i++){
	arreglo[i] = (int*)calloc(n, sizeof(int))
}
for(int i = 0; i<n; i++){
	hash(&arreglo, arreglo[i], n);
}
"""