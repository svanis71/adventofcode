from itertools import combinations

from indata import read_list_of_strings


def is_safe(nums: list[int]) -> bool:
    diffs = [a - b for (a, b) in zip(nums, nums[1:])]
    return all((0 < d < 4) for d in diffs) or all((-4 < d < 0) for d in diffs)


def part1(indata: list[str]) -> int:
    return len([1 for line in indata if is_safe([int(x) for x in line.split(' ')])])


def part2(indata: list[list[int]]) -> int:
    return sum(1 for int_list in indata if
               any(True for comb in combinations(int_list, len(int_list) - 1) if is_safe(list(comb))))


def run():
    indata = read_list_of_strings('day2', use_testdata=True)
    print(f'Day 2 pt1: {part1(indata)}')
    print(f'Day 2 pt2: {part2([[int(x) for x in line.split(" ")] for line in indata])}')


# Day 2 pt1: 242
# Day 2 pt2: 311

if __name__ == '__main__':
    run()
