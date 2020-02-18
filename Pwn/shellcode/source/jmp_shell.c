#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//gcc -fno-stack-protector -z execstack jmp_shell.c -o jmp_shell
void vulnable();
void jmp();
int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	puts("U have read 0day!");
	vulnable();
}

void vulnable()  
{
	char buf[0x20] = {0};
	read(0, buf, 0x30);
	return;
}   
void jmp()
{
	__asm__
	(
		"sub $0x30, %rsp\n\t"
		"jmp %rsp"
	);
}