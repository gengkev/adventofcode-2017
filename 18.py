#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from functools import reduce

def val(R, c):
    try:
        return int(c)
    except ValueError:
        return R[c]

def main(t):
    R = defaultdict(int)
    i = 0
    last_sound = 0

    while i < len(t):
        line = t[i].split()
        cmd, args = line[0], line[1:]

        if cmd == 'snd':
            last_sound = val(R, args[0])
        elif cmd == 'set':  R[args[0]]  = val(R, args[1])
        elif cmd == 'add':  R[args[0]] += val(R, args[1])
        elif cmd == 'mul':  R[args[0]] *= val(R, args[1])
        elif cmd == 'mod':  R[args[0]] %= val(R, args[1])
        elif cmd == 'rcv':
            if val(R, args[0]) != 0:
                print('last_sound:', last_sound)
                return
        elif cmd == 'jgz':
            if val(R, args[0]) > 0:
                i += val(R, args[1])
                continue
        else:
            assert False, "unknown cmd %s" % cmd

        i += 1

    print('exiting main without rcv')


def main2(t):
    R1 = defaultdict(int)
    R2 = defaultdict(int)
    i1 = 0
    i2 = 0
    msg1 = deque()  # sent to 1
    msg2 = deque()  # sent to 2
    finished1 = False
    finished2 = False
    values_sent = 0

    # initialize p variable
    R1['p'] = 0
    R2['p'] = 1

    # check for termination
    lol = 0

    while not(finished1 and finished2):
        #print('entering main loop')
        if not msg1 and not msg2:
            lol += 1
            if lol > 10:
                print('breaking on probable deadlock')
                break

        # execute program 1
        while i1 < len(t):
            line = t[i1].split()
            cmd, args = line[0], line[1:]

            if cmd == 'snd':
                msg2.append(val(R1, args[0]))
            elif cmd == 'set': R1[args[0]]  = val(R1, args[1])
            elif cmd == 'add': R1[args[0]] += val(R1, args[1])
            elif cmd == 'mul': R1[args[0]] *= val(R1, args[1])
            elif cmd == 'mod': R1[args[0]] %= val(R1, args[1])
            elif cmd == 'rcv':
                if msg1: R1[args[0]] = msg1.popleft()
                else:    break
            elif cmd == 'jgz':
                if val(R1, args[0]) > 0:
                    i1 += val(R1, args[1])
                    continue
            else:
                assert False, "unknown cmd %s" % cmd
            i1 += 1
        else:
            print('finished 1')
            finished1 = True

        # execute program 2
        while i2 < len(t):
            line = t[i2].split()
            cmd, args = line[0], line[1:]

            if cmd == 'snd':
                msg1.append(val(R2, args[0]))
                values_sent += 1
            elif cmd == 'set': R2[args[0]]  = val(R2, args[1])
            elif cmd == 'add': R2[args[0]] += val(R2, args[1])
            elif cmd == 'mul': R2[args[0]] *= val(R2, args[1])
            elif cmd == 'mod': R2[args[0]] %= val(R2, args[1])
            elif cmd == 'rcv':
                if msg2: R2[args[0]] = msg2.popleft()
                else:    break
            elif cmd == 'jgz':
                if val(R2, args[0]) > 0:
                    i2 += val(R2, args[1])
                    continue
            else:
                assert False, "unknown cmd %s" % cmd
            i2 += 1
        else:
            print('finished 2')
            finished2 = True

    print('exited loop, finished:', finished1, finished2)
    print('values_sent:', values_sent)


if __name__ == '__main__':
    # sample input
    print('Sample input:')
    t = open('sample.txt').read().rstrip()
    t = t.splitlines()
    print('> Star 1:')
    main(t)
    print('> Star 2:')
    main2(t)

    # actual input
    print('\nActual input:')
    t = open('input.txt').read().rstrip()
    t = t.splitlines()
    print('> Star 1:')
    main(t)
    print('> Star 2:')
    main2(t)

