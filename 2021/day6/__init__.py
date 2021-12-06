def part1():
    with open('indata/day6.txt') as f:
        lanternfishes = [int(x) for x in f.readline().split(',')]
    for day in range(0, 80):
        next_day_lanternfishes = []
        newborns = []
        for fish in lanternfishes:
            if fish > 0:
                next_day_lanternfishes.append(fish - 1)
            else:
                next_day_lanternfishes.append(6)
                newborns.append(8)
        next_day_lanternfishes += newborns
        lanternfishes = next_day_lanternfishes.copy()
    return len(lanternfishes)


def part2():
    with open('indata/day6_test.txt') as f:
        lanternfishes = [int(x) for x in f.readline().split(',')]
    for day in range(0, 80):
        next_day_lanternfishes = []
        newborns = []
        for fish in lanternfishes:
            if fish > 0:
                next_day_lanternfishes.append(fish - 1)
            else:
                next_day_lanternfishes.append(6)
                newborns.append(8)
        next_day_lanternfishes += newborns
        lanternfishes = next_day_lanternfishes.copy()
    return len(lanternfishes)


def run():
    print(f'Day 6 pt1: {part1()}')
    # print(f'Day 6 pt2: {part2()}')
