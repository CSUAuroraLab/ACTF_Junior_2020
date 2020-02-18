#!/usr/bin/python3

import os
from binascii import hexlify, unhexlify
import Crypto.Random.random as random
from secret import flag

SZ = 8

sbox = list(range(256))
random.shuffle(sbox)
sboxi = []
for i in range(256):
    sboxi.append(sbox.index(i))

def doxor(l1,l2):
    return [x[0]^x[1] for x in zip(l1,l2)]

def trans(blk):
    res = []
    for k in range(0, SZ, 8):
        bits = [bin(x)[2:].rjust(8,'0') for x in blk[k:k+8]]
        for i in range(8):
            res.append(int(''.join([x[i] for x in bits]),2))
    return res

def encrypt_block(pt, ks):
    cur = doxor(pt, ks[:SZ])
    cur = [sbox[x] for x in cur]
    cur = trans(cur)
    cur = [sboxi[x] for x in cur]
    cur = doxor(cur, ks[SZ:])
    return cur

def encrypt(pt, k):
    x = 0 if len(pt)%SZ==0 else (SZ-len(pt)%SZ)
    pt += [x]*x
    ct = ''
    for i in range(0, len(pt), SZ):
        res = encrypt_block([x for x in pt[i:i+SZ]], k)
        ct += ''.join(["{:02x}".format(xx) for xx in res])
    return ct

def doout(x):
    if len(x) % 16:
        x = (16 - len(x) % 16) * "0" + x
    return x

def doin(x):
    return list(unhexlify(x))

def genkeys():
    return list(os.urandom(2*SZ))

if __name__ == "__main__":
    print(sbox)
    key = genkeys()
    ct = encrypt(flag, key)
    print(ct)
    while True:
        pt = doin(input())
        print(doout(encrypt(pt, key)))