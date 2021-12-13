from collections import deque

from indata import read_list_of_strings


def get_neighbours(matrix, x, y):
    adjacent_points = []
    if x > 0:
        adjacent_points.append((x - 1, y))
    if x < len(matrix[y]) - 1:
        adjacent_points.append((x + 1, y))
    if y > 0:
        adjacent_points.append((x, y - 1))
    if y < len(matrix) - 1:
        adjacent_points.append((x, y + 1))
    return adjacent_points


def get_lows(matrix):
    low_points = []
    for iy, row in enumerate(matrix):
        for ix, colval in enumerate(row):
            adjacents = [matrix[py][px] for (px, py) in get_neighbours(matrix, ix, iy)]
            if len([x for x in adjacents if x <= colval]) == 0:
                low_points.append((ix, iy))
    return low_points


def get_basins(matrix, px, py):
    basin = []
    visited = set()
    queue = deque([(px, py)])

    while queue:
        (x, y) = queue.pop()

        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))
            if matrix[y][x] != 9:
                basin.append((x, y))
                queue.extend([(xn, yn) for (xn, yn) in get_neighbours(matrix, x, y) if (xn, yn) not in visited])

    return basin


def part1():
    matrix = [[int(i) for i in s] for s in (read_list_of_strings('day9'))]
    return sum([matrix[y][x] + 1 for (x, y) in get_lows(matrix)])


def part2():
    matrix = [[int(i) for i in s] for s in (read_list_of_strings('day9'))]
    lows = get_lows(matrix)
    prod, basins = 1, [get_basins(matrix, x, y) for (x, y) in lows]
    for n in sorted([len(basin) for basin in basins], reverse=True)[0:3]:
        prod *= n
    return prod


def run():
    print(f'Day 9 pt1: {part1()}')
    print(f'Day 9 pt2: {part2()}')

# Day 9 pt1: 486
# Day 9 pt2: 1059300
