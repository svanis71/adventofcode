from collections import defaultdict
from indata import read_list_of_strings


def part1():
    matrix = defaultdict(int)
    lines = read_list_of_strings('day5')
    for line in lines:
        pt1, pt2 = line.replace(' ', '').split('->')
        x1,y1 = pt1.split(',')
        x2,y2 = pt2.split(',')
        if x1 == x2:
            for y in range(int(min(y1, y2)), int(max(y1, y2))+1):
                matrix[f'{x1},{y}'] += 1
        elif y1 == y2:
            for x in range(int(min(x1, x2)), int(max(x1, x2))+1):
                matrix[f'{x},{y1}'] += 1
        else: 
            print(f'Skipping {x1},{y1} {x2},{y2}')
    return len([x for x in matrix.values() if x > 1])


def part2():
    pass


def run():
    print(f'Day 5 pt1: {part1()}')
    print(f'Day 5 pt2: {part2()}')
