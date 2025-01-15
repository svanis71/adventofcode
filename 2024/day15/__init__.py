from collections import deque

import numpy as np

import indata
from common import DIRECTIONS


def find_next_box(wm, from_pos: tuple[int, int], direction: tuple[int, int]) \
        -> tuple[tuple[int, int], tuple[int, int] | None]:
    cy, cx = from_pos[0] + direction[0], from_pos[1]

    if wm[cy][cx] == 'O':
        return (cy, cx), None
    if wm[cy][cx] in "[":
        return (cy, cx), (cy, cx + 1)
    return (cy, cx - 1), (cy, cx)


def move_horizontal(wm, robot_pos, direction: tuple[int, int]) -> tuple[int, int]:
    _, dx = direction
    cur_y, cur_x = robot_pos[0], robot_pos[1] + dx
    while wm[cur_y, cur_x] in '[]O':
        cur_x = cur_x + dx
    if wm[cur_y, cur_x] == '#':
        return robot_pos
    while (cur_y, cur_x) != robot_pos:
        wm[(cur_y, cur_x)], wm[(cur_y, cur_x - dx)] = wm[(cur_y, cur_x - dx)], wm[(cur_y, cur_x)]
        cur_x = cur_x - dx
    return cur_y, cur_x + dx


def hit_a_wall(wm, left: tuple[int, int], right: tuple[int, int]) -> bool:
    return wm[left] == '#' or (all(x is not None for x in right) and wm[right] == '#')


def move_robot(wm, robot_pos: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    que: deque[tuple[tuple[int, int], tuple[int, int]]] = deque()
    que.append(find_next_box(wm, robot_pos, direction))
    items_to_move = set()
    while len(que) > 0:
        next_box_left, next_box_right = que.pop()
        new_left_y, new_left_x = (next_box_left[0] + direction[0], next_box_left[1])
        new_right_y, new_right_x = (None, None) if next_box_right is None \
            else (next_box_right[0] + direction[0], next_box_right[1])
        if hit_a_wall(wm, (new_left_y, new_left_x), (new_right_y, new_right_x)):
            return robot_pos
        items_to_move.add((next_box_left, next_box_right))
        if wm[(new_left_y, new_left_x)] in '[]O':
            que.append(find_next_box(wm, next_box_left, direction))
        if new_right_y is not None and wm[(new_right_y, new_right_x)] == '[':
            que.append(find_next_box(wm, next_box_right, direction))

    for (left, right) in sorted(items_to_move, reverse=direction[0] > 0):
        wm[(left[0] + direction[0], left[1])], wm[left] = wm[left], '.'
        if right is not None:
            wm[(right[0] + direction[0], right[1])], wm[right] = wm[right], '.'
    move_robot_to = (robot_pos[0] + direction[0], robot_pos[1])
    wm[move_robot_to], wm[robot_pos] = '@', '.'
    return move_robot_to


def get_score(wm, point_char: str) -> int:
    return sum(sum(100 * iy + ix for ix, c in enumerate(row) if c == point_char) for iy, row in enumerate(wm))


def solution(warehouse_map, instructions: str, start_pos: tuple[int, int], box_char: str) -> int:
    current_pos = start_pos
    for direction in instructions:
        dy, dx = DIRECTIONS[direction]
        ny, nx = (current_pos[0] + dy, current_pos[1] + dx)
        if warehouse_map[(ny, nx)] == '#':
            continue
        if warehouse_map[(ny, nx)] == '.':
            warehouse_map[(ny, nx)], warehouse_map[current_pos] = warehouse_map[current_pos], '.'
            current_pos = (ny, nx)
        elif direction in '<>':
            current_pos = move_horizontal(warehouse_map, current_pos, DIRECTIONS[direction])
        else:
            current_pos = move_robot(warehouse_map, current_pos, DIRECTIONS[direction])

    return get_score(warehouse_map, box_char)


def get_start_pos(wm) -> tuple[int, int]:
    return [(y, x) for y, row in enumerate(wm) for x, cell in enumerate(row) if cell == '@'][0]


def warehouse_large(warehouse: str):
    translate = {'@': '@.', 'O': '[]', '.': '..', '#': '##'}
    grid = [list(''.join([translate[c] for c in row])) for row in warehouse.splitlines()]
    return np.array(grid, dtype=str)


def run():
    puzzle_input = indata.read_infile('day15', use_testdata=False)
    warehouse_map, instructions = puzzle_input.split('\n\n')
    wm = np.array([list(itm) for itm in warehouse_map.splitlines()], dtype=str)
    instructions = instructions.replace('\n', '')
    print(f'Day 15 pt1: {solution(wm, instructions, get_start_pos(wm), "O")}')
    wm = warehouse_large(warehouse_map)
    print(f'Day 15 pt2: {solution(wm, instructions, get_start_pos(wm), "[")}')


if __name__ == '__main__':
    run()
