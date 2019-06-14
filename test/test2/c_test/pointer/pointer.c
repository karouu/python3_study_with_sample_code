/*
#include<stdio.h>
int main()
{
	int *p;
	printf("%X\n",p);
	return 0;
} 
*/

/*
#include<stdio.h>
int main()
{
	int a=100,b=10;
	int *pointer_1,*pointer_2;
	pointer_1=&a;
	pointer_2=&b;
	printf("%d,%d\n",a,b);
	printf("%d,%d\n",*pointer_1,*pointer_2);
	
	return 0;
} */

/*
#include<stdio.h>
int main()
{
	int *max,*min,*tmp,a,b;
	scanf("%d	%d",&a,&b);
	max=&a;
	min=&b;
	if(*max<*min)
	{
		tmp =max;
		max=min;
		min=tmp;
	}
	printf("a=%d,b=%d\n",a,b);
	printf("max=%d,min=%d\n",*max,*min);
	
	return 0;
}*/

/*
#include<stdio.h>
void swap(int *p1,int *p2);

int main(void)
{
	int a,b;
	int *pointer_1,*pointer_2;
	scanf("%d %d",&a,&b);
	pointer_1=&a;
	pointer_2=&b;
	if(a<b)
	{
		swap(pointer_1,pointer_2);
	}
	printf("%d,%d\n",a,b);
	
	return 0;
} 

void swap(int *p1,int *p2)
{
	int temp;
	temp = *p1;
	*p1=*p2;
	*p2=temp;
	
}*/
 
/*
 #include <stdio.h>
// 交换两个数
void swap(int *p1,int *p2){
    int *p;
    p = p1;
    p1 = p2;
    p2 = p;
}
int main(){
    int a, b;
    int *pointer_1, *pointer_2;
    scanf("%d, %d",&a, &b);
    pointer_1 = &a;
    pointer_2 = &b;
    if(a<b){
        swap(pointer_1, pointer_2);
    }
    printf("%d		%d\n",a, b);
    return 0;
}*/

/*
#include<stdio.h>
int main()
{
	int a=5;
	int *p;p=&a;
	printf("%d\n",*p);
	return 0;
}
*/

/*
#include<stdio.h>
int main(void)
{
	int a=10,b=20,sum,product,*pa,*pb;
	pa=&a;
	pb=&b;
	sum=*pa+*pb;
	product=*pa**pb;
	printf("%d,%d,%d,%d\n",a,b,a+b,a*b);
	printf("%d,%d,%d,%d\n",*pa,*pb,sum,product);
	
	return 0;
}*/

/*
#include<stdio.h>
int main(void)
{
	int a,b;
	char str[10];
	str[10]="bad.";
	a=sizeof str;
	b=strlen(str);
	printf("a=%d\nb=%d\n",a,b);
	
	return 0;
} 
*/

/*
#include<stdio.h>
int main(void)
{
	char *string="I love guanghzou.!";
	printf("%s\n",string);
	return 0;
}*/

/*
#include<stdio.h>
void filter(int *str)
{
	int i;
	for(i=0;i<5;i++)
	{
		if(str[i]<=0)
		str[i]=0;
	}
	
}



int main(void)
{
	int a[5],i;
	for(i=0;i<5;i++)
	scanf("%d",&a[i]);
	filter(a);
	for(i=0;i<5;i++)
	printf("%d",a[i]);
	printf("\n");
	//puts(a);
	
	return 0;
	
}*/


/*
#include<stdio.h>
int main(void)
{
	int i,str[5]={1,2,3,4,5};
	for(i=0;i<5;i++)
	printf("%d\n",str[i]);
	return 0;
} 
*/


/*
#include<stdio.h>
int main(void)
{
	char str1[10],str2[10];
	scanf("%s",str1);
	scanf("%s",str2);
	printf("%s\n%s\n",str1,str2);
	
	return 0;
}
*/

/*
#include<stdio.h>
int main(void)
{
	char str[20],*ps;
	int i;
	printf("Input a string:");
	ps=str;
	scanf("%s",ps);
	for(i=0;ps[i]!='\0';i++)
		if(ps[i]=='k')
		{
			printf("There is a 'k' in the string.\n");
			break;
		}
	if(ps[i]=='\0')
	printf("There is no 'k' in the string.\n");
	
	return 0;
}
*/
/*

#include<stdio.h>
void cpystr(char *str1,char *str2);
int main(void)
{
	char *a="so lazy",b[30],*pb;
	pb=b;
	cpystr(pb,a);
	printf("string a=%s\nstring b=%s\n",a,b);
	return 0; 
}

void cpystr(char *str1,char *str2)
{
	while((*str1=*str2)!='\0')
	{
		str1++;
		str2++;
	}
}*/

#include<stdio.h>
int main(void)
{
	int a[3][4]={0,1,2,3,4,5,6,7,8,9,10,11};
	printf("a=%d \n",a);
	printf("*a=%d \n",*a);
	printf("a[0]=%d \n",a[0]);
	printf("&a[0]=%d \n",&a[0]);
	printf("&a[0][0]=%d \n",&a[0][0]);
	printf("\n");
	
	printf("a+1=%-8d \n",a+1);
	printf("*(a+1)=%-8d \n",*(a+1));
	printf("a[1]=%-8d \n",a[1]);
	printf("&a[1]=%-8d \n",&a[1]);
	printf("&a[1][0]=%-8d \n",&a[1][0]);
	printf("\n");
	
	printf("a+2=%d \n",a+2);
	printf("*(a+2)=%d \n",*(a+2));
	printf("a[2]=%d \n",a[2]);
	printf("&a[2]=%d \n",&a[2]);
	printf("&a[2][0]=%d \n",&a[2][0]);
	printf("\n");
	
	printf("a[1]+1=%-8d \n",a[1]+1);
	printf("*(a+1)+1=%-8d \n",*(a+1)+1);
	printf("*(a[1]+1)=%-8d \n",*(a[1]+1));
	printf("*(*(a+1)+1)=%-8d \n",*(*(a+1)+1));
	
	return 0;
	
	
	
	
	
} 



