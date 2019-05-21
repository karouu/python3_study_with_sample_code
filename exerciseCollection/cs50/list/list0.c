#include <stdio.h>
#include "cs50.h"
int main(void)
{
    //capacity
    int capacity;
    do{
        capacity = get_int("capacity:");
    }while(capacity<1);

    int numbers[capacity];
    int size=0;
    while(size<capacity)
    {
    //input a number
        int number=get_int("input a number:");
    //judge the if numner is in the array already
        bool found=false;
        for(int i=0;i<size;i++)
        {
            if(numbers[i]==number)
            {
                found=true;
                break;
            }
        }
    //if not in the array ,insert the number inside th array
        if(!found){
            numbers[size]=number;
    //operation again until array reaches the capacity
            size++;
        }
    }

    //print the array
    for(int i=0;i<size;i++)
        printf("numbers[%d]=%d\n",i,numbers[i]);

}