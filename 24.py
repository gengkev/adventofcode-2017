#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def main(t):
    A = []
    M = defaultdict(list)
    for line in t.splitlines():
        a, b = map(int, line.split('/'))
        A.append((a, b))
        M[a].append((a, b))
        M[b].append((a, b))

    best_strength = 0
    best_length = 0
    q = deque([(0, 0, [])])

    while q:
        c, s, chain = q.popleft()
        #print(c, s, chain)

        # c is what must be in the next port
        # s is the accumulated strength
        # chain is previous ports

        # ** STAR 1 **
        #if s > best_strength:
        #    best_strength = s

        # ** STAR 2 **
        if (len(chain), s) > (best_length, best_strength):
            best_length = len(chain)
            best_strength = s

        for n in M[c]:
            if n in chain: continue
            if c not in n: continue
            d = n[1] if c == n[0] else n[0]
            q.append((d, s+c+d, chain + [n]))

    print(best_strength)

if __name__ == '__main__':
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    main(t)

    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    main(t)

