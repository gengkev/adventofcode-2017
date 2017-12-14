#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

#key = 'flqrgnkx'
key = 'amgozmfv'

def knot_hash(s):
    A = [ord(n) for n in s]
    A.extend([17, 31, 73, 47, 23])
    SZ = 256

    B = list(range(SZ))
    skip_size = 0
    pos = 0

    for rnd in range(64):
        for length in A:
            #print('length', length, 'pos', pos)
            # swap length elements
            for i in range(0, length//2):
                o = (pos + length - i - 1) % SZ
                i = (i + pos) % SZ
                B[i], B[o] = B[o], B[i]

            # move forward
            pos += length + skip_size
            pos %= SZ
            skip_size += 1

    # part 2
    out = []
    for i in range(16):
        c = 0
        for j in range(16):
            c ^= B[16*i + j]
        # star 1
        #out.extend(bin(c).count('1'))
        # star 2
        out.extend([1 if (c & (1 << (7 - i))) else 0 for i in range(8)])
    return out


'''
# star 1
total = 0
for i in range(128):
    s = '{}-{}'.format(key, i)
    total += knot_hash(s)

print(total)
'''

# star 2
grid = []
for i in range(128):
    s = '{}-{}'.format(key, i)
    s = knot_hash(s)
    grid.append(s)

# grid search
def is_good(p):
    x, y = p
    return 0 <= x < 128 and 0 <= y < 128

def get_neighbors(x, y):
    return list(filter(is_good, [
        (x+1,y), (x-1,y), (x,y-1), (x,y+1)
    ]))

marked = defaultdict(lambda: False)
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for n in get_neighbors(x, y):
            if not marked[n] and grid[n[0]][n[1]]:
                marked[n] = True
                q.append(n)

total = 0
for i in range(128):
    for j in range(128):
        if not marked[(i, j)] and grid[i][j]:
            total += 1
            print(i, j)
            bfs(i, j)

print(total)
