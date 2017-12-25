#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

M = {
        'A': [(1, 1, 'B'), (0, -1, 'E')],
        'B': [(1, -1, 'C'), (0, 1, 'A')],
        'C': [(1, -1, 'D'), (0, 1, 'C')],
        'D': [(1, -1, 'E'), (0, -1, 'F')],
        'E': [(1, -1, 'A'), (1, -1, 'C')],
        'F': [(1, -1, 'E'), (1, 1, 'A')],
}

def step(tape, pos, state):
    val = tape[pos]
    wr, mv, cont = M[state][val]
    tape[pos] = wr
    return (pos + mv, cont)

def main(iters):
    tape = defaultdict(int)
    pos = 0
    state = 'A'

    for i in range(iters):
        pos, state = step(tape, pos, state)

    c = Counter(tape.values())
    print(c[1])

if __name__ == '__main__':
    main(12208951)

