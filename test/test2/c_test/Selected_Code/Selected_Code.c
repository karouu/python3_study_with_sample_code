/*
//1. scanf()有空格就停止，get()遇换行才停止 
#include<stdio.h>
int main(void)
{
	char str1[20],str2[20],str3[20],ch;

	scanf("%s",str1);
	//while((ch=getchar()!='\n'));
	gets(str2);
	gets(str3);
	printf("%s|%s|%s\n",str1,str2,str3);
	
	return 0;
} */

/*
//2. replace a string of blanks with a single blank.
#include<stdio.h>
#define NONBLANK 'a'
int main(void)
{
	char c,lastc;
	lastc=NONBLANK;
	while(1)
	{
	if((c=getchar())!=' '||lastc!=' ')
		putchar(c);
		
	lastc=c;
	}
	return 0;	
}
*/

/*
//3. the use of advanced printf( )   %[flags][width][.precision]
#include<stdio.h>
int main(void)
{
	int a='F';
	int b=12;
	int c=452;
	printf("&a=%#-16x&b=%#-16x&c=%#-16x\n",&a,&b,&c);
	printf("&a=%#-16X&b=%#-16X&c=%#-16X\n",&a,&b,&c);
	
	return 0;
}*/

/*
//4. 随机数生成 
#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a;
	srand((unsigned)time(NULL));
	 a=rand()%51+13;
	printf("%d\n",a);
	return 0;
}
*/

/*
//5. 关键字 continue; 的用法
#include<stdio.h>
int main(void)
{
	char c=0;
	while(c!='\n')
	{
		c=getchar();
		if(c=='4'||c=='5')
		{
			continue;  //跳出此次循环，直接进行下一次。 
		}
		putchar(c);
	}
	return 0;
}
 */
 
 
 
 
 