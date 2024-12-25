from collections import deque

import indata
from pathfinding import get_adjacent_squares, inbound


def get_neighbors(matrix, pos: tuple[int, int]) -> list[tuple[int, int]]:
    y, x = pos[0], pos[1]
    return [(y + offset[0], x + offset[1]) for offset in get_adjacent_squares()]


def is_edge(matrix: list[list[str]], ny: int, nx: int, current_plant: str) -> bool:
    return (inbound(matrix, ny, nx) and matrix[ny][nx] != current_plant) \
        or ny < 0 or ny >= len(matrix) or nx < 0 or nx >= len(matrix[0])


def cost_of_region(matrix, start: tuple[int, int]):
    que = deque([start])
    visited = {start}
    cost = 0
    perimeter, plant = 0, matrix[start[0]][start[1]]
    perimeter_nodes = []
    while len(que) > 0:
        cy, cx = que.pop()
        for nxt in ((0, -1), (0, 1), (-1, 0), (1, 0),):
            ny, nx = cy + nxt[0], cx + nxt[1]
            if is_edge(matrix, ny, nx, plant):
                perimeter += 1
                perimeter_nodes.append((ny, nx))
            elif inbound(matrix, ny, nx) and (ny, nx) not in visited:
                que.append((ny, nx))
                visited.add((ny, nx))
    for (y, x) in visited:
        matrix[y][x] = '-'
    print(f'A region of {plant} plants with price {len(visited)} * {perimeter} = {perimeter * len(visited)}')
    cost += (perimeter * len(visited))
    return cost


def part1(matrix: list[list[str]]) -> int:
    cost: int = 0
    for iy, row in enumerate(matrix):
        for ix, plant in enumerate(row):
            if plant != '-':
                cost += cost_of_region(matrix, (iy, ix))
    return cost


def part2(puzzle_input: list[str]) -> int:
    pass


def run():
    puzzle_data = indata.read_list_of_strings('day12', use_testdata=True)
    matrix = [list(r) for r in puzzle_data]
    print(f'Day 12 pt1: {part1(matrix)}')
    print(f'Day 12 pt2: {part2(puzzle_data)}')


# Day 12 pt1: 1304764
# Day 12 pt2: 0

if __name__ == '__main__':
    run()
