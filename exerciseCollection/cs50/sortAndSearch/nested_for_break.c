#include <stdio.h>

int main(void)
{
    for(int i=0;i<9;i++)
    {
        printf("now i is %d\n",i);
        for(int j=0;j<i;j++)
        {

            if(i==5)
                break;
            printf("j=%d\n",j);
        }
        printf("\n");
    }
}