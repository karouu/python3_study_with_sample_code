#include <stdio.h>
#include "cs50.h"

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *numbers = NULL;

    while(true)
    {
        //input a number
        int number=get_int("input a number:");
        if(number==INT_MAX)
            break;
        //judge the if numner is in the array already
        bool found=false;

        for(node *ptr=numbers; ptr!=NULL;ptr=ptr->next)
        {
            if(ptr->number == number)
            {
                found=true;
                break;
            }
        }

        //if not in the array, add to array
        if(!found){

            node *n = malloc(sizeof(node));
            n->number = number;
            n->next = NULL;

            if(numbers)
            {
                for(node *ptr=numbers;ptr!=NULL;ptr=ptr->next)
                {
                    if(!ptr->next)
                    {
                        ptr->next = n;
                        break;
                    }
                }
            }
            else
                numbers=n;
        }
    }

    printf("\n");
    for(node *ptr=numbers;ptr!=NULL;ptr=ptr->next)
        printf("%d\n",ptr->number);

    node *ptr=numbers;
    while(ptr!=NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }

}