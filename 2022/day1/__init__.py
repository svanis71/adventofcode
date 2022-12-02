"""
AoC 22 day 1
"""
from itertools import groupby

from indata import read_list_of_strings


def run():
    """
    AoC 22 day 1
    """
    elves_inventory = groupby(read_list_of_strings('day1'), lambda z: z == '')
    inventory = sorted([sum(int(i) for i in list(y)) for x, y in elves_inventory if not x],
                       reverse=True)[0:3]
    print(f'Day 1 pt1: {max(inventory)}')
    print(f'Day 1 pt2: {sum(inventory)}')

# Day 1 pt1: 69206
# Day 1 pt2: 197400
