import os
def oper(a,line):
    with open("char"+str(a),"a") as f:
        f.write(line)
lines=[]
with open("origin.txt","r") as f:
    lines=f.readlines()
for i in range(12):
    if os.path.exists("char"+str(i)):
        os.remove("char"+str(i))
for i in range(3000//12):
    for j in range(12):
        oper(j,lines[i*12+j])