#include<stdio.h>

void func()
{
    int i;
    char enc_flag[17]={81,115,119,51,115,106,95,108,122,52,95,85,106,119,64,108,0};
    char flag[23];
    char in[16];
    printf("Please input:");
    scanf("%s",flag);

    if(flag[0]!=65 || flag[1]!=67 || flag[2]!=84 || flag[3]!=70 || flag[4]!=123)
        return;

    if(flag[21]!=125)
        return;

    memcpy(in,flag+5,16);

    for(i=0;i<16;i++)
    {
        if(in[i]>64 && in[i]<91)         //ด๓ะด
        {
            in[i]=(in[i]-65+14)%26+65;
            //printf("%i\n",in[i]);
        }
        if(in[i]>96 && in[i]<123)
        {
            in[i]=(in[i]-97+18)%26+97;
            //printf("%i\n",in[i]);
        }
        //printf("%i\n",in[i]);
    }

    for(i=0;i<16;i++)
    {
        if(in[i]!=enc_flag[i])
        {
            //printf("%i\n",in[i]);
            //printf("%i\n",enc_flag[i]);
            //printf("err %i",i);
            return;
        }
    }

    printf("You are correct!");
    return;

}

int main(void)
{
    func();
    return 0;
}
