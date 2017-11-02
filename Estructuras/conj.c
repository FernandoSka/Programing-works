#include "Conjunto.h"

int
unir (Conjunto A, Conjunto B, Conjunto * Resultado)
{
  int tam = 0, i = 0, j = 0;

  tam = A.tamanio + B.tamanio;

  if (tam > 100 || (A.tamanio == 0 && B.tamanio == 0 ))
    {
      Resultado->arreglo = NULL;
      Resultado->tamanio = 0;
      return 3;
    }
  else
    {
      for (i = 0; i < tam; i++)
	{
	  if (i < A.tamanio)
	    {
	      *(Resultado->arreglo + i) = *(A.arreglo + i);
	    }
	  else
	    {
	      *(Resultado->arreglo + i) = *(B.arreglo + j);
	      j++;
	    }
	}
      Resultado->tamanio = EliminarRepetidos (Resultado->arreglo, tam);
    }

  return 0;

}

void
mostrar (Conjunto a)
{
  int tam = a.tamanio;
  int i;
  for (i = 0; i < tam; i++)
    {
      printf ("| %d |", a.arreglo[i]);
    }
  printf ("\n");
}

int
agregar (Conjunto * a, int b)
{
  int i;

  if (!(a->tamanio) || !(a->arreglo))
    {
      return 3;
    }
  if ((a->tamanio + 1) > 100)
    return 3;

  for (i = 0; i < a->tamanio; i++)
    {
      if (a->arreglo[i] == b)
	return 2;
    }
  int *nuevo = (int *) malloc (sizeof (int) * (a->tamanio + 1));
  copiarArreglo (nuevo, a->arreglo, (a->tamanio + 1));
  nuevo[a->tamanio] = b;

  a->arreglo = nuevo;
  a->tamanio = a->tamanio + 1;

  return 0;
}

void
copiarArreglo (int *des, int *org, int n)
{
  int i = 0;

  memset (des, 0, (n * sizeof (int)));

  for (i = 0; i < n; i++)
    {
      *(des + i) = *(org + i);
    }
}

int
EliminarRepetidos (int *C, int n)
{
  int i = 0, j = 0, k = 0, cont = 0, num = 0;
  int *tmp = NULL, *aux = NULL;

  tmp = (int *) malloc (n * sizeof (int));
  aux = (int *) malloc (n * sizeof (int));
  memcpy (aux, C, n);

  for (i = 0; i < n; i++)
    {
      cont = 0;
      *(aux + i) = num = *(C + i);
      for (j = 0; j < i; j++)
	{
	  if (*(aux + j) == num)
	    {
	      cont = 1;
	    }
	}
      if (cont == 0)
	{
	  *(tmp + k) = num;
	  k++;
	}
    }

  copiarArreglo (C, tmp, k);
  free (tmp);
  return k;
}
