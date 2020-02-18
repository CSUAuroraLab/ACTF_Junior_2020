from Cryptodome.Cipher import AES
import os
import gmpy2
from flag import FLAG
from Cryptodome.Util.number import *

def main():
    key=os.urandom(2)*16
    iv=os.urandom(16)
    print(bytes_to_long(key)^bytes_to_long(iv))
    aes=AES.new(key,AES.MODE_CBC,iv)
    enc_flag = aes.encrypt(FLAG)
    print(key)
    print(iv)
    print(enc_flag)
#91144196586662942563895769614300232343026691029427747065707381728622849079757
#b'\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81\xc9\x81'
#b'\x87lQbI0\xfc\xe6\xaa\x05P\xb1\x01\xd1pL'
#b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
if __name__=="__main__":
    main()
