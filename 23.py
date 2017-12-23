#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def val(R, c):
    try:
        return int(c)
    except ValueError:
        return R[c]

def main(t):
    t = t.splitlines()
    R = defaultdict(int)
    i = 0
    count = 0

    while i < len(t):
        line = t[i].split()
        cmd, args = line[0], line[1:]

        if   cmd == 'set':  R[args[0]]  = val(R, args[1])
        elif cmd == 'sub':  R[args[0]] -= val(R, args[1])
        elif cmd == 'mul':
            R[args[0]] *= val(R, args[1])
            count += 1
        elif cmd == 'jnz':
            if val(R, args[0]) != 0:
                i += val(R, args[1])
                continue
        else:
            assert False, "unknown cmd %s" % cmd

        i += 1

    print(count)

if __name__ == '__main__':
    print('** STAR 1 **')
    t = open('input.txt').read().rstrip()
    main(t)

