#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def move(a, b):
    return (a[0] + b[0], a[1] + b[1])

def get_grid(grid, pos):
    return grid[pos[0]][pos[1]]


def main(grid):
    letters = []
    pos = (0, grid[0].index('|'))
    direction = (1, 0)
    steps = 0
    while True:
        #print('starting at', pos)

        # check if we need to change direction
        try:
            c = get_grid(grid, pos)
            #print('  > char', c)
        except IndexError as e:
            print('read out of bounds so break', e)
            break

        if c == '+':
            # time to change directions
            possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for ndir in possible_directions:
                # don't go back the way we came
                if move(direction, ndir) == (0, 0):
                    continue
                npos = move(pos, ndir)
                try:
                    nc = get_grid(grid, npos)
                except IndexError:
                    # if out of bounds, ignore
                    continue
                if nc != ' ':
                    direction = ndir
                    #print('changed direction to', ndir, pos)
                    break
            else:
                assert False, "don't know where to go"
        elif c.isalpha():
            letters.append(c)
        elif c == ' ':
            print('hit a space so break')
            break
        elif c == '|' or c == '-':
            pass
        else:
            print('bad char', pos, c)
            assert False

        # move in direction
        pos = move(pos, direction)
        steps += 1


    print('Star 1:', ''.join(letters))
    print('Star 2:', steps)


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

