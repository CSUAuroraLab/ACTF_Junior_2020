import os
import random

array = []
for i in range(0, 600):
    array.append(0)

for i in range(0, 500):
    tmp = random.randint(0, 500)
    while (array[tmp] == 1):
        tmp = random.randint(0, 500)

    array[tmp] = 1
    f = open('D:\\flag\\' + str(i) + '.txt', 'w')
    if (tmp == 208):
        f.write('flag就在这里哦，找找看吧ADS:)')
        os.system('echo ACTF{AAAds_nntfs_ffunn?} > d:\\flag\\' + str(i) + '.txt:flag.txt')
    else:
        f.write('flag is not here')



