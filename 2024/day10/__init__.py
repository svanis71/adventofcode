from collections import deque, defaultdict

import indata
from pathfinding import inbound


def get_starting_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    starting_points: list[tuple[int, int]] = []
    for ir, r in enumerate(matrix):
        for ic, c in enumerate(r):
            if c == 0:
                starting_points.append((ir, ic))
    return starting_points


def get_neighbors(matrix, pos: tuple[int, int]) -> list[tuple[int, int]]:
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    y, x = pos
    return [(y + offset[0], x + offset[1]) for offset in adjacent_squares
            if
            inbound(matrix, offset[0] + y, offset[1] + x) and matrix[y + offset[0]][x + offset[1]] == matrix[y][x] + 1]


def get_score(matrix, start, distinct: bool = False) -> int:
    que = deque([start])
    visited = {start}
    came_from = defaultdict(list)
    score: int = 0
    while len(que) > 0:
        current = que.pop()
        if matrix[current[0]][current[1]] == 9:
            score += 1
        for nxt in get_neighbors(matrix, current):
            if distinct or nxt not in visited and nxt not in came_from:
                que.append(nxt)
                came_from[nxt].append(current)
                visited.add(nxt)
    return score


def run():
    puzzle_data = indata.read_list_of_strings('day10', use_testdata=True)
    matrix = [[int(c) for c in r] for r in puzzle_data]
    print(f'Day 10 pt1: {sum(get_score(matrix, start) for start in (get_starting_points(matrix)))}')
    print(f'Day 10 pt2: {sum(get_score(matrix, start, True) for start in (get_starting_points(matrix)))}')


# Day 10 pt1: 514
# Day 10 pt2: 1162

if __name__ == '__main__':
    run()
