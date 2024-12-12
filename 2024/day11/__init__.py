from collections import Counter, defaultdict

import indata


def count_digits(n):
    if n // 10 == 0:
        return 1
    return 1 + count_digits(n // 10)


def blink(n: int) -> list[int]:
    digits = count_digits(n)
    if n == 0:
        return [1]
    if digits % 2 == 0:
        return list(divmod(n, 10 ** (digits // 2)))
    return [n * 2024]


def blink_all(p_stones: list[int], times: int) -> int:
    stones = Counter(p_stones)
    for _ in range(times):
        updated_stones: defaultdict[int, int] = defaultdict(int)
        for n, cnt in stones.items():
            for new_stone in blink(n):
                updated_stones[new_stone] += cnt
        stones = Counter(updated_stones)
    return sum(stones.values())


def run():
    puzzle_data = indata.read_infile('day11', use_testdata=False)
    stones: list[int] = [int(x) for x in puzzle_data.split(' ')]
    print(f'Day 11 pt1: {blink_all(stones, 25)}')
    print(f'Day 11 pt2: {blink_all(stones, 75)}')


# Day 11 pt1: 233050
# Day 11 pt2: 276661131175807

if __name__ == '__main__':
    run()
