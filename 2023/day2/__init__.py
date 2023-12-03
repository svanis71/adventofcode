from collections import defaultdict
from math import prod

from indata import read_list_of_strings


# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
def part1() -> int:
    max_of_col = {'red': 12, 'green': 13, 'blue': 14}
    indata: list[str] = read_list_of_strings('day2', use_testdata=False)
    id_sum: int = 0
    for game in indata:
        valid = True
        game = game.replace(', ', ',')
        gameid: int = int(game[5:game.find(':')])
        cube_sets = game[game.find(':') + 1:].strip(' ').split(';')
        draws = [x.split(',') for x in cube_sets]
        for draw in draws:
            valid = valid and all((int(n) <= max_of_col[m]) for (n, m) in [x.strip(' ').split(' ') for x in draw])
        if valid:
            id_sum += gameid
    return id_sum


def part2() -> int:
    games: list[str] = read_list_of_strings('day2', use_testdata=False)
    sum_of_power = 0
    for game in games:
        dd = defaultdict(int)
        xx = game[game.index(':') + 2:].replace(',', '').replace(';', '').split(' ')
        for n, col in zip(xx, xx[1:]):
            if n.isnumeric() and dd[col] < int(n):
                dd[col] = int(n)
        sum_of_power += prod(dd.values())
    return sum_of_power


def run():
    print(f'Day 2 pt1: {part1()}')
    print(f'Day 2 pt2: {part2()}')

# Day 2 pt1: 2105
# Day 2 pt2: 72422
