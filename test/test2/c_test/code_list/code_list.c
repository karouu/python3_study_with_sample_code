//6.1 summing.c 
/*
#include <stdio.h>
int main(void)
{
	long num;
	long sum = 0;
	//int status;
	_Bool input_is_good;
	
	
	printf("please enter an integer to be summed.");
	printf("(q to quit):");
	//status = scanf("%ld",&num);
	input_is_good=(scanf("%ld",&num)==1);
	
	while(input_is_good == 1)
	{
		sum= sum+num;
		printf("please enter next integer (q to quit):");
		//status = scanf("%d",&num);
		input_is_good=(scanf("%ld",&num)==1);
		
	}
	printf("Those integer sum to %ld.\n",sum);
    return 0;
    
} 
*/

//6.2 when to quit a loop
/*
#include <stdio.h>
int main(void)
{
	int n=5;
	while(n<10)
	{
		printf("n=%d\n",n);
		n++;
		printf("Now n=%d\n",n);
	}
	printf("The loop has finished.\n");
	return 0;
}
*/

//6.3 while 1.c 
/*
#include <stdio.h>
int main(void)
{
	int n=0;
	while (n++<3)
		printf("n is %d\n",n);
		//n++;
		printf("That's all this program does\n");
		return 0;
}
*/

//6.5 compare float.c
/* 
#include <stdio.h>
#include <math.h>
int main(void)
{
	const double ANSWER=3.14159;
	double response;
	printf("What is the value of pi.\n");
	scanf("%lf",&response);
	while(fabs(response-ANSWER)>0.0001)
	{
		printf("Try again!\n");
		scanf("%lf",&response);
	}
	printf("Close enough!\n");
	return 0;
}
*/

// 6.6 true or false
/*
#include <stdio.h>
int main(void)
{
	int true_val,false_val;
	true_val=(100>='a');
	false_val=(2==3);
	printf("the result of true_val is %d.\nthe result of false_val is %d.\n",true_val,false_val);
	return 0; 
}
*/

//6.7 truth.c
/*
#include <stdio.h>
int main(void)
{
	int n;
	n=3;
	while (n)
	printf("%d is true.\n",n--);
	printf("%d is false.\n",n);
	
	n=-3;
	while(n)
	printf("%d is true.\n",n++);
	printf("%d is false.\n",n);
	
	return 0;
}
*/

/* 
// 6.10&6.11 while/for
#include<stdio.h>
int  main(void)
{
	int num=5;
	
	
	int i;
	//int i=0;
	//while(i++<num)
	
	for(i=0;i<num;i++)
	printf("be my lover,pls!\n");
	return 0;
	
}
*/

/* 
//6.12 for_cube.c 
#include <stdio.h>
int main(void)
{
	int n;
	//int cube
	printf("n	n^3\n");
	for(n=1;n<10;n++)
		printf("%d	%d\n",n,n*n*n);
	return 0;
}
*/

/* 
//6.14 zeno.c
# include<stdio.h>
int main(void)
{
	//int n;
	float n,sum;
	for(n=1.,sum=0.;n>0.;n=n/2.)
	printf("the result of sum is %f.\n",sum+=n);
	return 0;
}
*/

/* 
// 6.19 scores_in.c
#include <stdio.h>
#define SIZE 4
#define PAR 72
int main (void)
{
	int index,score[SIZE];
	int sum=0;
	float average;
	
	printf ("Enter %d golf scores: \n",SIZE);
	for (index=0;index<SIZE;index++)
		scanf("%d",&score[index]);
	printf("The scores read in are as follows:\n");
	for (index=0;index<SIZE;index++)
		printf("%5d",score[index]);
		printf("\n");
	for(index=0;index<SIZE;index++)
		sum+=score[index];
	average=(float)sum/SIZE;
	printf("Sum of scores = %d,average = %.2f\n",sum,average);
	printf("That's a handicap of %.0f.\n",average-PAR);
	return 0; 
} 
*/

/* 
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    char cmd[20]="shutdown -s -t ";
    char t[5]="0";
    int c;

    system("title C语言关机程序");  //设置cmd窗口标题
    system("mode con cols=48 lines=20");  //窗口宽度高度 
    system("color fc");//system("color f0");  //可以写成 red 调出颜色组
    system("date /T");
    system("time /T");

    printf("----------- C语言关机程序 -----------\n");
    printf("1.实现10分钟内的定时关闭计算机\n");
    printf("2.立即关闭计算机\n");
    printf("3.注销计算机\n");
    printf("0.退出系统\n");
    printf("-------------------------------------\n");

    scanf("%d",&c);
    switch(c) {
        case 1:
            printf("您想在多少秒后自动关闭计算机？（0~600）\n");
            scanf("%s",t);
            system(strcat(cmd,t));
            break;
        case 2:
            system("shutdown -p");
            break;
        case 3:
            system("shutdown -l");
            break;
        case 0:
            break;
        default:
            printf("Error!\n");
    }
    system("pause");
    return 0;
} 
*/

/* 
// 6.20 power.c
#include <stdio.h>
double power(double n,int p);
int main(void)
{
	double x,xpow;
	int exp;
	
	printf("Enter a number and the positive integer power ");
	printf("to which\nthe number will be raised.Enter q ");
	printf("to quit.\n");
	while (scanf("%lf%d",&x,&exp)==2)
	{
		xpow=power(x,exp);
		printf("%.3g to the power %d is %.5g\n",x,exp,xpow);
		printf("Enter next pair of numbers or q to quit.\n");
	}
	printf("Hope you enjoyed this power trip -- bye!\n");
	return 0;
	
} 

double power(double n,int p)
{
	double pow=1;
	int i;
	
	for(i=1;i<=p;i++)
	pow *=n;
	return pow;
}
*/

 #include <stdio.h>
#include <stdlib.h>
int main() {
    printf("Date : %s\n", __DATE__);
    printf("Time : %s\n", __TIME__);
    printf("File : %s\n", __FILE__);
    printf("Line : %d\n", __LINE__);
    system("pause");
    return 0;
}