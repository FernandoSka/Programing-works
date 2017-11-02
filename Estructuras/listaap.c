#include <stdio.h>
#include <stdlib.h>
void asignacion(int *arre[]);
int main(){
    int arr[10]={1,2,3,4,5,6,7,8,9,10};
    int x;
    for(x =0; x<10; x++){
        printf("%i ",arr[x]);
    }
    asignacion(arr);
    for(x =0; x<10; x++){
        printf("%i ",arr[x]);
    }
    getch();
    return 0;
}
void asignacion(int *arre[]){
     int x;
    for(x =0; x<10; x++){
        arre[x]=x+10;
    }
}

