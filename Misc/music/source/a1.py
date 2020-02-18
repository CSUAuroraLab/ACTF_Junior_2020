import struct
import os


def turnxor(filename, xorbyte):
    with open(filename, 'rb') as file:
        with open(filename+".m4a", "wb") as outfile:
            all = file.read()
            for b in all:
                b = struct.pack('!B', b)
                outfile.write(bxor(b, xorbyte))


def bxor(b1, b2):  # use xor for bytes
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)


def main():
    xorbyte = b'\xa1'
    filename = 'vip.m4a.m4a'
    turnxor(filename, xorbyte)


if __name__ == "__main__":
    main()
