from collections import defaultdict
from queue import PriorityQueue

from indata import read_list_of_strings


def find_lowest_risk(grid, start, goal, allow_diagonal_movement=False):
    queue = PriorityQueue()
    queue.put(start, 0)
    risk_levels = defaultdict(int)
    risk_levels[start] = 0
    came_from = defaultdict(tuple)
    came_from[start] = None

    neighbours = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    while not queue.empty():
        current = queue.get()
        if current == goal:
            break

        for nextp_offset in neighbours:
            nextp = (current[0] + nextp_offset[0], current[1] + nextp_offset[1])
            if nextp[0] > (len(grid) - 1) or nextp[0] < 0 or nextp[1] > (len(grid[len(grid) - 1]) - 1) or nextp[1] < 0:
                continue
            new_cost = risk_levels[current] + grid[nextp[0]][nextp[1]]
            if nextp not in risk_levels or new_cost < risk_levels[nextp]:
                risk_levels[nextp] = new_cost
                prio = new_cost + ((nextp[0] - goal[0]) ** 2) + ((nextp[1] - goal[1]) ** 2)
                queue.put(nextp, prio)
                came_from[nextp] = current

    path = [goal]
    while path[0] != start:
        path.insert(0, came_from[path[0]])
    for iy, row in enumerate(grid):
        for ix, risk_level in enumerate(row):
            if (iy, ix) in path:
                print(f'\033[94m\033[1m{risk_level}\033[0m', end='')
            else:
                print(f'{risk_level}', end='')
        print()

    return risk_levels[goal]


def part1():
    risk_level_map = [[int(risk_level) for risk_level in row] for row in read_list_of_strings('day15')]
    return find_lowest_risk(risk_level_map, (0, 0), (len(risk_level_map) - 1, len(risk_level_map[0]) - 1))


def part2():
    pass


def run():
    print(f'Day 15 pt1: {part1()}')
    print(f'Day 15 pt2: {part2()}')

# Day 15 pt1: 527
# Day 15 pt2:
