#!/usr/bin/env python3
from collections import defaultdict
import operator

class Day6:
    def __init__(self):
        indata = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
        tupp = tuple(indata)
        history = defaultdict(tuple)
        ll = len(indata)
        self.cycles = 0
        while tupp not in history:
            history[tupp] = self.cycles
            self.cycles += 1
            index, value = max(enumerate(indata), key=operator.itemgetter(1))
            indata[index] = 0
            while value > 0:
                index = (index + 1) % ll
                indata[index] += 1
                value -= 1
            tupp = tuple(indata)
        self.pt2 = self.cycles - history[tupp]

    def part1(self):
        return self.cycles

    def part2(self):
        return self.pt2
