#!/usr/bin/python3

import os
from binascii import hexlify, unhexlify
import random
import pysnooper

SZ = 8

def trans_inv(blk):
    res = []
    for k in range(0, SZ, 8):
        a = [0, 0, 0, 0, 0, 0, 0, 0]
        for txt in blk[k:k+8]:
            for i in range(7,-1,-1):
                a[i] *= 2
                a[i] |= txt&1
                txt //= 2
        res += a
    return res

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

def encrypt_block(pt, ks, sbox, sboxi):
    cur = doxor(pt, ks[:SZ])
    cur = [sbox[x] for x in pt]
    cur = trans(cur)
    cur = [sboxi[x] for x in pt]
    cur = doxor(cur, ks[SZ:])
    return cur

def doout(x):
    if len(x) % 16:
        x = (16 - len(x) % 16) * "0" + x
    return x

def doin(x):
    return list(unhexlify(x))
 