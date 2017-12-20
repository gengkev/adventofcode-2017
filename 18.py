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
    R = defaultdict(int)
    i = 0
    last_sound = 0

    while i < len(t):
        line = t[i].split()
        cmd, args = line[0], line[1:]

        if cmd == 'snd':
            last_sound = val(R, args[0])
        elif cmd == 'set':
            R[args[0]] = val(R, args[1])
        elif cmd == 'add':
            R[args[0]] += val(R, args[1])
        elif cmd == 'mul':
            R[args[0]] *= val(R, args[1])
        elif cmd == 'mod':
            R[args[0]] %= val(R, args[1])
        elif cmd == 'rcv':
            if val(R, args[0]) != 0:
                print('hello', last_sound)
                return
        elif cmd == 'jgz':
            if val(R, args[0]) > 0:
                i += val(R, args[1])
                continue
        else:
            assert False, "unknown cmd %s" % cmd

        i += 1



if __name__ == '__main__':
    # sample input
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    main(t)

    # actual input
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    main(t)

