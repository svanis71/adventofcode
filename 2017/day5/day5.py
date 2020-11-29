#!/usr/bin/env python3

class Day5:
    def __init__(self):
        with open('day5/indata.txt', 'r') as myfile:
            self.data=myfile.read().strip().split('\n')

    def part2(self):
        data = [int(i) for i in self.data]
        pos = 0
        steps = 0
        
        while pos < len(data):
            steps += 1
            jmp = data[pos]
            if jmp >= 3:
                data[pos] -= 1
            else:
                data[pos] += 1
            pos += jmp
        return steps
            
    def part1(self):
        data = [int(i) for i in self.data]
        pos = 0
        steps = 0

        while pos < len(data):
            steps += 1
            jmp = data[pos]
            data[pos] += 1
            pos += jmp
                            
        return steps
    
