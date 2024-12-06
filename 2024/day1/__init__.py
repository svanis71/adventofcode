from collections import Counter

from indata import read_list_of_strings


def part1(inlist: list[list[int]]) -> int:
    left, right = sorted(x[0] for x in inlist), sorted(x[1] for x in inlist)
    return sum(abs(a - b) for a, b in zip(left, right))


def part2(inlist: list[list[int]]):
    c = Counter([x[1] for x in inlist])
    return sum(left * c[left] for left in list(x for x in [x[0] for x in inlist]))


def run():
    inlist = [[int(r[0]), int(r[1])] for r in [x.split('   ') for x in
                                               (read_list_of_strings('day1', use_testdata=False))]]
    print(f'Day 1 pt1: {part1(inlist)}')
    print(f'Day 1 pt2: {part2(inlist)}')


# Day 1 pt1: 1941353
# Day 1 pt2: 22539317

if __name__ == '__main__':
    run()
