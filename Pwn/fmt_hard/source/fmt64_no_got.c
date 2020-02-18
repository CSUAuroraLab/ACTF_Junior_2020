#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pvoit()
{
	setbuf(stdin, 0, 2, 0);
	setbuf(stdout, 0, 2, 0);
	setbuf(stderr, 0, 2, 0);
	puts("This's my mind!");
	no_return(stdout);
}
void no_return(FILE *a)
{
	char s[256];
	while(read(0, s, 0x100))
	{
		fprintf(a, s);
		sleep(1);
	}
	exit(0);

}
int main()
{
	pvoit();
}
/*gcc -fPIC -pie -z now fmt64_no_got.c -o fmt64*/