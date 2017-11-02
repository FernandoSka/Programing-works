/*
Author: Lopez Perez Fernando
*/
#include <stdio.h>
#include <stdlib.h>
#include "hanoi.h"
int main(){
    Pila pila[3] = {NULL, NULL, NULL};
    int cantidad = 0;
    printf("ingrese la cantidad de discos para jugar \n");
    scanf("%d",&cantidad);
    push(&pila[0], cantidad);
    nodos_pila(pila[0], pila[1], pila[2], cantidad);
    int cons = 1, pasos = 0;
    while(cons == 1){
         int opc;
         printf("teclee una opcion \n\n");
         
         printf("1) Mostrar torres \n");
         printf("2) Intercambiar discos\n");
         printf("3) Rendirse \n");
         printf("4) Comprobar torres\n");
         scanf("%i", &opc);
         if(opc == 1){
             nodos_pila(pila[0], pila[1], pila[2], cantidad);
         }
         else if(opc == 2){
              int ori, dest;
              printf("teclee el origen\n");
              scanf("%d",&ori);
              ori = ori - 1;
              printf("teclee el destino\n");
              scanf("%d",&dest);
              dest = dest -1;
              if(ori >= 0 && ori <= 2 && dest >= 0 && dest <= 2){
                  if(ori != dest){
                      cambiar(&pila[ori], &pila[dest], cantidad);
                      pasos++;
                  }
                  
                  else{
                      printf("\n No se puede cambiar en la misma posicion\n");
                  }
              }
              else{
                  printf("torres invalidas, seleccione torres existentes del 1 al 3\n\n"); 
              }
         }
         else if(opc == 3){
              printf("\nHaz perdido");
              cons = 2;
              break;
              }
         else if(opc == 4){
              int torre1 = comprobar(pila[1]);
              int torre2 = comprobar(pila[2]);
              if(torre1 == cantidad){
                  printf("\nHaz ganado en %i pasos", pasos);
                  cons = 2;
                  break;
              }
              if(torre2 == cantidad){
                  printf("\nHaz ganado en %i pasos", pasos);
                  cons = 2;
                  break;
              }
              printf("\nninguna torre completa, sigue jugando\n");
              }
         else{
              printf("\nOpcion invalida\n");
              }
    }
    getch();//sin este comando tambien funciona en linux :v
    
    return 0;
}
