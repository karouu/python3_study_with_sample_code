//find 50 in the array

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int num[8] = {1,2,13,29,38,42,50,63};
    int min=0,max=7;
    int mid,count=0;
    int find=get_int("input number you want to find: ");

    while(count<20)
    {
        //for debug
        count++;
        printf("count = %d  min=%d  num[min]=%d \n",count,min,num[min]);

        //for the case find if out of range.
        if(mid==0||mid==7)
        {
            printf("the find isn't in the num array.\n");
            break;
        }

        //begin to search the find number using binary method
        mid=(min+max)/2;

        if(num[mid]>find)
        {
            max=mid-1;
            continue;
        }
        else if(num[mid]<find)
        {
            min=mid+1;
            continue;
        }
        else
        {
            printf("find is in num[%d]\n",mid);
            break;
        }

    }
}