from collections import Counter

from indata import read_list_of_strings


def part1(inlist: list[list[int]]) -> int:
    left, right = sorted(x[0] for x in inlist), sorted(x[1] for x in inlist)
    return sum(abs(a - right[ix]) for ix, a in enumerate(left))


def part2(inlist: list[list[int]]):
    c = Counter([x[1] for x in inlist])
    return sum(left * occurrences_in_right for (left, occurrences_in_right) in [(x, 0 if x not in c else c[x]) for x in [x[0] for x in inlist]])


def run():
    inlist = [[int(r[0]), int(r[1])] for r in [x.split('   ') for x in
                                               (read_list_of_strings('day1', use_testdata=False))]]
    print(f'Day 1 pt1: {part1(inlist)}')
    print(f'Day 1 pt2: {part2(inlist)}')


# Day 1 pt1: 1941353
# Day 1 pt2: 22539317

if __name__ == '__main__':
    run()
