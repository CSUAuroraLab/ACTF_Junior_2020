#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vulnable();
void readn(char* buf, int len);

int main()
{
	char fmt[0x8];

	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	puts("Give you a gift..."); /*leave a libc pointer stdout in stack*/
	read(0, fmt, 0x8);
	__printf_chk(1, fmt);		/*%a will leak the libc*/
	vulnable();
}

void vulnable()  
{
	char name[0x10] = {0};
	char content[0x30];
	int len;

	write(1, "Tell me U filename\n", 0x13);
	readn(name, 0x10);
	len = strlen(name) * 3 % 0x30;
	write(1, "And the content:\n", 0x11);
	readn(content, len);
	return;	
}    

void readn(char* buf, int len)
{
	char* idx = buf;
	int t;
	do{
		t = read(0, idx, 1);
		if(t <=0 )
			exit(1);
		if(*idx == 0xa)
			break;
		idx += 1;
	}while(idx != &(buf[len-1+1]));		/*over flow when len=0*/

}

/*gcc -fno-stack-protector chk_rop.c -o chk_rop*/