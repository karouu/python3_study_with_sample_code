#include <stdio.h>
#include <conio.h>
// 也可以不写 extern；为了程序可读性，建议写上
extern long sum(int, int);
// 必须写 extern
extern char* OS;
int main()
{
    int n1 = -1, n2 = -100;
    printf("从%d加到%d的和为%ld [By %s]", n1, n2, sum(n1, n2), OS);
    getch();
    return 0;
}