#include <stdio.h>
#include <stdlib.h>
 
typedef struct nodo_s
{
 int dato;
 struct nodo_s *siguiente;
} nodo_t;
 
typedef nodo_t *Pila;
typedef nodo_t *Nodo;

void push(Pila *pila, int x)
{
     // Crea un nuevo nodo
     
     int i = x;
     for(i = x; i > 0; i--){
         Nodo nodo;
         nodo = (Nodo)malloc(sizeof(nodo_t));
         if (nodo != NULL){
                 nodo->dato = i;
                 // El apuntador nodo->siguiente va a apuntar al primer nodo de la lista ligada
                 nodo->siguiente = *pila;
                 // pila va a apuntar al nuevo nodo, con esto hacemos que el nuevo nodo sea ahora el primer nodo de la lista ligada
                 *pila=nodo;
             }
        }
    }
    
    void nodos_pila(Nodo nodo1, Nodo nodo2, Nodo nodo3, int cantidad)
    {//impresion de las torres 
     if (nodo1 == NULL)
         printf("La pila 1 esta vacia\n\n\n\n");
     else
         {
          while (nodo1 != NULL){
                int i = 0;
                 int espacio = cantidad - nodo1->dato;
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 for(i = 0; i < nodo1->dato; i++){
                       printf("=");
                 }
                 printf("|");
                 for(i = 0; i < nodo1->dato; i++){
                       printf("=");
                 }
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 nodo1 = nodo1->siguiente;
          printf("\n");
         }
         printf("\n\n\n\n");
    }
     if (nodo2 == NULL)
         printf("La pila 2 esta vacia\n\n\n\n");
     else
         {
          while (nodo2 != NULL){
                int i = 0;
                 int espacio = cantidad - nodo2->dato;
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 for(i = 0; i < nodo2->dato; i++){
                       printf("=");
                 }
                 printf("|");
                 for(i = 0; i < nodo2->dato; i++){
                       printf("=");
                 }
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 nodo2 = nodo2->siguiente;
         }
         printf("\n\n\n\n");
    }
     if (nodo3 == NULL)
         printf("La pila 3 esta vacia\n\n\n\n");
     else
         {
          while (nodo3 != NULL){
                int i = 0;
                 int espacio = cantidad - nodo3->dato;
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 for(i = 0; i < nodo3->dato; i++){
                       printf("=");
                 }
                 printf("|");
                 for(i = 0; i < nodo3->dato; i++){
                       printf("=");
                 }
                 for(i = 0; i < espacio; i++){
                       printf(" ");
                 }
                 nodo3 = nodo3->siguiente;
          printf("\n");
         }
         printf("\n\n\n\n");
    }
}
void cambiar(Pila *pila1, Pila *pila2, int cantidad)
{
     // Crea un nuevo nodo
     Nodo nodo1;
     int x, y;
      
     // El nuevo nodo va a apuntar al primer nodo de la lista ligada para sacarle el dato
     nodo1 = *pila1;
     if(nodo1 != NULL){
         x = (*pila1)->dato;//extraigo el dato 1
         if(*pila2 != NULL){
             
         y = (*pila2)->dato;//extraigo el dato 2
             }
         else{
              y = cantidad + 1;
         }
         if(x < y){//comparo el primero con el segundo para ver cual es mas grande
             // Ahora el segundo nodo de la lista ligada va a ser el primero
             *pila1 = (*pila1)->siguiente;
             // Borra el primer nodo de la lista ligada
             free(nodo1);//borramos el elemento
             Nodo nodo2;
             nodo2 = (Nodo)malloc(sizeof(nodo_t));
             if (nodo2 != NULL){
                 nodo2->dato = x;
                 // El apuntador nodo->siguiente va a apuntar al primer nodo de la lista ligada
                 nodo2->siguiente = *pila2;
                 // pila va a apuntar al nuevo nodo, con esto hacemos que el nuevo nodo sea ahora el primer nodo de la lista ligada
                 *pila2=nodo2;
             }
         }
         else{
              printf("\nDestino invalido, el disco de origen es mas grande\n");
         }
     }
     else{
          printf("\n La torre esta vacia \n");
     }
}
int comprobar(Nodo nodo)
    {
    int cuenta = 0;
     if (nodo == NULL){
         printf("La pila esta vacia\n\n\n\n");
         return 0;
         }
     else
         {
          while (nodo != NULL){
                cuenta++;
                 nodo = nodo->siguiente;
                 }
    }
    return cuenta;
     
}
