#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from heapq import heappop, heappush

#lines = open('sample.txt').read().splitlines()
lines = open('input.txt').read().splitlines()

R = defaultdict(int)
lol = 0

for line in lines:
    '''
    r1, op, val, _, cond_r, cond_cmp, cond_val = line.split()
    val, cond_val = int(val), int(cond_val)
    if cond_cmp == '>':
        c = R[cond_r] > cond_val
    elif cond_cmp == '<':
        c = R[cond_r] < cond_val
    elif cond_cmp == '>=':
        c = R[cond_r] >= cond_val
    elif cond_cmp == '<=':
        c = R[cond_r] <= cond_val
    elif cond_cmp == '==':
        c = R[cond_r] == cond_val
    elif cond_cmp == '!=':
        c = R[cond_r] != cond_val
    else:
        assert False
    '''

    r1, op, val, _, cond = line.split(maxsplit=4)
    val = int(val)
    c = eval(cond, {}, R)

    if c:
        if op == 'inc':
            R[r1] += val
        elif op == 'dec':
            R[r1] -= val
        else:
            assert False

    lol = max(lol, max(R.values()))

print(R)
print(max(R.values()))
print('lol', lol)
