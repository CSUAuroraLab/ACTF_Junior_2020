import os
import random
flag="F0uRTy_7w@"
nflag=[]
for i in flag:
    nflag.append(ord(i))
print(nflag)
Lines=[]
for i in range(10):
    res=0
    normal=[random.randint(-127,128) for a in range(10)]
    sr="if("
    for j in range(len(normal)):
        res+=normal[j]*nflag[j]
        if normal[j]>=0:
            sr+="+%s*inp[%d]"%(str(normal[j]),j)
        else:
            sr+="%s*inp[%d]"%(str(normal[j]),j)

    sr+="!=%s) return false;\n"%(str(res))
    Lines.append(sr)

if os.path.exists("array.txt"):
    os.remove("array.txt")

with open("array.txt","w") as f:
    f.writelines(Lines)