from collections import defaultdict, Counter
from itertools import pairwise

from indata import read_list_of_strings


def step(cnt: Counter, pairs: defaultdict(int), rules: dict) -> defaultdict(int):
    new_pairs = defaultdict(int)
    for pair in pairs:
        ins_letter = rules[pair]
        new_pairs[pair[0] + ins_letter] += pairs[pair]
        new_pairs[ins_letter + pair[-1]] += pairs[pair]
        cnt[ins_letter] += pairs[pair]
    return new_pairs


def calc_polymer(steps: int) -> int:
    indata = read_list_of_strings('day14')
    polymer_template = indata.pop(0)
    pairs, letter_count = defaultdict(int), Counter(polymer_template)

    for pair in [''.join(p) for p in pairwise(polymer_template)]:
        pairs[pair] += 1
    rules = dict([(rule[:2], rule[-1]) for rule in indata[1:]])

    for i in range(steps):
        pairs = step(letter_count, pairs, rules)

    return max(letter_count.values()) - min(letter_count.values())


def part1() -> int:
    return calc_polymer(10)


def part2() -> int:
    return calc_polymer(40)


def run():
    print(f'Day 14 pt1: {part1()}')
    print(f'Day 14 pt2: {part2()}')

# Day 14 pt1: 4244
# Day 14 pt2: 4807056953866
