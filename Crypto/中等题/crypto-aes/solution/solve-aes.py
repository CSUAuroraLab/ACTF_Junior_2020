from Cryptodome.Cipher import AES
import os
from Cryptodome.Util.number import *
import gmpy2

def main():
    enc_flag=b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
    xornum=91144196586662942563895769614300232343026691029427747065707381728622849079757
    for i in range(0,256):      
        for j in range(0,256):
             num=i*256+j
             subkey=long_to_bytes(num).ljust(2,b'\x00')
             key=subkey*16
             iv=long_to_bytes(bytes_to_long(key)^xornum)[-16:].ljust(16,b'\x00')
             aes=AES.new(key,AES.MODE_CBC,iv)
             flag = aes.decrypt(enc_flag)
             if(flag[:4]==b'actf'):
                 print(flag)

if __name__=="__main__":
    main()
