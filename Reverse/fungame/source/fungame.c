#include<stdio.h>
#include<stdbool.h>
#include<string.h>

#define BASE64_PAD '='
#define BASE64DE_FIRST '+'
#define BASE64DE_LAST 'z

char x[20];
char y1[16]={35,97,62,105,84,65,24,77,110,59,101,83,48,121,69,91};
char y2[16]={113,4,97,88,39,30,75,34,94,100,3,38,94,23,60,122};
static const char table[] = {
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
	'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
	'w', 'x', 'y', 'z', '0', '1', '2', '3',
	'4', '5', '6', '7', '8', '9', '+', '/',
};

int sub_401340(char *readin)
{
    char i=0;

    printf("Please input:");
    scanf("%s",readin);

    for(i=0;i<16;i++)
    {
        if((y1[i]^readin[i])!=y2[i]){
            exit(0);
        }
    }

    return 0;
}

int sub_4013BA(char *readin)
{
    char content[4];

    strcpy(content,readin);
    strcpy(x,readin);

    return 0;
}

void sub_4013EC(void)
{
    int num_in_rank[13];
    int num_in_suit[4];
    bool card_exists[13][4];
    char ch,rank_ch,suit_ch;
    int rank,suit;
    bool bad_card;
    int cards_read=0;

    for(rank=0;rank<13;rank++){
      num_in_rank[rank]=0;
      for(suit=0;suit<4;suit++)
        card_exists[rank][suit]=false;
    }

    for(suit=0;suit<4;suit++)
      num_in_suit[suit]=0;

    while(cards_read<5){
      bad_card=false;


      rank_ch='2';
      switch(rank_ch){
        case '0':exit(0);
        case '2':rank=0;break;
        case '3':rank=1;break;
        case '4':rank=2;break;
        case '5':rank=3;break;
        case '6':rank=4;break;
        case '7':rank=5;break;
        case '8':rank=6;break;
        case '9':rank=7;break;
        case 't':case 'T':rank=8;break;
        case 'j':case 'J':rank=9;break;
        case 'q':case 'Q':rank=10;break;
        case 'k':case 'K':rank=11;break;
        case 'a':case 'A':rank=12;break;
        default:bad_card=true;
      }

      suit_ch='c';
      switch(suit_ch){
        case 'c':case 'C':suit=0;break;
        case 'd':case 'D':suit=1;break;
        case 'h':case 'H':suit=2;break;
        case 's':case 'S':suit=3;break;
        default:bad_card=true;
      }

      while((ch=getchar())!='\n')
        if(ch!=' ')
          bad_card=true;
    }
}

void sub_401576(void)
{
    int num_in_rank[13];
    int num_in_suit[4];

    int num_consec=0;
    int rank,suit;

    bool straight,flush,four,three;
    int pairs;

    straight=false;
    flush=false;
    four=false;
    three=false;
    pairs=0;

    for(suit=0;suit<4;suit++)
      if(num_in_suit[suit]==5)
        flush=true;

    rank=0;
    while(num_in_rank[rank]==0)
      rank++;
    for(;rank<13&&num_in_rank[rank]>0;rank++)
      num_consec++;
    if(num_consec==5){
      straight=true;
      return;
    }
    if(num_in_rank[0]&&num_in_rank[1]&&num_in_rank[2]&&num_in_rank[3]&&num_in_rank[12])
      straight=true;

    for(rank=0;rank<13;rank++){
      if(num_in_rank[rank]==4)
        four=true;
      if(num_in_rank[rank]==3)
        three=true;
      if(num_in_rank[rank]==2)
        pairs++;
    }
}

