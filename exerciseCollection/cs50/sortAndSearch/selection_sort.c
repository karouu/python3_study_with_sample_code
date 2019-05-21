#include <stdio.h>

int main(void)
{
    int num[6]={5,1,6,2,4,3};
    int len_array=6;

    for(int i=0;i<len_array-1;i++)
    {

        for(int k=i+1;k<len_array;k++)
        {
            int j=num[i];
            if(num[i]<num[k])
            {
                num[i]=num[k];
                num[k]=j;
            }
        }
    }

    printf("selection sort array: \n");
    for(int i=0;i<len_array;i++)
    {
        printf("%d ",num[i]);
    }
    printf("\n");
}