	首先稍微调试一下就能很快发现这个题目的本质是迷宫。但是不像普通的走一步就是一格的迷宫，这个迷宫会向一个方向一直走到遇见墙壁，然后根据用户的输入来决定转向哪个方向。

有经验的朋友通过研究判断函数的工作流程也能够明白，这个组成迷宫的字符数组是256的大小，而迷宫的宽是16，故迷宫的大小是16*16。我们依此可以画出整个迷宫。故整个迷宫如下：

```
____#_______####
___##___OO______
________OO_PP___
___L_OO_OO_PP___
___L_OO_OO_P____
__LL_OO____P____
_____OO____P____
#_______________
____________#___
______MMM___#___
_______MMM____EE
___0_M_M_M____E_
______________EE
TTTI_M_M_M____E_
_T_I_M_M_M____E_
_T_I_M_M_M!___EE
```

为了显示方便我将其中为0的地块以`_`代表。结合研究流程时我们可以发现，这个迷宫当中W是上，M是下，J是左，E是右。只要首先确定应该往下走，就能顺理成章地得到整个flag。

所以flag是 `actf{MEWEMEWJMEWJM}`

当然如果在了解到该flag的组成只有4个字母时我们也可以直接用穷举暴力来解。4^12=16,777,216,写一个脚本应该还是能跑出来的。
