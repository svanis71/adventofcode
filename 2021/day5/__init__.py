import re
from collections import defaultdict

from indata import read_list_of_strings


def part1():
    matrix = defaultdict(int)
    lines = read_list_of_strings('day5')

    for line in lines:
        (x1, y1, x2, y2) = [int(p) for p in re.findall(r'(\d+)', line)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix[(x1, y)] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix[(x, y1)] += 1
    return len([k for k, v in matrix.items() if v >= 2])


def part2():
    matrix = defaultdict(int)
    lines = read_list_of_strings('day5')

    for line in lines:
        (x1, y1, x2, y2) = [int(p) for p in re.findall(r'(\d+)', line)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix[(x, y1)] += 1
        else:
            #print(f'{x1},{y1} -> {x2},{y2} ')
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            ydir = -1 if y1 > y2 else 1
            for yoffset, x in enumerate(range(x1, x2 + 1)):
                y = y1 + yoffset * ydir
                #print(f'Set {x},{y}')
                matrix[(x, y)] += 1

    # for y in range(10):
    #     for x in range(10):
    #         if matrix[(x, y)] == 0:
    #             print('.', end='')
    #         else:
    #             print(matrix[(x, y)], end='')
    #     print()

    return len([k for k, v in matrix.items() if v >= 2])


def run():
    print(f'Day 5 pt1: {part1()}')
    print(f'Day 5 pt2: {part2()}')

# Day 5 pt1: 6267
