#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float f;
    do
    {
        f=get_float("Owed change: ");
    }
    while(f<0||f>1);

    int count=0;
    int cent = (int)(f*100);

    count = cent/25;
    cent %=25;

    count += cent/10;
    cent %= 10;

    count += cent/5;
    cent %= 5;

    count += cent;

    printf("%d\n",count);
}