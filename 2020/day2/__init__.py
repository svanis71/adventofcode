import re

from indata import read_lines

REGEXP = r'(\d+)-(\d+)\s([a-z]):\s(.*)'


def part1():
    ok_cnt = 0
    for line in [re.findall(REGEXP, x) for x in (read_lines('day2'))]:
        minoccurs, maxoccurs, ch, pw = line.pop(0)
        cnt = len([c for c in pw if c == ch])
        ok_cnt = ok_cnt + 1 if int(minoccurs) <= cnt <= int(maxoccurs) else ok_cnt
    return ok_cnt


def part2():
    ok_cnt = 0
    for line in [re.findall(REGEXP, x) for x in (read_lines('day2'))]:
        p1, p2, ch, pw = line.pop(0)
        ok_cnt = ok_cnt + 1 if (pw[int(p1) - 1] == ch and pw[int(p2) - 1] != ch) or (
                pw[int(p1) - 1] != ch and pw[int(p2) - 1] == ch) else ok_cnt
    return ok_cnt


def run():
    print(f'Day 2 part 1: {part1()}')
    print(f'Day 2 part 2: {part2()}')
