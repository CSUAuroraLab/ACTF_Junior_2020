'''
python2.7
生成start.py所用的明文
'''
import base64

f = open('D:\\ming.txt')
f2 = open('D:\\1.txt', 'wb')
for line in f.readlines():
    res = base64.b64encode(line)
    f2.write(res)
    f2.write('\n')