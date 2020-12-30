from collections import defaultdict

from indata import read_list_of_integers


def part1():
    adapters = sorted(read_list_of_integers('day10'))
    diff = defaultdict(int)
    diff[3] = 1
    prev = 0
    while len(adapters):
        diff[adapters[0] - prev] += 1
        prev = adapters.pop(0)
    return diff[1] * diff[3]


def part2():
    adapters = sorted(read_list_of_integers('day10'))
    can_remove_more, kombos, idx = False, 1, 1
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    while idx < len(adapters) - 1:
        if adapters[idx + 1] - adapters[idx - 1] == 3:  # Required
            idx += 1
            continue
        xl = [x for x in adapters[idx:idx+3] if x < adapters[idx]]
        kombos += 1

    return kombos


def run():
    print(f'Day 10 part 1: {part1()}')
#    print(f'Day 10 part 2: {part2()}')
