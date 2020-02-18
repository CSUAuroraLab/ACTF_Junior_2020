from z3 import *
inp = [BitVec("inp_%d"%i,8) for i in range(10)]
s=Solver()
s.add(-85 * inp[8] + 58 * inp[7] + 97 * inp[6] + inp[5] + -45 * inp[4] + 84 * inp[3] + 95 * inp[0] - 20 * inp[1] + 12 * inp[2] == 12613)
s.add(30 * inp[9] + -70 * inp[8] + -122 * inp[6] + -81 * inp[5] + -66 * inp[4] + -115 * inp[3] + -41 * inp[2] + -86 * inp[1] - 15 * inp[0] - 30 * inp[7] == -54400)
s.add(-103 * inp[9] + 120 * inp[7] + 108 * inp[5] + 48 * inp[3] + -89 * inp[2] + 78 * inp[1] - 41 * inp[0] + 31 * inp[4] - (inp[6] << 6) - 120 * inp[8] == -10283)
s.add(71 * inp[6] + (inp[5] << 7) + 99 * inp[4] + -111 * inp[2] + 85 * inp[1] + 79 * inp[0] - 30 * inp[3] - 119 * inp[7] + 48 * inp[8] - 16 * inp[9] == 22855)
s.add(5 * inp[9] + 23 * inp[8] + 122 * inp[7] + -19 * inp[6] + 99 * inp[5] + -117 * inp[4] + -69 * inp[2] + 22 * inp[1] - 98 * inp[0] + 10 * inp[3] == -2944)
s.add(-54 * inp[9] + -23 * inp[7] + -82 * inp[2] + -85 * inp[0] + 124 * inp[1] - 11 * inp[3] - 8 * inp[4] - 60 * inp[5] + 95 * inp[6] + 100 * inp[8] == -2222)
s.add(-83 * inp[9] + -111 * inp[5] + -57 * inp[0] + 41 * inp[1] + 73 * inp[2] - 18 * inp[3] + 26 * inp[4] + 16 * inp[6] + 77 * inp[7] - 63 * inp[8] == -13258)
s.add(81 * inp[9] + -48 * inp[8] + 66 * inp[7] + -104 * inp[6] + -121 * inp[5] + 95 * inp[4] + 85 * inp[3] + 60 * inp[2] + -85 * inp[0] + 80 * inp[1] == -1559)
s.add(101 * inp[9] + -85 * inp[8] + 7 * inp[6] + 117 * inp[5] + -83 * inp[4] + -101 * inp[3] + 90 * inp[2] + -28 * inp[1] + 18 * inp[0] - inp[7] == 6308)
s.add(99 * inp[9] + -28 * inp[8] + 5 * inp[7] + 93 * inp[6] + -18 * inp[5] + -127 * inp[4] + 6 * inp[3] + -9 * inp[2] + -93 * inp[1] + 58 * inp[0] == -1697)

if s.check() !=sat:
    print("unsat")
else:
    m=s.model()
    print(m)
    print(repr("".join([chr(m[inp[i]].as_long())for i in range(10)])))