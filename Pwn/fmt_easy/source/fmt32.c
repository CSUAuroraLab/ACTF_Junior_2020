#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int key1, key2;

int lucky(int *key1, int *key2);

void hack();
void r_init()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	srand(time(0));
}
int main()
{
	r_init();
	key1 = rand();
	key2 = rand();
	if(lucky(&key1, &key2))
	{
		hack();
	}
	else
	{
		puts("haha!");
	}
}

int lucky(int *key1, int *key2)
{
	int passwd;
	char name[32];
	puts("Tell me your name:");
	fgets(name, 32, stdin);
	printf("hello,");
	printf(name);

	return (*key1) == 2*(*key2);
}

void hack()
{
	puts("give you the score!");
	system("cat flag");
}
/*gcc -m32 -fstack-protector-all fmt32.c -o fmt32*/