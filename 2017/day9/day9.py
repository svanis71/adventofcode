#!/usr/bin/env python3
import re

class Day9:
    garbLen = 0

    def removeGarbage(self, data):
        clean = re.sub(r'!.', '', data)
        clean = re.sub(r'<.*?>', '', clean)
        st = clean.find('<')
        end = clean.find('>', st)
        if st > 0:
            clean = self.removeGarbage(clean[0:st] + clean[end+1:])
        return clean

    def part1(self):
        data = open('day9/indata.txt', 'r').read()
        data = self.removeGarbage(data)

        score = 0
        level = 0
        for c in data:
            if c == '{':
                level += 1
                score += level
            elif c == '}':
                level -= 1

        return score

    def part2(self):
        data = open('day9/indata.txt', 'r').read()
        clean = re.sub(r'!.', '', data)
        m = re.findall(r'<.*?>', clean)
        return sum([len(hit) - 2 for hit in m])