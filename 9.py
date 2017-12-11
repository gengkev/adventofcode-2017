#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from heapq import heappop, heappush

#line = open('sample.txt').read()
line = open('input.txt').read()

scores = [0]
level = 0
is_garbage = False

total_score = 0

i = 0
count = 0
while i < len(line):
    c = line[i]
    if is_garbage:
        if c == '>':
            is_garbage = False
        elif c == '!':
            i += 1
        else:
            count += 1

    else:
        if c == '{':
            level += 1
            #if len(scores) <= level:
            #    scores.append(0)
            #assert scores[level] == 0
        elif c == '<':
            is_garbage = True
        elif c == '}':
            '''
            print('end', level, scores[level])
            level -= 1
            scores[level+1] += 1
            print('score', scores[level+1])
            total_score += scores[level+1]

            scores[level] += scores[level+1]
            scores[level+1] = 0
            '''
            total_score += level
            level -= 1

    i += 1

print('end level', level)
#print('score', scores[0])
print('score', total_score)
print('count', count)
