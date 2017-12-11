#!/usr/bin/env python3

t = open('input.txt').read().splitlines()
t = list(map(int, t))

i = 0
c = 0
while True:
    if i < 0 or i >= len(t):
        print('out', i, c)
        break
    newi = i + t[i]
    if t[i] >= 3:
        t[i] -= 1
    else:
        t[i] += 1
    i = newi
    c += 1
