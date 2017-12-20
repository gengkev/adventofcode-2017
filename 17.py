#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def main(N, spins):
    q = deque()
    q.append(0)
    for i in range(1, spins+1):
        for j in range(N % len(q)):
            q.append(q.popleft())
        q.append(i)
        if i % 100000 == 0:
            print('i', i)
    print('> star 1', q[0])
    print('> star 2', q[q.index(0) + 1])

def main2(N, spins):
    pos = 0
    after_zero = -1
    for i in range(1, spins+1):
        pos = (pos + N) % i
        if pos == 0:
            after_zero = i
        pos += 1
    print('> star 2', after_zero)


if __name__ == '__main__':
    # sample input
    print('sample input')
    main(3, 2017)

    # main input
    print('main input, star 1')
    main(354, 2017)

    print('main input, star 2')
    #main(354, 50000000)
    main2(354, 50000000)

