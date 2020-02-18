#!/usr/bin/python3

from typing import List, Tuple
from tqdm import tqdm
# import test
# import pysnooper
from util import doxor, doin, trans_inv, SZ
from binascii import unhexlify
from codecs import encode
import random
import pwn

def maskeq(a: int, b: int) -> bool:
    c: int = 0
    while b > 0:
        if b&1:
            c ^= (a&1)
        b //= 2
        a //= 2
    return c==0

def LAT(sbox: List[int]) -> List[List[int]]:
    count = []
    for row in tqdm(range(256), desc="compute LAT"):
        count.append([])
        for col in range(256):
            cnt = -128
            bitmask = (row << 8) | col
            for i in range(256):
                if maskeq((i << 8) | sbox[i],  bitmask):
                    cnt += 1
            count[row].append(abs(cnt))
        count[row].append(row)
    return count

def check(num: int, bitmask: int) -> bool:
    a = 0
    while bitmask > 0:
        if bitmask & 1 == 1:
            a ^= num & 1
        bitmask //= 2
        num //= 2
    return a == 0

def check_key(text_pairs: List[Tuple[int, int]], sbox: List[int], key: int, mask: int) -> int:
    cnt = 0
    for text_pair in text_pairs:
        (plain, cipher) = text_pair
        mid = cipher ^ key
        mid = sbox[mid] 
        if check((plain << 8) | mid, mask):
            cnt += 1
    return cnt

# @pysnooper.snoop()
def decrypt(sbox, sboxi, ct, k):
    pt = ''
    for i in range(0, len(ct), SZ):
        res = decrypt_block(sbox, sboxi, ct[i:i+SZ], k)
        pt += ''.join(map(chr, res))
    return pt

def decrypt_block(sbox, sboxi, pt, ks):
    cur = doxor(pt, ks[SZ:])
    cur = list(map(lambda x:sbox[x], cur))
    cur = trans_inv(cur)
    cur = list(map(lambda x:sboxi[x], cur))
    cur = doxor(cur, ks[:SZ])
    return cur

def compute_frontkey(sbox, sboxi, pt: List[int], ct: List[int], lastkey: List[int]) -> List[int]:
    cur = doxor(ct, lastkey)
    cur = list(map(lambda x:sbox[x], cur))
    cur = trans_inv(cur)
    cur = list(map(lambda x:sboxi[x], cur))
    return doxor(cur, pt)

def doin(x):
    return list(unhexlify(x))

def doout(x):
    tmp = ''.join(map(chr, x))
    return (encode(tmp.encode(), 'hex')).decode()

def main():
    # pwn.context.log_level = "DEBUG"
    # io = pwn.remote("192.168.16.128", 9999)
    io = pwn.process("../src/server.py")
    sbox_str = io.readline()
    sbox: List[int] = list(map(int, sbox_str[1:-2].split(b",")))
    sboxi: List[int] = []
    for i in range(256):
        sboxi.append(sbox.index(i))
    # print(sbox)
    flag_ct = doin(io.readline().strip())
    # print(flag_ct)
    pts: List[str] = []#test.pt
    cts: List[str] = []#test.ct
    for i in tqdm(range(2048), desc="collect plaintext-cipher paits"):
        pt = random.randint(0, (1<<64)-1)
        pt = "{:016x}".format(pt)
        io.sendline(pt)
        ct = io.readline().strip()
        pts.append(pt)
        cts.append(ct)
    # print("pt0: {}".format(pts[0]))
    # print("ct0: {}".format(cts[0]))
    lat = LAT(sbox)
    ptx = list(map(lambda x:(int(x[0:2], 16)), pts))
    key = []
    for i in range(8):
        ctx = list(map(lambda x:(int(x[i*2:i*2+2], 16)), cts))
        lat.sort(key=lambda x:x[(1<<(7-i))], reverse=True)
        # print("{}th byte is for LT{}".format(i, lat[0][256]))
        res = []
        for k in tqdm(range(256), desc="compute {}th byte of key".format(i+9)):
            res.append((k, abs(check_key(zip(ptx, ctx), sbox, k, (lat[0][256]<<8) |0b10000000)-(len(pts)//2))))
        res.sort(key=lambda x: x[1], reverse=True)
        key.append(res[0][0])
        # print(res)
        # print("{}th key is {:02x}".format(i+9, res[0][0]))
    pt1 = doin(pts[0])
    ct1 = doin(cts[0])
    key = compute_frontkey(sbox, sboxi, pt1, ct1, key) + key
    print("computed key: {}".format(doout(key)))
    # print(key)
    ans = decrypt(sbox, sboxi, flag_ct, key)
    if ord(ans[-1]) < 9:
        ans = ans[:-ord(ans[-1])]
    print(ans)

if __name__ == "__main__":
    main()
