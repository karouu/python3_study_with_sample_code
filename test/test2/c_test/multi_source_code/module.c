#include <stdio.h>
// 当前操作系统
char *OS = "Windows 7";
long sum(int fromNum, int endNum){
    int i;
    long result = 0;
    // 参数不符合规则，返回 -1
    if(fromNum<0 || endNum<0 || endNum<fromNum){
        return -1;
    }
    for(i=fromNum; i<=endNum; i++){
        result += i;
    }
    // 返回大于等于0的值
    return result;
}