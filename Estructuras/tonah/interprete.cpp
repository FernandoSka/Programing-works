#include "iostream"
#include "string"
#include "string.h"
#include "stdio.h"
#include <cstddef> // for std::size_t

template< class T, size_t N >
size_t length(const T (&)[N] )
{
  return N;
};

class Nodo{
      public:
             int valor;
             Nodo *siguiente, *anterior;
             };
class Lista{
      public:
             Nodo inicial, final, aux1, aux2;
             void inserta(int val_ext, int pos);
             void muestra(int pos);
             void extrae(int pos);
             };
using namespace std;
void imprime(){
     cout<<"hola";
     }
int main(void){
    int clav = 0, num = 0, pos = 0, i = 0, j = 0, k=0, cuenta = 0;  
    string dictclav[3][4];
    string dictnum[] = {"valor", "el", "numero"};
    string dictpos[] = {"posicion", "medio", "final", "inicio"};
    string lista[] = {"lista", "doblemente", "ligada"};
    string articulo1[] = {"el", "al", "la", "en", "de"};
    string articulo2[] = {"la", "una"};
    dictclav[0][0] = "mostrar";
    dictclav[0][1] = "muestra";
    dictclav[0][2] = "muestrame";
    dictclav[0][3] = "dame";
    dictclav[1][0] = "inserta";
    dictclav[1][1] = "mete";
    dictclav[1][2] = "insertame";
    dictclav[1][3] = "aniade";
    dictclav[2][0] = "borra";
    dictclav[2][1] = "elimina";
    dictclav[2][2] = "quita";
    dictclav[2][3] = "quitame";
    char *palabra,**palabras;
    
    palabras = (char**)malloc(1*sizeof(char*));
    string input;
    cout<<"inserte el texto";
    getline(cin, input);
    
    palabra = strtok((char*)input.c_str(), " ");
    
    while (palabra != NULL)
    {
        palabras[cuenta] = palabra;
        palabra = strtok (NULL, " ");
        if(palabra != NULL){
          cuenta++;
          palabras = (char**)realloc(palabras, (cuenta+1) * sizeof(*palabras));
          }
    }
    
    for(i = 0; i<=cuenta; i++){
          if(palabras[i] == dictclav[0][0] || palabras[i] == dictclav[0][1] || palabras[i] == dictclav[0][2] || palabras[i] == dictclav[0][3]){
              clav = 1;
          }
          if(palabras[i] == dictclav[1][0] || palabras[i] == dictclav[1][1] || palabras[i] == dictclav[1][2] || palabras[i] == dictclav[1][3]){
              clav = 2;
          }
          if(palabras[i] == dictclav[0][0] || palabras[i] == dictclav[2][1] || palabras[i] == dictclav[2][2] || palabras[i] == dictclav[2][3]){
              clav = 3;
          }
          if(palabras[i] == dictpos[0] || palabras[i] == dictpos[1] || palabras[i] == dictpos[2] || palabras[i] == dictpos[3] ){
              if(palabras[i] == dictpos[0]){
                  pos = atoi(palabras[i+1]);
                  }
              if(palabras[i] == dictpos[1]){
                  pos = 3
                  }
              if(palabras[i] == dictpos[2]){
                  pos = 2
                  }
              if(palabras[i] == dictpos[3]){
                  pos = 1
                  }
          }
    }
    
    cin>>input;
}
