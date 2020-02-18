#include<stdio.h>

char flag[25]={"Ygvdmq[lYate[elghqvakl}"};

int main()
{
	int i;
	for(i=0;i<25;i++)
	{
		flag[i] ^= 0x7;
        flag[i] += 3;
		printf("%c",flag[i]);
	}
}
