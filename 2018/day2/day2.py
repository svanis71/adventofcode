#!/usr/bin/env python3
from collections import defaultdict


class Day2:
    def __init__(self):
        with open('day2/in.txt') as f:
            content = f.readlines()
        self.rows = [x.strip() for x in content]

    def part1(self):
        dd = defaultdict(int)
        threes = 0
        twos = 0
        for row in list(self.rows):
            dd.clear()
            for ch in row:
                dd[ch] = dd[ch] + 1
            (c2, c3) = (0, 0)
            for k in dd.keys():
                if dd[k] == 3:
                    c3 = c3 + 1
                if dd[k] == 2:
                    c2 = c2 + 1
            threes = threes + (1 if c3 > 0 else 0)
            twos = twos + (1 if c2 > 0 else 0)
        print('Day 2 pt 1 %d' % (threes * twos))

    def part2(self):
        once = []
        for (ix, r) in enumerate(self.rows):
            for nr in self.rows[ix+1::]:
                ns = ''.join([(nr[i] if r[i] == nr[i] else '') for i in range(len(r))])
                if len(ns) == len(r) - 1:
                    once.append(ns)
        print('Day 2 p2 2 %s' % once[0])
