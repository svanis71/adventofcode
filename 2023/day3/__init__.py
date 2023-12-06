import re
from math import prod

from indata import read_list_of_strings


def part1():
    engine_schematic = read_list_of_strings('day3', use_testdata=False)
    sum_part_numbers = 0
    for lineno, line in enumerate(engine_schematic):
        for m in re.finditer(r'(\d+)', line):
            s = 0 if m.start() == 0 else m.start() - 1
            e = m.end() if m.end() == len(line) else m.end() + 1
            same_line = is_symbol(line[s:e])
            next_line = lineno < len(engine_schematic) - 1 and is_symbol(engine_schematic[lineno + 1][s:e])
            prev_line = lineno > 0 and is_symbol(engine_schematic[lineno - 1][s:e])
            if same_line or next_line or prev_line:
                sum_part_numbers += int(m.group())
    return sum_part_numbers


def part2():
    engine_schematic = read_list_of_strings('day3', use_testdata=False)
    gear_ratios = []
    for lineno, line in enumerate(engine_schematic):
        for m in re.finditer(r'\*', line):
            gear_numbers = []
            gear_pos = m.start()
            prev_line, next_line = engine_schematic[lineno - 1], engine_schematic[lineno + 1]
            if line[gear_pos - 1].isnumeric():
                gear_numbers.append(check_left(gear_pos, line))
            if line[gear_pos + 1].isnumeric():
                gear_numbers.append(check_right(gear_pos, line))
            if any(c.isnumeric() for c in prev_line[gear_pos - 1:gear_pos + 2]):
                check_adjacent_line(gear_numbers, gear_pos, prev_line)
            if any(c.isnumeric() for c in next_line[gear_pos - 1:gear_pos + 2]):
                check_adjacent_line(gear_numbers, gear_pos, next_line)
            if len(gear_numbers) == 2:
                gear_ratios.append(prod(gear_numbers))
    return sum(gear_ratios)


# Part 1 helpers

def is_symbol(c: str):
    return re.search(r'[^\d.]', c) is not None


def find_next_gear_number(gear_pos: int, lineno: int, engine_schematic: list[list[str]]) -> str:
    # left
    cur_line, next_line = engine_schematic[lineno], '' if lineno == len(engine_schematic) - 1 else engine_schematic[
        lineno + 1]
    n = []
    if cur_line[gear_pos - 1].isnumeric():
        p = gear_pos - 1
        while cur_line[p].isnumeric():
            n.insert(0, cur_line[p])
            p -= 1
    elif cur_line[gear_pos + 1].isnumeric():
        p = gear_pos + 1
        while cur_line[p].isnumeric():
            n.append(cur_line[p])
            p -= 1
    else:
        for m in re.finditer(r'(\d+)', next_line):
            if m.start() - 1 <= gear_pos <= m.end():
                return m.group()
    return ''.join(n)


# part two helpers

def check_adjacent_line(gear_numbers, gear_pos, line):
    for number_match_above in re.finditer(r'(\d+)', line):
        if number_match_above.start() - 1 <= gear_pos <= number_match_above.end():
            gear_numbers.append(int(number_match_above.group()))


def check_right(gear_pos, line):
    p, n = gear_pos + 1, []
    while line[p].isnumeric():
        n.append(line[p])
        p += 1
    possible_number = int(''.join(n))
    return possible_number


def check_left(gear_pos, line):
    p, n = gear_pos - 1, []
    while line[p].isnumeric():
        n.insert(0, line[p])
        p -= 1
    possible_number = int(''.join(n))
    return possible_number


def run():
    print(f'Day 3 pt1: {part1()}')
    print(f'Day 3 pt2: {part2()}')

# Day 3 pt1: 1129843
# Day 3 pt2: 73201705
