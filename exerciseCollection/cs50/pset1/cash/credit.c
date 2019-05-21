#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int char2int(char c)
{
    char a[2];
    a[0]=c;
    a[1]='\0';
    return atoi(a);
}

int main(void)
{
    string s;
    int length,stat;
    do
    {
        stat=0;
        s= get_string("input your credit number: ");
        length=strlen(s);
        for(int i=0;i<length;i++)
            if(!isdigit(s[i]))
                stat = 1;
                continue;
    }
    while(stat);

    //sum1 is the even sequence, sum2 is the odd sequence.
    int flag=1,sum1=0,sum2=0,convert=0,convert1=0,convert2=0;
    printf("length = %d\n",length);

    for(int i=0;i<length;i++)
    {
        if(i%2==0)
        {
            sum1 += char2int(s[i]);
            printf("s[%d]=%c,sum1=%d\n",i,s[i],sum1);
        }
        else
        {
            //convert is the every other digit multiply by 2,convert1 is the decimal digit of convert,and convert2 is less than 10 number
            convert=char2int(s[i])*2;
            convert1=convert/10;
            convert2=convert%10;
            sum2 = sum2+convert1+convert2;
        }
    }
    printf("sum1=%d,sum2=%d\n",sum1,sum2);
    flag = (sum1+sum2)%10;

    if(flag==0)
    {
        printf("valid!\n");
    }
    else
    {
        printf("invalid number.\n");
    }

}