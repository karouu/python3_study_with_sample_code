#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


int main(void)
{
    char a[2];
    a[0]='5';
    a[1]='\0';
    printf("%s\n",a);
    int n=atoi(a);
    printf("n=%d\n",n);
    if(isdigit(a[0]))
        printf("a[0] is digit.\n");
    if(isdigit('a'))
        printf("a is digit.\n");

    if(isalnum(a[0]))
        printf("a[0] is a num.\n");
    if(isalnum('a'))
        printf("a is a num.\n");
}