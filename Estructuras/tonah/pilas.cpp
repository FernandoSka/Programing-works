#include <iostream>
using namespace std;
class Nodo{
      public:
             int valor;
             Nodo *siguiente;
             };
typedef Nodo *pnodo;
class Pila{
      public:
             pnodo actual, aux;
             Pila(){actual = NULL;aux = NULL;}
             void inserta(int val_ext);
             void muestra(void);
             void extrae(void);
             };
void Pila::inserta(int valorext){
     aux = new(Nodo);
     aux->siguiente = NULL;
     if(aux!=NULL){
     	aux->valor = valorext;
     	if(actual != NULL){
     		aux->siguiente = actual;
		 }
		 actual = aux;
	 }
                        
            }
void Pila::muestra(){
     if(actual != NULL){
         cout<<actual->valor;
     }
     else{
          cout<<"\n No hay datos\n";
     }
}
void Pila::extrae(){
     if(actual!=NULL){
	 
     if(actual->siguiente!=NULL){
     	actual = actual->siguiente;
	 }
	 else{
          actual = NULL;
          }
                        
            }
    else{
         cout<<"\n No hay datos\n";
         }
            }

int main(void){
	Pila p1;
	while(true){
		int opc=0;
		cout<<"\nteclee opcion\n";
		cout<<"1)inserta\n";
		cout<<"2)muestra\n";
		cout<<"3)extrae\n";
		cout<<"4)salir\n";
		cin>>opc;
		if (opc == 1){//inserta
			int valor = 0;
			cout<<"inserta valor\n";
			cin>>valor;			
			p1.inserta(valor);
		}
		else if(opc == 2){//muestra
			p1.muestra();
		}
		else if(opc == 3){//extrae
			
			p1.extrae();
		}
		else if(opc == 4){//salir
			break;
		}
		else{
			cout<<"Teclee una opcion valida\n";
		}
		
	}
}
