#include <stdio.h>

int main(void)
{
    int num[6]={5,1,6,2,4,3};
    int length=6;
    for(int i=1;i<length;i++)
    {
        int pop=num[i];
        for(int j=0;j<i;j++)
        {
            if(num[i]<num[j])
            {
                for(int k=i-1;k>=j;k--)
                {
                    num[k+1]=num[k];
                }
                num[j]=pop;
            }
        }
    }
    printf("insertion sort num array is: \n");
    for(int i=0;i<length;i++)
    {
        printf("%d ",num[i]);
    }
    printf("\n");
}