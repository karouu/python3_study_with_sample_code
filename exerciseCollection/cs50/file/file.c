#include <stdio.h>
#include <cs50.h>

int main(int argc, char **argv)
{
    if(argc<2)
    {
        printf("pls enter a filename.\n");
        return 0;
    }
    FILE *in = fopen( argv[1],"r" );
    FILE *out = fopen( "out.txt","w" );

/*
// fgetc()&fputc() example
    char c;
    while((c=fgetc(in))!=EOF)
    {
        printf("%c",c);
        fputc(c,out);
    }


// fgets() example
    char s[5];
    while(fgets(s,5,in)!=NULL)
    {
        printf("%s",s);
    }

    string s2=get_string("input a string: ");
    fputs(s2,out);
*/
    char s[10];
    while(fread(s,10,1,in))
    {
        printf("%s",s);
        fwrite(s,10,1,out);
    }
    fclose(in);
    fclose(out);
}