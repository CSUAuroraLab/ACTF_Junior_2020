#！/bin/python3
#不过首先先测试一下能不能用吧
import random
import os

sth=[54, 11, 49, 107, 79, 104, 114, 84, 66, 24, 124, 50]
flag=[0x62,0x30,0x4e,0x66,0x7c,0x52,0x65,0x5f,0x4c,0x69,0x54,0x21]

def out_to_char(outlist):
    for tmp in outlist:
        print(chr(tmp),end="")
    print()
def lines(a,b,special):
    with open("run.txt","a") as f:
        if  special==0:
            f.write("inp[%d]++;\n" % (a))

        elif special==1 :
            f.write("inp[%d]^=inp[%d];\n"%(a,b))
        else:
            f.write("inp[%d]^=%du;\n" % (a, b))

            
change1=flag[:]
count=[50 for x in range(12)]
mark=0
if os.path.exists("run.txt"):
    os.remove("run.txt")
stp=-2
stp1=-2
for i in range(3000):
    #算了不要想太多，直接让它暴力跑吧。
    choice=random.randint(0,5)
    tmp1=i%12
    if choice==0:
        if change1[tmp1]==127 or stp1==i-1:
            choice+=2
        else:
            lines(tmp1,0,0)
            change1[tmp1]+=1
            stp=i
    elif choice == 1:
        if tmp1==0 or stp==i-1:
            choice+=1
        else:
            tmp2=random.randint(0,tmp1-1)
            change1[tmp1]^=change1[tmp2]
            lines(tmp1,tmp2,choice)
            stp1=i
    if choice>1:
        tmp2=random.randint(1,127)
        change1[tmp1]^=tmp2
        lines(tmp1,tmp2,choice)

print(change1)