/*
author: Fernando Natan Lopez Perez
group: 1cv8
*/
#include <iostream>
using namespace std;
class Pila{
	public:
		int valor;
};

int main(void){
	Pila arreglo[30];
	int cuenta=-1;
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
				
			if (cuenta<30){
				cuenta++;
				arreglo[cuenta].valor=valor;
			}
			else{
				cout<<"pila llena\n";
			}
		}
		else if(opc == 2){//muestra
			if(cuenta >= 0){
				cout<<arreglo[cuenta].valor;
			}
			else{
				cout<<"no hay datos\n";
			}
		}
		else if(opc == 3){//extrae
			if(cuenta >= 0){
				
				cuenta--;
				//arreglo[cuenta].valor= NULL;
			}
			else{
				cout<<"no hay datos\n";
			}
		}
		else if(opc == 4){//salir
			break;
		}
		else{
			cout<<"Teclee una opcion valida\n";
		}
		
	}
}
