#include<stdio.h>

char flag[25] = {"actf{my_naive_encrytion}"};

int main()
{
	int i;
	for(i=0;i<25;i++)
	{
		flag[i] -= 3;
		flag[i] ^= 0x7;
		printf("%c",flag[i]);
	}
	return 0; 
}
