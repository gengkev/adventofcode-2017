#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce


def add_vec(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def dist(a):
    return sum(map(abs, a))

def parse_vec(sub):
    sub = sub.lstrip('<').rstrip('>')
    return tuple(int(n.strip()) for n in sub.split(','))

def main(t):
    particles = []
    for line in t:
        line = line.split(', ')
        obj = [parse_vec(line[i].split('=')[1]) for i in range(3)]
        obj.append(False)
        particles.append(obj)

    for t in range(1000):
        coll = Counter([p[0] for p in particles if not p[3]])
        temp = set()
        for pos in coll:
            if coll[pos] >= 2:
                temp.add(pos)

        for i, p in enumerate(particles):
            if p[0] in temp:
                p[3] = True
            p[1] = add_vec(p[1], p[2])  # v += a
            p[0] = add_vec(p[0], p[1])  # p += v


    sd = -1
    for i, p in enumerate(particles):
        d = dist(p[0])
        if sd == -1 or d < sd:
            si, sd = i, d

    print('Star 1:', si)
    print('Star 2:', sum(0 if p[3] else 1 for p in particles))


if __name__ == '__main__':
    # sample input
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    main(t)

    # actual input
    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    main(t)

