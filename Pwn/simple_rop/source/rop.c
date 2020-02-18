#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char whoami[0x10] = "who can turn to be a hacker?";
char binsh[0x10] = "/bin/sh\x00";

void vulnable();
void copy(char* buf, int what);

int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	puts("You need search Rop");
	vulnable();
}

void vulnable()
{
	unsigned int cur;
	srand(time(0));
	char buf[0x30] = {0};
	read(0, buf, 0x30);
	puts("Give you a cursor: ");
	scanf("%ud", &cur);
	copy(buf, cur);
	return;
}
void copy(char* buf, int what)
{
	char flow[0x10];
	int a, cur;
	a = abs(what);				/*trick*/
	if(a >= 0)
	{
		cur = rand()%0x10;		
		*(char*)(buf + (0x10 - cur)) = 0; /*wrong way*/
	}
	else
	{
		cur %= 0x20;			/*0x80000000 -> 0*/
	}
	memcpy(flow+cur, buf, strlen(buf));
	puts("copy over!");
}

void hack()
{
	puts("cat flag!");
	system("kill the flag");
}    


/*
gcc -fno-stack-protector -m32 rop.c -o rop
*/