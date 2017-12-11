#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from heapq import heappop, heappush

lines = open('input.txt').read().splitlines()
with_children = []
no_children = []

cand = set()
children = set()

M = {}

for line in lines:
    line = line.split()
    cand.add(line[0])
    if len(line) > 2:  # has children
        M[line[0]] = (int(line[1].strip('()')), [n.rstrip(',') for n in line[3:]])
        for z in line[3:]:
            children.add(z.rstrip(','))
    else:  # no children
        M[line[0]] = (int(line[1].strip('()')), [])
        no_children.append(line)


root = list(cand - children)[0]
print('root is', root)

def check(r):
    total = []
    for c in M[r][1]:
        total.append(check(c))
    if len(total) > 0 and not all(n == total[0] for n in total):
        ct = Counter(total)
        for k in ct:
            if ct[k] == 1:
                yay = M[r][1][total.index(k)]
                break

        print('blah', r, M[r], total)
        print('detail', yay, M[yay])

    return M[r][0] + sum(total)

check(root)

print(M['vrgxe'])
