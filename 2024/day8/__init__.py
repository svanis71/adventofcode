import itertools as it
from collections import defaultdict

import indata


def get_distance(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return p2[0] - p1[0], p2[1] - p1[1]


def inside_map(the_map: list[str], pt: tuple[int, int]) -> bool:
    return 0 <= pt[0] < len(the_map) and 0 <= pt[1] < len(the_map[0])


def get_antinodes(antennas, puzzle_input: list[str], with_t_freq: bool = False):
    antinodes: set[tuple[int, int]] = set()
    for antenna in antennas.values():
        for antenna_1, antenna_2 in it.combinations(antenna, 2):
            dy, dx = antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]
            antinode_up = antenna_1[0] - dy, antenna_1[1] - dx
            antinode_down = antenna_2[0] + dy, antenna_2[1] + dx
            if inside_map(puzzle_input, antinode_up):
                antinodes.add(antinode_up)
            if inside_map(puzzle_input, antinode_down):
                antinodes.add(antinode_down)
            if with_t_freq:
                antinodes.add(antenna_1)
                antinodes.add(antenna_2)
                while inside_map(puzzle_input, antinode_up) or inside_map(puzzle_input, antinode_down):
                    antinode_up = antinode_up[0] - dy, antinode_up[1] - dx
                    antinode_down = antinode_down[0] + dy, antinode_down[1] + dx
                    if inside_map(puzzle_input, antinode_up):
                        antinodes.add(antinode_up)
                    if inside_map(puzzle_input, antinode_down):
                        antinodes.add(antinode_down)
    return antinodes


def solution(puzzle_input: list[str], with_t_freq: bool = False) -> int:
    antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for ir, row in enumerate(puzzle_input):
        for ic, col in enumerate(row):
            if col != '.':
                antennas[col].append((ir, ic))
    return len(get_antinodes(antennas, puzzle_input, with_t_freq))


def run():
    puzzle_data = indata.read_list_of_strings('day8', use_testdata=True)
    print(f'Day 8 pt1: {solution(puzzle_data, with_t_freq=False)}')
    print(f'Day 8 pt2: {solution(puzzle_data, with_t_freq=True)}')


# Day 8 pt1: 344
# Day 8 pt2: 1182

if __name__ == '__main__':
    run()
