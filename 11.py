#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

t = open('sample.txt').read()
t = open('input.txt').read()

A = t.rstrip().split(',')

x = 0
y = 0

M = {
    'n': (0, 2),
    'e': (2, 0),
    'w': (-2, 0),
    's': (0, -2),
    'ne': (1, 1),
    'nw': (-1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

m = 0

for n in A:
    d = M[n]
    x += d[0]
    y += d[1]
    m = max(m, ((abs(x) + abs(y))) // 2)

# star 1
print(x, y)
print((abs(x) + abs(y)) // 2)

# star 2
print(m)

