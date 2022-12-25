import math

from indata import read_infile

START_POS = (500, 0)


def part_1(rock_structure: dict[tuple[int, int]]) -> int:
    ymax = max(k[1] for k, _ in rock_structure.items())
    sand_pos, sand_units = START_POS, []

    while True:
        sand_x, sand_y = sand_pos
        if (sand_x, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x, sand_y + 1)
        elif (sand_x - 1, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x - 1, sand_y + 1)
        elif (sand_x + 1, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x + 1, sand_y + 1)
        elif sand_pos[1] < ymax:
            rock_structure[sand_pos] = 2
            sand_units.append(sand_pos)
            sand_pos = START_POS
        if sand_pos[1] > ymax:
            break
    return len(sand_units)


def part_2(rock_structure: dict[tuple[int, int]]) -> int:
    ymax = max(k[1] for k, _ in rock_structure.items()) + 2
    sand_pos, sand_units = START_POS, []
    sand_x, sand_y = math.inf, math.inf
    while sand_y != sand_pos[1]:
        sand_x, sand_y = sand_pos
        rock_structure[(sand_x - 1, ymax)] = 1
        rock_structure[(sand_x + 1, ymax)] = 1
        rock_structure[(sand_x, ymax)] = 1
        if (sand_x, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x, sand_y + 1)
        elif (sand_x - 1, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x - 1, sand_y + 1)
        elif (sand_x + 1, sand_y + 1) not in rock_structure:
            sand_pos = (sand_x + 1, sand_y + 1)
        elif sand_pos[1] < ymax:
            rock_structure[sand_pos] = 2
            sand_units.append(sand_pos)
            sand_pos = START_POS
        else:
            break
    return len(sand_units)


def create_rock_structure(pts_list) -> dict[tuple[int, int]]:
    structure: dict[tuple[int, int]] = dict()
    structure[START_POS] = 3
    for pts in pts_list:
        for pt in zip(pts, pts[1:]):
            x1, y1 = [int(x) for x in pt[0].split(',')]
            x2, y2 = [int(x) for x in pt[1].split(',')]
            if x1 == x2:  # Vert
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    structure[(x1, y)] = 1
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    structure[(x, y1)] = 1
    return structure


def run():
    pts_list: list[list[str]] = [ll.split('->') for ll in
                                 (read_infile('day14').replace(' ', '').splitlines())]
    print(f'Day 14 pt1: {part_1(create_rock_structure(pts_list))}')
    print(f'Day 14 pt2: {part_2(create_rock_structure(pts_list))}')

# Day 14 pt1: 618
# Day 14 pt2: 26358
