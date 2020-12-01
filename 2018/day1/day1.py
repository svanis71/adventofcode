#!/usr/bin/env python3
from collections import defaultdict

class Day1:
  def __init__(self):
    with open('day1/in.txt') as f:
      content = f.readlines()
    self.list = [int(x.strip()) for x in content]

  def part1(self):
    print('Day 1 pt1 : %d ' % sum(self.list))

  def part2(self):
    dd = defaultdict(int)
    running_sum = 0
    found = False
    while not found:
      for i in self.list:
        running_sum += i
        dd[running_sum] = dd[running_sum] + 1
        if dd[running_sum] > 1:
          found = True
          print('Day 2 tp 2: %d' %  running_sum)
          break

