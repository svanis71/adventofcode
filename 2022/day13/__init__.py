import json
from functools import cmp_to_key
from math import prod

from indata import read_infile


def compare_pairs(left: list[int | list], right: list[int | list]) -> int:
    # -1 if order is right, 1 is order is not right, 0 if equal
    for i, lv in enumerate(left):
        if len(right) == i:
            return 1
        rv = right[i]

        if type(lv) is int and type(rv) is int:
            if lv != rv:
                return -1 if lv < rv else 1
        else:
            cmp_list = compare_pairs([lv] if not type(lv) is list else lv, [rv] if not type(rv) is list else rv)
            if cmp_list != 0:
                return cmp_list
    return -1 if len(right) > 0 else 0


def part1(infile: str) -> int:
    pairs = [(json.loads(p[0]), json.loads(p[1])) for p in [x.split('\n') for x in infile.split('\n\n')]]
    return sum([pairno for pairno, pair in enumerate(pairs, 1) if compare_pairs(pair[0], pair[1]) == -1])


def part2(infile: str) -> int:
    pairs = [json.loads(x) for x in [x for x in infile.split('\n') if len(x) > 0]] + [[[2]], [[6]]]
    return prod([idx for idx, packet in
                 enumerate(sorted(pairs, key=cmp_to_key(lambda l, r: compare_pairs(l, r))), 1) if
                 packet in [[[2]], [[6]]]])


def run():
    infile = read_infile('day13')
    print(f'Day 13 pt1: {part1(infile)}')
    print(f'Day 13 pt2: {part2(infile)}')

# Day 13 pt1: 5905
# Day 13 pt2: 21691
