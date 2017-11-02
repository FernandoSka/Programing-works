#include <stdio.h>
#include "pilas.h"
int main(){
    ptrPila pila = NULL;
    ptrNodo nodo = NULL;
    char c = 'h';
    char c2 = 'o';
    char c3 = 'l';
    push(&pila, c);
    push(&pila, c2);
    push(&pila, c3);
    nodos_pila(pila);
    getch();
    
    return 0;
}
