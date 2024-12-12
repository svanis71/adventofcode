from itertools import product
from operator import add, mul, concat

import indata


def part1(puzzle_input: list[str]) -> tuple[int, list[tuple[int, list[str]]]]:
    validos, invalidos = [], []
    for line in puzzle_input:
        ans, nums_str = line.split(': ')
        nums: list[int] = [int(n) for n in nums_str.split(' ')]
        ops = product([add, mul], repeat=len(nums) - 1)
        valido = False
        for oplist in ops:
            rt = nums[0]
            for n, op in zip(nums[1:], oplist):
                rt = op(rt, n)
            if rt == int(ans):
                validos.append(int(ans))
                valido = True
                break
        if not valido:
            invalidos.append((int(ans), nums_str.split(' ')))
    return sum(validos), invalidos


def part2(p1_invalidos: list[tuple[int, list[str]]], p1_sum: int) -> int:
    validos:list[int] = []
    for ans, nums in p1_invalidos:
#        ops = product([add, mul, concat], repeat=len(nums) - 1)
        for oplist in ops:
            rt = int(nums[0])
            for n, op in zip(nums[1:], oplist):
                rt = op(rt, n)
            if rt == int(ans):
                validos.append(int(ans))
                break
    return sum(validos) + p1_sum

def run():
    puzzle_data = indata.read_list_of_strings('day7', use_testdata=False)
    p1_sum, p1_invalidos = part1(puzzle_data)
    print(f'Day 7 pt1: {p1_sum}')
    print(f'Day 7 pt2: {part2(p1_invalidos, p1_sum)}')


# Day 7 pt1: 0
# Day 7 pt2: 0

if __name__ == '__main__':
    run()
