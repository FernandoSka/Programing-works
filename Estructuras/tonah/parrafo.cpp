#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <string.h>
#include <time.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main () {
  
  srand (time(NULL));
  string input;
  int i,  j;
  ifstream archivo ("parrafos.txt", ifstream::binary);
  char pini[] = "<p style='font-size: 40px;background-color: #";
  char pinif[] = ";'>";
  char pfin[] = "</p>";
  char hexad[] = "0123456789ABCDEF";
  char **pararray, *ultima;
  pararray = (char**)malloc(1*sizeof(char*));
  char *parrafos;
  if (archivo) {
    // get length of file:
    archivo.seekg (0, archivo.end);
    int length = archivo.tellg();
    archivo.seekg (0, archivo.beg);

    char * buffer = new char [length];

    cout << "Reading " << length << " characters... ";
    // read data as a block:
    archivo.read(buffer,length);

    if (archivo){
       cout << "all characters read successfully.";
      }
    else{
      cout << "error: only " << archivo.gcount() << " could be read";
      }
    archivo.close();
    parrafos = strtok(buffer, "\n");
    int cuenta = 0;
    while (parrafos != NULL)
  {
    pararray[cuenta] = parrafos;
    parrafos = strtok (NULL, "\n");
    if(parrafos != NULL){
      cuenta++;
      pararray = (char**)realloc(pararray, (cuenta+1) * sizeof(*pararray));
      }
  }/*
  for(i = 0; pararray[cuenta][i] != '\0'; ++i);
  ultima = (char*)malloc((i-6)*sizeof(char));
  strncpy(ultima,pararray[cuenta],i-6);
  pararray[cuenta] = ultima;*/
  ofstream myfile;
  myfile.open("parrafos.html");
  myfile << "<HTML><HEAD><TITLE>parrafos</TITLE></HEAD><BODY>";
  for(i = 0; i<=cuenta; i++){
         myfile <<pini;
         for(j = 0; j<6; j++){
              int temp = rand() % 16;
               myfile <<hexad[temp];
              }
         myfile <<pinif<<pararray[i]<<pfin;
  }
  myfile << "</BODY></HTML>";
  myfile.close();

    // ...buffer contains the entire file...
  }
  
  return 0;
}
