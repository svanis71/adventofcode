from indata import read_list_of_integers


def part1(input):
    return [1 for i, j in zip(input, input[1:]) if j > i].count(1)


def part2(input):
    sums = [sum(input[i:i + 3]) for i, j in enumerate(input) if i <= len(input) - 3]
    return part1(sums)


def run():
    indata = read_list_of_integers('day1')
    print(f'Day 1 pt1: {part1(indata)}')
    print(f'Day 1 pt2: {part2(indata)}')

# Day 1 pt1: 1688
# Day 1 pt2: 1728