void sub_401668(void)
{
    int m,n,p,t,m1,n1,x,y=5,b[4]={0};
    char ch[10][10],a[26];

    for(m=0;m<10;m++)
      for(n=0;n<10;n++)
        ch[m][n]='.';

    for(m=0;m<26;m++)
      a[m]='A'+m;

    srand((unsigned)time(NULL));

    for(m=0,n=0,p=1,ch[m][n]=a[0];p<26;p++){
      for(t=0;t<4;t++){
        x=rand()%4;
        m1=m,n1=n;
        switch(x){
          case 0:if(m>=0&&(n-1)>=0&&ch[m][n]=='.')
                   ch[m][n-1]=a[p],n=n-1;
                 break;
          case 1:if((m-1)>=0&&n>=0&&ch[m-1][n]=='.')
                   ch[m-1][n]=a[p],m=m-1;
                 break;
          case 2:if(m>=0&&(n+1)<=9&&ch[m][n+1]=='.')
                   ch[m][n+1]=a[p],n=n+1;
                 break;
          case 3:if((m+1)<=9&&n>=0&&ch[m+1][n]=='.')
                   ch[m+1][n]=a[p],m=m+1;
                 break;
        }
        if(m1!=m||n1!=n)
          break;
      }
      if(t==4)
        break;
    }
    for(m=0;m<10;m++)
      for(n=0;n<10;n++){
        printf("%c",ch[m][n]);
        if(n==9)
          printf("\n");
      }

    return 0;
}

void sub_1A14(void)
{
    char walk[10][10];

    int i,j,p=0,q=0,m=0,k=0,t,flag;
    for(i=0;i<10;i++)
        for(j=0;j<10;j++)
        walk [i][j]='.';

        srand(time(0));
/*循环嵌套控制输出*/
        for (i=0,j=0; m<4 && walk [i][j]<'Z';)
        {
           walk [0][0]='A';
            t=rand()%4;
           for(;;i=p,j=q)//每次返回不通前的初始位置
           {
               switch((t+m)%4)
               {
                   case 0 : i++;break;
                   case 1 : i--;break;
                   case 2 : j++;break;
                   case 3 : j--;break;
               }
               m++;
               if(walk [i][j]=='.'&&i>=0&&i<10&&j>=0&&j<10)
                break;//可以走通的条件
           }
           walk[i][j]=walk[p][q]+1;
           p=i;
           q=j;
           m=0;
        }
}

void sub_1BDE(void)
{
    int dollars;
    int *twenties;
    int *tens;
    int *fives;
    int *ones;
    *twenties=dollars/20;
    *tens=(dollars-*twenties*20)/10;
    *fives=(dollars-*twenties*20-*tens*10)/5;
    *ones=dollars-*twenties*20-*tens*10-*fives*5;
}


int sub_401C84(void)
{
    int x,n=1,p,q,y,m;
    char ch;

    x=0;

    while(2*n*n-1<=x)
      n++;

    for(n--,q=n,p=1;p<=2*q-1;p++){
      for(y=n;y<q;y++)
        x++;
      for(m=0;m<2*n-1;m++)
        x++;
      for(y=n;y<q;y++)
        x--;
      if(p<q)
        n--;
      else
        n++;
    }

    return 0;

}

int sub_401D3A(void)
{
    int height,length,width,volume,weight;

    height=8;
    length=12;
    width=10;
    volume=height*length*width;
    weight=(volume+165)/166;

    return 0;
}
int sub_401D8B(void)
{
    int d,i1,i2,i3,i4,i5,j1,j2,j3,j4,j5,s,
    first_sum,second_sum,total;

    printf("Enter the first (single) digit:");
    scanf("%1d",&d);
    printf("Enter first group of five digits:");
    scanf("%1d%1d%1d%1d%1d",&i1,&i2,&i3,&i4,&i5);
    printf("Enter second group of five digits:");
    scanf("%1d%1d%1d%1d%1d",&j1,&j2,&j3,&j4,&j5);
    printf("Enter the last (single) digit:");
    scanf("%f",&s);

    first_sum=d+i2+i4+j1+j3+j5;
    second_sum=i1+i3+i5+j2+j4;
    total=3*first_sum+second_sum;
    printf("Check digit:%d\n",9-((total-1)%10));

    if(9-((total-1)%10)==s)
        printf("VALID");
    else
        printf("NO VALID");
    return 0;
}

