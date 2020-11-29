#!/usr/bin/env python3

class Day1:
    def __init__(self):
        with open('day1/indata_day1.txt', 'r') as myfile:
            self.data=myfile.read().replace('\n', '')

    def split_list(self, a_list):
        half = int(len(a_list)/2)
        return a_list[:half], a_list[half:]
    
    def part2(self):
        intarr = [int(s) for s in list(self.data)]
        arr1,arr2 = self.split_list(intarr)
        sum = 0
        for i,j in zip(arr1, arr2):
            if i == j:
                sum += (i + j)
        return sum

    def part1(self):
        intarr = [int(s) for s in list(self.data)]
        prev = intarr[-1]
        sum = 0
        for i in intarr:
            if i == prev:
                sum += i
            prev = i
        return sum
    
