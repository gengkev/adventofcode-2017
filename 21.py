#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def parse_pattern(line):
    a, b = line.split(' => ')
    return (list(map(list, a.split('/'))),
            list(map(list, b.split('/'))))

def flip(grid):
    return list(reversed(grid))

def rotate(grid):
    N = len(grid)
    return [[grid[N-1-j][i] for j in range(N)] for i in range(N)]

def grid_tuple(grid):
    return tuple(tuple(line) for line in grid)

def main(t, iters):
    MAP = {}
    for line in t:
        a, b = parse_pattern(line)
        a0 = a
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        assert a == a0
        a = flip(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        MAP[grid_tuple(a)] = b; a = rotate(a)
        assert a == flip(a0)

    print('done parsing rules')

    grid = [list('.#.'), list('..#'), list('###')]
    for i in range(iters):
        print('iteration', i)
        N = len(grid)
        if N % 2 == 0:
            M = (N//2) * 3
            out = [[0 for j in range(M)] for i in range(M)]
            squares = []
            for i in range(0, N, 2):
                for j in range(0, N, 2):
                    tiny = [
                            [grid[i][j], grid[i][j+1]],
                            [grid[i+1][j], grid[i+1][j+1]]
                    ]
                    large = MAP[grid_tuple(tiny)]
                    ni = (i//2)*3
                    nj = (j//2)*3
                    for ii in range(3):
                        for jj in range(3):
                            out[ni+ii][nj+jj] = large[ii][jj]
            grid = out
        else:
            assert N % 3 == 0
            M = (N//3) * 4
            out = [[0 for j in range(M)] for i in range(M)]
            squares = []
            for i in range(0, N, 3):
                for j in range(0, N, 3):
                    tiny = [
                            [grid[i][j], grid[i][j+1], grid[i][j+2]],
                            [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]],
                            [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]],
                    ]
                    large = MAP[grid_tuple(tiny)]
                    ni = (i//3)*4
                    nj = (j//3)*4
                    for ii in range(4):
                        for jj in range(4):
                            out[ni+ii][nj+jj] = large[ii][jj]
            grid = out

    print(sum(line.count('#') for line in grid))


if __name__ == '__main__':
    # sample input
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    main(t, 2)

    # actual input
    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    main(t, 5)
    main(t, 18)

