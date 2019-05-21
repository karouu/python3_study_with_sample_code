#include <stdio.h>

int main(void)
{
    int num[6]={6,5,4,3,2,1};

// counter is the flag of buble sort is ending.
    int counter=0;

    while(counter!=0)
    {

// one buble period
        for(int i=0;i<5;i++)
        {
            if(num[i]>num[i+1])
            {
                counter++;
                int j=num[i];
                num[i]=num[i+1];
                num[i+1]=j;
            }
        }
    }

// print the num[] array, it's a little tedious, but neccessary.
    printf("sorted num[i] is :\n");
    for(int i=0;i<6;i++)
    {
        printf("%d ",num[i]);
    }
    printf("\n");
}
