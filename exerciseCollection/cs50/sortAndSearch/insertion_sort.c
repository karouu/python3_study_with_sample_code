#include <stdio.h>

int main(void)
{
    int num[6]={5,1,6,2,4,3};
    int length = 6;
    int sort[length];
    for(int i=0;i<length;i++)
    {
        sort[i]=0;
    }

    sort[0]=num[0];
    for(int i=1;i<length;i++)
    {
        for(int j=0;j<i;j++)
        {
            if( num[i]>=sort[j]&&num[i]<sort[j+1] )
            {
                for(int k=i;k>=j;k--)
                {
                    sort[k+1]=sort[k];
                }
                sort[j]=num[i];
            }
        }
    }

    for(int i=0;i<length;i++)
    {
        printf("%d ",sort[i]);
    }
    printf("\n");

}