import itertools as it
from collections import deque

import indata
from pathfinding import get_adjacent_squares, inbound


def get_neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
    y, x = pos[0], pos[1]
    return [(y + offset[0], x + offset[1]) for offset in get_adjacent_squares()]


def is_edge(matrix: list[list[str]], ny: int, nx: int, current_plant: str) -> bool:
    return (inbound(matrix, ny, nx) and matrix[ny][nx] != current_plant) \
        or ny < 0 or ny >= len(matrix) or nx < 0 or nx >= len(matrix[0])


def cost_of_region(matrix, start: tuple[int, int]):
    plants = deque([start])
    region = {start}
    perimeter, plant = 0, matrix[start[0]][start[1]]
    while len(plants) > 0:
        cy, cx = plants.pop()
        for nxt in ((0, -1), (0, 1), (-1, 0), (1, 0),):
            ny, nx = cy + nxt[0], cx + nxt[1]
            if is_edge(matrix, ny, nx, plant):
                perimeter += 1
            elif inbound(matrix, ny, nx) and (ny, nx) not in region:
                plants.append((ny, nx))
                region.add((ny, nx))
    for (y, x) in region:
        matrix[y][x] = '-'

    cost = perimeter * len(region)
    # part 2
    side_cost = sum(corners(cy, cx, region) for cy, cx in region) * len(region)
    return cost, side_cost


def corners(cy, cx, region) -> int:
    num_corners = 0
    for oy, ox in it.product([1, -1], repeat=2):
        row_neighbor, col_neighbor, diagonal_neighbor = (cy + oy, cx), (cy, cx + ox), (cy + oy, cx + ox)
        if row_neighbor not in region and col_neighbor not in region:
            num_corners += 1
        if row_neighbor in region and col_neighbor in region and diagonal_neighbor not in region:
            num_corners += 1
    return num_corners


def solution(matrix: list[list[str]]) -> tuple[int, int]:
    costs_of_regions = []
    for iy, row in enumerate(matrix):
        for ix, plant in enumerate(row):
            if plant != '-':
                costs_of_regions.append(cost_of_region(matrix, (iy, ix)))
    return sum(n[0] for n in costs_of_regions), sum(n[1] for n in costs_of_regions)


def run():
    puzzle_data = indata.read_list_of_strings('day12', use_testdata=True)
    p1, p2 = solution([list(r) for r in puzzle_data])
    print(f'Day 12 pt1: {p1}')
    print(f'Day 12 pt2: {p2}')


# Day 12 pt1: 1304764
# Day 12 pt2: 811148

if __name__ == '__main__':
    run()
