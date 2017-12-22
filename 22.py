#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

CLEAN = 0
INFECT = 1
WEAK = 2
FLAG = 3

def move(a, b):
    return (a[0] + b[0], a[1] + b[1])

def turn(d):
    return (d[1], -d[0])

def main(t, iters):
    grid = defaultdict(bool)
    N = len(t)
    for i in range(N):
        for j in range(N):
            grid[(i - N//2, j - N//2)] = (
                    CLEAN if t[i][j] == '.' else INFECT)

    pos = (0, 0)
    direc = (-1, 0)
    count = 0
    for it in range(iters):
        if grid[pos] == INFECT:
            direc = turn(direc)
            grid[pos] = CLEAN
        elif grid[pos] == CLEAN:
            direc = turn(turn(turn(direc)))
            grid[pos] = INFECT
            count += 1
        else:
            assert False
        pos = move(pos, direc)
        #print(it)
        #print(pos, direc)

    if iters <= 100:
        for i in range(-5, 6):
            for j in range(-5, 6):
                if pos == (i, j):
                    print('x', end='')
                else:
                    print('.#'[grid[(i, j)]], end='')
            print()

    print('iters', iters, 'count', count)


def main2(t, iters):
    grid = defaultdict(bool)
    N = len(t)
    for i in range(N):
        for j in range(N):
            grid[(i - N//2, j - N//2)] = (
                    CLEAN if t[i][j] == '.' else INFECT)

    pos = (0, 0)
    direc = (-1, 0)
    count = 0
    for it in range(iters):
        if grid[pos] == INFECT:
            direc = turn(direc)
            grid[pos] = FLAG
        elif grid[pos] == CLEAN:
            direc = turn(turn(turn(direc)))
            grid[pos] = WEAK
        elif grid[pos] == WEAK:
            grid[pos] = INFECT
            count += 1
        elif grid[pos] == FLAG:
            direc = turn(turn(direc))
            grid[pos] = CLEAN
        else:
            assert False
        pos = move(pos, direc)

    print('iters', iters, 'count', count)

if __name__ == '__main__':
    print('** STAR 1 **')
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    main(t, 7)
    main(t, 70)
    main(t, 10000)

    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    main(t, 10000)

    print('\n** STAR 2 **')
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    main2(t, 100)
    main2(t, 10000000)

    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    main2(t, 10000000)
