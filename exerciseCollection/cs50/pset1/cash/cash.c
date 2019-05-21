#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float change;
    do
    {
        change=get_float("Change Owed: ");
    }
    while(change<0||change>1);

    int c;
    c = (int) (change*100);
    int quarter=0,dime=0,nickel=0,penny=0;
    while(c>=25)
    {
        quarter++;
        c-=25;
    }
    while(c>=10)
    {
        dime++;
        c-=10;
    }
    while(c>=5)
    {
        nickel++;
        c-=5;
    }

    penny=c;

    printf("%d\n",quarter+dime+nickel+penny);

}