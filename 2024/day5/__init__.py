from collections import defaultdict
from functools import cmp_to_key

import indata


def solve(puzzle_input: str) -> tuple[int, int]:
    rules_def, data = puzzle_input.split('\n\n')
    rule_map: dict[str, list[str]] = defaultdict(list[str])

    for rule in rules_def.splitlines():
        before, after = rule.split('|')
        rule_map[before].append(after)

    correct_middle_numbers, incorrect_middle_numbers = [], []
    for inp in data.splitlines():
        from_input = inp.split(',')
        correct_sorted_input = sorted(from_input,
                                      key=cmp_to_key(lambda a, b: 0 if a == b else -1 if b in rule_map[a] else 1))
        if from_input == correct_sorted_input:
            correct_middle_numbers.append(int(from_input[len(from_input) // 2]))
        else:
            incorrect_middle_numbers.append(int(correct_sorted_input[len(correct_sorted_input) // 2]))
    return sum(correct_middle_numbers), sum(incorrect_middle_numbers)


def run():
    puzzle_data = indata.read_infile('day5', use_testdata=False)
    part1, part2 = solve(puzzle_data)
    print(f'Day 5 pt1: {part1}')
    print(f'Day 5 pt2: {part2}')


# Day 5 pt1: 6384
# Day 5 pt2: 5353

if __name__ == '__main__':
    run()