int sub_401F23(void)
{
    char a[50];
    char ch,*p,*q,*m;

    printf("Enter a sentence: ");

    for(p=a;(ch=getchar())!='.'&&ch!='?'&&ch!='!';p++)
      *p=ch;

    printf("Reversal of sentence:");

    p--;
    for(q=p;p>=a;p--)
      if(*p==' '||p==a){
        if(p==a)
          printf(" ");
        for(m=p;m<=q;m++)
          printf("%c",*m);
        q=p-1;
    }

    printf("%c",ch);

    return 0;

}

int sub_401FEF(void)
{
    int m,n,p,t,m1,n1,x,y=5,b[4]={0};
    char ch[10][10],a[26];

    for(m=0;m<10;m++)
      for(n=0;n<10;n++)
        ch[m][n]='.';

    for(m=0;m<26;m++)
      a[m]='A'+m;

    srand((unsigned)time(NULL));

    for(m=0,n=0,p=1,ch[m][n]=a[0];p<26;p++){
      for(t=0;t<4;t++){
        x=rand()%4;
        m1=m,n1=n;
        switch(x){
          case 0:if(m>=0&&(n-1)>=0&&ch[m][n]=='.')
                   ch[m][n-1]=a[p],n=n-1;
                 break;
          case 1:if((m-1)>=0&&n>=0&&ch[m-1][n]=='.')
                   ch[m-1][n]=a[p],m=m-1;
                 break;
          case 2:if(m>=0&&(n+1)<=9&&ch[m][n+1]=='.')
                   ch[m][n+1]=a[p],n=n+1;
                 break;
          case 3:if((m+1)<=9&&n>=0&&ch[m+1][n]=='.')
                   ch[m+1][n]=a[p],m=m+1;
                 break;
        }
        if(m1!=m||n1!=n)
          break;
      }
      if(t==4)
        break;
    }


    return 0;
}


void sub_40233D(void)
{

    printf("Please input again:");
    char readin2[12];
    unsigned int len;
    char out[16];
    char result[]="YTFzMF9wV24=";

    memset(readin2,0,12);
    memset(out,0,16);

    scanf("%s",readin2);
    len=strlen(readin2);

    sub_402421(readin2,len,out);

    if(!strcmp(out,result)){
        printf("%s%s",x,readin2);
        exit(0);
    }
    else{
       exit(0);
    }

}

void sub_402421(char *in,unsigned int inlen,char *out)
{
    int s;
	unsigned int i;
	unsigned int j;
	unsigned char c;
	unsigned char l;

	s = 0;
	l = 0;
	for (i = j = 0; i < inlen; i++) {
		c = in[i];

		switch (s) {
		case 0:
			s = 1;
			out[j++] = table[(c >> 2) & 0x3F];
			break;
		case 1:
			s = 2;
			out[j++] = table[((l & 0x3) << 4) | ((c >> 4) & 0xF)];
			break;
		case 2:
			s = 0;
			out[j++] = table[((l & 0xF) << 2) | ((c >> 6) & 0x3)];
			out[j++] = table[c & 0x3F];
			break;
		}
		l = c;
	}

	switch (s) {
	case 1:
		out[j++] = table[(l & 0x3) << 4];
		out[j++] = BASE64_PAD;
		out[j++] = BASE64_PAD;
		break;
	case 2:
		out[j++] = table[(l & 0xF) << 2];
		out[j++] = BASE64_PAD;
		break;
	}

	out[j] = 0;

	return j;
}

int main(void)
{
    char *readin;
    readin=malloc(20);

    memset(readin,0,20);
    memset(x,0,24);

    sub_401340(readin);
    sub_4013BA(readin);

    return 0;
}
