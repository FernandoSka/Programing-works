#include "Conjunto.h"

int
main (void)
{
  int i = 0;

  Conjunto A;
  Conjunto B;
  Conjunto C;

  A.arreglo = (int *) malloc (10 * sizeof (int));
  B.arreglo = (int *) malloc (10 * sizeof (int));
  C.arreglo = (int *) malloc (20 * sizeof (int));

  A.tamanio = 10;
  B.tamanio = 10;
  C.tamanio = 20;

  for (i = 0; i < 10; i++)
    {
      *(A.arreglo + i) = i + 1;
      *(B.arreglo + i) = i + 2;
    }

  if (agregar (&A, 1) == (2 || 3) || agregar (&B, 2) == (2 || 3))
    return -1; //No se pudo agregar

  if (unir (A, B, &C) == 3)
    return -1;			//No pudo unir

  mostrar (A);
  puts ("\n");
  mostrar (B);
  puts ("\n");
  mostrar (C);

  return 0;

}
