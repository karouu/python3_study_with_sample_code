#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n=get_int("Height: ");
    while(n<0||n>23)
    {
        n=get_int("your height is out of range,pls input again: ");
    }
    int m=n-1;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m-i;j++)
        {
            printf(" ");
        }
        for(int k=m-i;k<n;k++)
        {
            printf("$");
        }
        printf("  ");
        for(int k=m-i;k<n;k++)
        {
            printf("$");
        }
        printf("\n");
    }
}