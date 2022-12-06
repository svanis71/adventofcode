from indata import read_infile


def part1_2(uniq_len: int) -> int:
    datastream = read_infile('day6')
    for idx, letter in enumerate(datastream):
        if uniq_len == len(set(datastream[idx:idx + uniq_len])):
            return idx + uniq_len


def run():
    print(f'Day 6 pt1: {part1_2(4)}')
    print(f'Day 6 pt2: {part1_2(14)}')

# Day 6 pt1: 1766
# Day 6 pt2: 2383
