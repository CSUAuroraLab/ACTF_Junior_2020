import os
from encrypt import doxor
from Crypto.Util.number import long_to_bytes, bytes_to_long

sbox = [155, 104, 202, 19, 157, 5, 179, 28, 234, 199, 42, 7, 201, 186, 96, 183, 140, 27, 218, 220, 45, 125, 57, 81, 137, 226, 212, 160, 100, 237, 242, 69, 92, 79, 130, 173, 189, 117, 49, 181, 41, 164, 102, 225, 0, 141, 195, 142, 62, 174, 180, 109, 122, 53, 187, 4, 168, 240, 80, 184, 227, 228, 230, 44, 15, 128, 167, 175, 48, 26, 111, 76, 118, 91, 50, 165, 224, 119, 61, 231, 144, 103, 219, 106, 207, 170, 54, 10, 156, 190, 35, 148, 55, 66, 75, 93, 222, 22, 138, 203, 87, 90, 68, 77, 178, 38, 52, 71, 116, 33, 115, 112, 209, 24, 133, 58, 161, 59, 94, 105, 213, 196, 129, 8, 215, 46, 107, 176, 40, 64, 236, 214, 6, 13, 31, 208, 114, 245, 193, 131, 253, 65, 151, 74, 1, 51, 36, 63, 88, 83, 239, 166, 16, 95, 169, 163, 134, 162, 32, 39, 126, 2, 198, 98, 192, 20, 72, 182, 172, 136, 127, 171, 110, 135, 204, 210, 251, 252, 158, 254, 85, 82, 143, 206, 223, 25, 97, 120, 200, 249, 238, 3, 47, 233, 30, 188, 73, 9, 123, 248, 232, 159, 147, 149, 132, 194, 229, 241, 145, 216, 150, 185, 17, 21, 43, 247, 99, 250, 154, 67, 211, 14, 255, 146, 84, 86, 78, 153, 23, 18, 12, 217, 56, 243, 152, 60, 205, 11, 246, 70, 34, 113, 121, 29, 89, 197, 108, 177, 221, 244, 37, 124, 191, 139, 101, 235]

def enum_key(pos):
    a = []
    for i in range(0,255):
        s = "\0" * pos + chr(i) + "\0" * (7-pos)
        a.append((map(ord, s), i))
    return a

def check(num, bitmask):
    a = 0
    while bitmask > 0:
        if bitmask & 1 == 1:
            a ^= num & 1
        bitmask //= 2
        num //= 2
    return a == 0

def check_key(text_pairs, key, mask):
    cnt = 0
    for text_pair in text_pairs:
        (plain, cipher) = text_pair
        mid = cipher ^ key
        mid = sbox[mid] 
        if check((plain << 8) | mid, mask):
            cnt += 1

    return cnt

if __name__ == "__main__":
    f = open("ciphertext", "r")
    pairs = f.readlines()[1:]
    pairs = list(map(lambda x:x.replace("\n", "").split(" "), pairs))
    pairs = list(map(lambda x:(x[0][0:2], x[1][10:12]), pairs))
    print(type(pairs[0]),type(pairs[0][0]))
    pairs = list(map(lambda x:(int(x[0], 16), int(x[1], 16)), pairs))
    a = []
    for key in range(256):
        a.append((key, check_key(pairs, key, 0b1100101010000000)-(len(pairs)//2)))
    a.sort(key=lambda x:x[1])
    print(a)
        
