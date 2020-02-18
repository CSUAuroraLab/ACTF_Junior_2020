如果你够厉害，当然你可以直接根据密文来解啦，不过就是两种加密合在一起，不是简单凯撒，所以有一定难度

不过如果你知道生日攻击的话，不妨拿个工具跑一下嘛，那么很快就可以得到结果了，然后写出解题代码

```c
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

```

注意，有个地方的字符不是空格也不是'.'！不过你是可以用winhex或者010editor看到它具体的值的，这个值是7f。