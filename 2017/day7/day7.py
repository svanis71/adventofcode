#!/usr/bin/env python3
import re

class Day7:
    def __init__(self):
        self.data = [l.strip() for l in open('day7/indata.txt', 'r')]

    def part1(self):
        pgms = [x for x in self.data if x.find('->') >= 0]
        for s in pgms:
            m = re.search('\w+', s)
            t = [x for x in self.data if x.find(m.group(0)) >= 0]
            if len(t) == 1:
                root = m.group(0)
                break

        return root

    def getWeight(self, pgm):
        return
    def part2(self):
        root = 'cyrupz'
        return 0