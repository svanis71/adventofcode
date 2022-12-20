import json
from functools import cmp_to_key
from math import prod

from indata import read_infile


def compare_pairs(left: list[int | list], right: list[int | list]) -> bool | None:
    for i, lv in enumerate(left):
        if len(right) == i:
            return False
        rv = right[i]

        if type(lv) is int and type(rv) is int:
            if lv != rv:
                return lv < rv
        else:
            cmp_list = compare_pairs([lv] if not type(lv) is list else lv, [rv] if not type(rv) is list else rv)
            if cmp_list is not None:
                return cmp_list
    return True if len(right) > 0 else None


def part1(pairs: list[tuple]) -> int:
    right_order_pairs = [pairno for pairno, pair in enumerate(pairs, 1) if compare_pairs(pair[0], pair[1])]
    return sum(right_order_pairs)


def compare_converter(bool_val: bool | None):
    return -1 if bool_val else 0 if bool_val is None else 1


def part2(pairs: list[list]) -> int:
    mul_val = [idx for idx, packet in
               enumerate(sorted(pairs, key=cmp_to_key(lambda l, r: compare_converter(compare_pairs(l, r)))), 1) if
               packet in [[[2]], [[6]]]]
    return prod(mul_val)


def run():
    infile = read_infile('day13')
    pairs_in = [x.split('\n') for x in infile.split('\n\n')]
    inpairs = [(json.loads(p[0]), json.loads(p[1])) for p in pairs_in]
    print(f'Day 13 pt1: {part1(inpairs)}')
    all_packets = [x for x in infile.split('\n') if len(x) > 0]
    all_packets.append('[[2]]')
    all_packets.append('[[6]]')
    print(f'Day 13 pt2: {part2([json.loads(x) for x in all_packets])}')

# Day 13 pt1:
# Day 13 pt2:
