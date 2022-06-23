#include <stdio.h>
#include <stdlib.h>

struct myArray {
    int arraySize;
    int array[];
};

int main(void) {
    int desiredSize;
    struct myArray *ptr;
    
    scanf("%d\n", &desiredSize);

    ptr = malloc( sizeof( struct myArray ) + desiredSize * sizeof( int ) );

    for (int i = 0; i < desiredSize; i++) {
        scanf("%d ", &(ptr -> array[i]));
    } 

    for (int i = 0; i < desiredSize; i++) {
        printf("%d ", ptr -> array[i]);
    }


    return 0; 
}