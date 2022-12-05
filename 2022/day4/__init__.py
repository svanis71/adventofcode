from indata import read_list_of_strings


def part1(puzzle_input: list) -> int:
    return len([True for s1, s2 in
                [(set(range(int(g1[0]), int(g1[1]) + 1)), set(range(int(g2[0]), int(g2[1]) + 1))) for g1, g2 in
                 puzzle_input] if s1.issubset(s2) or s1.issuperset(s2)])


def part2(puzzle_input: list) -> int:
    return len([True for s1, s2 in
                [(set(range(int(g1[0]), int(g1[1]) + 1)), set(range(int(g2[0]), int(g2[1]) + 1))) for g1, g2 in
                 puzzle_input] if len(s1.intersection(s2)) > 0])


def run():
    puzzle_input = [(l1.split('-'), l2.split('-')) for l1, l2 in [x.split(',') for x in read_list_of_strings('day4')]]
    print(f'Day 4 pt1: {part1(puzzle_input)}')
    print(f'Day 4 pt2: {part2(puzzle_input)}')

# Day 4 pt1: 588
# Day 4 pt2: 911
