from itertools import product
from time import perf_counter

import indata

operators = {
    0: lambda x, y: int(x) + int(y),
    1: lambda x, y: int(x) * int(y),
    2: lambda x, y: int(f'{x}{y}'),
}


def solve(test_data: list[tuple[int, list[int]]], op_list: list[int]) -> int:
    validos: list[int] = []
    for ans, nums in test_data:
        ops = product(op_list, repeat=len(nums) - 1)
        for oplist in ops:
            rt, test_value = int(nums[0]), int(ans)
            for n, op in zip(nums[1:], oplist):
                rt = operators[op](rt, n)
                if rt > test_value:
                    break
            if rt == test_value:
                validos.append(test_value)
                break
    return sum(validos)


def run():
    puzzle_data = indata.read_list_of_strings('day7', use_testdata=False)
    tests: list[tuple[int, list[int]]] = []
    for line in puzzle_data:
        test_value, nums = line.split(': ')
        tests.append((int(test_value), [int(x) for x in nums.split(' ')]))

    start = perf_counter()
    print(f'Day 7 pt1: {solve(tests, [0, 1])}')
    print(f'Time: {perf_counter() - start} seconds')
    print(f'Day 7 pt2: {solve(tests, [0, 1, 2])}')
    print(f'Time: {perf_counter() - start} seconds')

# Day 7 pt1: 20665830408335
# Day 7 pt2: 354060705047464

if __name__ == '__main__':
    run()
