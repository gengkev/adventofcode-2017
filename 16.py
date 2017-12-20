#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def main(t, N, num_dances):
    seen = {}
    A = [chr(ord('a') + n) for n in range(N)]
    lines = t.split(',')

    d = 0
    found_cycle = False
    while d < num_dances:
        A2 = tuple(A)
        if not found_cycle and A2 in seen:
            cycle_len = d - seen[A2]
            print('found cycle: {} - {} = {}'.format(
                d, seen[A2], cycle_len))
            num_dances = d + (num_dances % cycle_len)
            found_cycle = True
        seen[A2] = d

        for line in lines:
            if line[0] == 's':
                n = int(line[1:])
                A = A[-n:] + A[:-n]
            elif line[0] == 'x':
                a, b = line[1:].split('/')
                a = int(a); b = int(b)
                A[a], A[b] = A[b], A[a]
            elif line[0] == 'p':
                a, b = line[1:].split('/')
                a = A.index(a); b = A.index(b)
                A[a], A[b] = A[b], A[a]
            else:
                assert False
        d += 1

    print('Result from main:', ''.join(A))


def permutation_exp(X, e):
    N = len(X)
    Y = [i for i in range(N)]
    while e > 1:
        if e % 2 == 1:
            Y = [X[Y[i]] for i in range(N)]  # y = x * y
        X = [X[X[i]] for i in range(N)]  # x = x * x
        e = e // 2
    return [X[Y[i]] for i in range(N)]  # x * y

def to_chars(A):
    return ''.join(chr(ord('a') + n) for n in A)

def main2(t, N, num_dances):
    A = [i for i in range(N)]
    P = [i for i in range(N)]
    lines = t.split(',')

    # run one iteration
    for line in lines:
        if line[0] == 's':
            n = int(line[1:])
            A = A[-n:] + A[:-n]
        elif line[0] == 'x':
            a, b = line[1:].split('/')
            a = int(a); b = int(b)
            A[a], A[b] = A[b], A[a]
        elif line[0] == 'p':
            a, b = line[1:].split('/')
            a = ord(a) - ord('a'); b = ord(b) - ord('a')
            a = P.index(a); b = P.index(b)
            P[a], P[b] = P[b], P[a]
        else:
            assert False

    # exponentiation by squaring
    Ae = permutation_exp(A, num_dances)
    Pe = permutation_exp(P, num_dances)
    #print('Ae', Ae)
    #print('Pe', Pe)

    B = Ae[:]
    for i, n in enumerate(Pe):
        pos = Ae.index(i)
        B[pos] = n
    #print('B', B)
    print('Result from main2:', to_chars(B))


if __name__ == '__main__':
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    print('> Star 1:')
    main(t, 5, 1)
    main2(t, 5, 1)
    print('> Star 2:')
    main(t, 5, 2)
    main2(t, 5, 2)

    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    print('> Star 1:')
    main(t, 16, 1)
    main2(t, 16, 1)
    print('> Star 2:')
    main(t, 16, 1000000000)
    main2(t, 16, 1000000000)

