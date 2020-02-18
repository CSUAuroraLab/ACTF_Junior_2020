#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* g_complaint;
char* cps_contents[0x10];
int cps_len[0x10];

void welcome()
{
	puts("******** Welcome to Complain to Questioner ********");
	g_complaint = malloc(0x100);
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
}

void addComplain()
{
	int len, i;
	for(i=0; i<0x10; i++)
	{
		if(!cps_contents[i])
			break;
	}
	if(i == 0x10)
	{
		puts("You made so much complaints!");
		return;
	}

	puts("The complaint length you want:");
	scanf("%d",&len);
	if(0<len && len < 0x100)
	{
		printf("Input your complaint:");
		g_complaint[read(0, g_complaint, len)]=0;
		cps_len[i] = len;
		cps_contents[i] = malloc(len);
		strcpy(cps_contents[i], g_complaint);
	}
	else
	{
		puts("Your complaint is too long!!!");
	}
	return;

}

void modifyComplain()
{
	int index;
	puts("The complaint index you want to modify:");
	scanf("%d", &index);
	if(cps_contents[index])
	{
		printf("Input your complaint:");
		read(0, cps_contents[index], cps_len[index]);
	}
}

void showComplain()
{
	int index;
	puts("The complaint index you want to show:");
	scanf("%d", &index);
	if(cps_contents[index])
	{
		puts("Your complaint: ");
		write(1, cps_contents[index], cps_len[index]);
		puts("");
	}
}
void rmComplain()
{
	int index;
	puts("The complaint index you want to delete:");
	scanf("%d", &index);
	if(cps_contents[index])
	{
		free(cps_contents[index]);
		cps_contents[index] = 0;
	}

}
void submitComplain()
{
	int i;
	puts(" ******* Thanks to your Complains!     ******* ");
	puts(" ******* But i will delete all... hhh! ******* ");
	for(i=0; i<0x10; i++)
	{
		if(cps_contents[i])
		{
			free(cps_contents[i]);
			cps_contents[i] = 0;
		}

	}
}
void give_up()
{	
	int i;
	puts("Thanks to your complaints!");
	for(i=0; i<0x10; i++)
	{
		if(cps_contents[i])
		{
			free(cps_contents[i]);
			cps_contents[i] = 0;
		}

	}
	exit(0);
}

int menu()
{
	puts(" ***** Do any complaints as below! *****  ");
	puts(" ######################################## ");
	puts("			EE		 ##	  EE			    ");
	puts("			EE		 ##	  EE				");
	puts(" **[1]**  Create   ##   complaint    **** ");
	puts(" **[2]**  Modiefy  ##   complaint    **** ");
	puts(" **[3]**  Delete 	 ##   complaint    **** ");
	puts(" **[4]**  Show 	 ##   complaints   **** ");
	puts(" **[5]**  Submit 	 ##   complaints   **** ");
	puts(" **[0]**  Give up  ##   Exit  	   **** ");
	printf("Your choice: ");
	int ch;
	scanf("%d", &ch);
	return ch;
}


int main()
{
	int act;
	welcome();
	while(1)
	{
		act = menu();
		switch(act){
			case 1:
				addComplain();
				break;
			case 2:
				modifyComplain();
				break;
			case 3:
				rmComplain();
				break;
			case 4:
				showComplain();
				break;
			case 5:
				submitComplain();
				break;
			case 0:
				give_up();
			default:
				puts("No rule for your choice!");
				continue;
		}
	}
	return 0;
}
/*gcc complaint.c -o complaint*/