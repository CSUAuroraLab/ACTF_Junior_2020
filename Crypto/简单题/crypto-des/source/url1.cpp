#include <stdio.h> 
char flag[32]="Interestring Idea to encrypt";
 
int main() 
{    
	for(int i=0;i<7;++i)
	{        
		printf("%20f\n",*(float*)(flag+i*4));    
	} 
	printf("%20f\n",*(float*)(""))  ; 
	return 0; 
}
