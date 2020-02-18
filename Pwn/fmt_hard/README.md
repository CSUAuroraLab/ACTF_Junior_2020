### 												README

#### 出题思路及学习方向

* 思路来源于TWCTF的neighbor。
* 主要目的是格式化字符串漏洞利用方式
* 难点在开启了RELRO保护，got不能覆写。
* 关键点在于学会栈迁移、学会修改不在栈上的地址。
* 这里就是利用stack上的残留的信息，先泄露libc，再利用栈迁移改写malloc_hook内容为one_gadget，printf大块的内容时触发malloc即可。