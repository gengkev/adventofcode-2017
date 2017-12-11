#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

#A = open('sample.txt').read().split(',')
#A = list(map(int, A))
#SZ = 5

#A = open('input.txt').read().split(',')
#A = list(map(int, A))
#SZ = 256

A = open('input.txt').read().rstrip()
A = [ord(n) for n in A]
A.extend([17, 31, 73, 47, 23])
SZ = 256

B = list(range(SZ))
skip_size = 0
pos = 0

#for rnd in range(1):
for rnd in range(64):
    for length in A:
        #print('length', length, 'pos', pos)
        # swap length elements
        for i in range(0, length//2):
            o = (pos + length - i - 1) % SZ
            i = (i + pos) % SZ
            B[i], B[o] = B[o], B[i]

        # move forward
        pos += length + skip_size
        pos %= SZ
        skip_size += 1
        print(B)

# part 1
print(B[0] + B[1])

# part 2
out = ''
for i in range(16):
    c = 0
    for j in range(16):
        c ^= B[16*i + j]
    out += '%02x' % c

print(out)
