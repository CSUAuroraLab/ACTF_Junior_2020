#include<stdio.h>

static char table[]="~}|{zyxwvutsrqponmlkjihgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)('&%$# !\"";

int main(void)
{
    char flag[18];
    char in[12];
    char out[12]={42,70,39,34,78,44,34,40,73,63,43,64};
    int i;
    printf("Please input:");
    //for(i=0;i<94;i++)
        //printf("%c",table[i]);

    scanf("%s",flag);
    //printf("%s",flag);


    if(flag[0]!=65 || flag[1]!=67 || flag[2]!=84 || flag[3]!=70 || flag[4]!=123 || flag[17]!=125)
    {
        return 0;
    }
    else{
        memcpy(in,flag+5,12);

        for(i=0;i<12;i++)
        {
            if(out[i]!=table[in[i]-1])
                return 0;
            //out[i]=table[in[i]-1];
            //printf("%i ",in[i]);
            //printf("%d ",table[in[i]-1]);
            //printf("%c ",out[i]);
            //printf("%i\n",out[i]);
        }
        printf("You are correct!");
        return 0;
    }
}
