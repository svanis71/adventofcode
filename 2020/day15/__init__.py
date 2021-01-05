from collections import defaultdict


def part1(indata, max_turns=2020):
    previous = defaultdict(int)
    for ix, n in enumerate(indata):
        previous[int(n)] = ix + 1

    nextprevious, turn, lastspoken = defaultdict(int), len(previous) + 1, 0
    while True:
        lastspoken = 0 if nextprevious[lastspoken] == 0 else previous[lastspoken] - nextprevious[lastspoken]
        nextprevious[lastspoken] = previous[lastspoken]
        previous[lastspoken] = turn
        turn += 1
        if turn > max_turns:
            break
    return lastspoken


def part2(indata):
    return part1(indata, 30 * 10 ** 6)


def run():
    indata = '1,12,0,20,8,16'.split(',')
    print(f'Day 14 part 1: {part1(indata)}')
    print(f'Day 14 part 2: {part2(indata)}')
