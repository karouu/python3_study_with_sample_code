#include <stdlib.h>

void foo(void)
{
    int *x=malloc(10*sizeof(int));
    x[9]=0;
    free(x);
}

int main(void)
{
    foo();
    return 0;
}