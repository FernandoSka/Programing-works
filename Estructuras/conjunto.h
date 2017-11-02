// Conjunto.h
#include <stdio.h>
#include <stdlib.h>

typedef struct conj
{
  int dato;
  struct conj *siguiente;
} Conjunto;

typedef struct identificar
{
  Conjunto *inicio;
  Conjunto *final;
  int tama;
}Lista;

void inicializacion (Lista *lista, int dato){
  Conjunto *nuevo_elemento;
  nuevo_elemento = (Conjunto *) malloc (sizeof (Conjunto));
  nuevo_elemento->dato = dato;
  nuevo_elemento->siguiente = NULL;
  lista->inicio = nuevo_elemento;
  lista->final = nuevo_elemento;
  
  lista->tama = 1;
}

void mostrar(Lista *lista){
     Conjunto *actual;
     actual = lista->inicio;
     printf("%i", actual->dato);
}

/*
int unir (Conjunto, Conjunto, Conjunto *);
//Regresa el entero 3 si el conjunto rebasó el rango o ambos conjuntos estan vacios
void mostrar (Conjunto);
/* Errores, valor regresado:
  > 0, no hay problema
  > 2, error
  > 3, fuera de rango


// Funciones Auxiliares

void mostrar (Conjunto a)
{
  int tam = a.tamanio;
  printf("%i", tam);
  int i;
  for (i = 0; i < tam; i++)
    {
      printf ("| %d |", a.arreglo[i]);
    }
  printf ("\n");
}

int agregar (Conjunto a, int b)
{
  int tam = a.tamanio;
  if (tam + 1 <= 100){
     a.tamanio = a.tamanio + 1;
     *a.arreglo = realloc(*a.arreglo, a.tamanio * sizeof (int));
     a.arreglo[tam] = b;
     }
  
  return 0;
}
*/
