#include <stdio.h>
#include "cs50.h"

int main(void)
{
    int *numbers = NULL;
    int capacity = 0;
    int size=0;
    
    while(true)
    {
        //input a number
        int number=get_int("input a number:");
        //judge the if numner is in the array already
        bool found=false;
        
        if(number==INT_MAX)
            break;

        for(int i=0;i<size;i++)
        {
            if(numbers[i]==number)
            {
                found=true;
                break;
            }
        }

        //if not in the array, add to array
        if(!found){
            int *tmp=realloc(numbers,sizeof(int)*(size+1));
            numbers=tmp;
            //operation again until array reaches the capacity
            capacity++;
            numbers[size]=number;
            size++;
        }
    }
    //print the array
    printf("\n");
    for(int i=0;i<size;i++)
        printf("numbers[%d]=%d\n",i,numbers[i]);

    free(numbers);

}