from collections import defaultdict
from queue import PriorityQueue

from indata import read_list_of_strings


def find_lowest_risk(grid, multiplier=1):
    start, size_x, size_y = (0, 0), len(grid[0]), len(grid)
    x_goal, y_goal = size_x * multiplier - 1, size_y * multiplier - 1
    risk_levels = defaultdict(int)
    came_from = defaultdict(tuple)

    queue = PriorityQueue()
    queue.put(start, 0)
    risk_levels[start] = 0
    came_from[start] = None

    neighbours = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    while not queue.empty():
        current = queue.get()
        if current == (x_goal, y_goal):
            break

        for nextp_offset in neighbours:
            nextp = (current[0] + nextp_offset[0], current[1] + nextp_offset[1])
            if nextp[0] > x_goal or nextp[0] < 0 or nextp[1] > y_goal or nextp[1] < 0:
                continue
            gy, gx = nextp
            adjusted_risk = (grid[gy % size_y][gx % size_x] + (gx // size_x) + (gy // size_y) - 1) % 9 + 1
            new_risk_level = risk_levels[current] + adjusted_risk
            if nextp not in risk_levels or new_risk_level < risk_levels[nextp]:
                risk_levels[nextp] = new_risk_level
                prio = new_risk_level + ((nextp[0] - y_goal) ** 2) + ((nextp[1] - x_goal) ** 2)
                queue.put(nextp, prio)
                came_from[nextp] = current
    return risk_levels[(y_goal, x_goal)]


def part1(risk_level_map):
    return find_lowest_risk(risk_level_map)


def part2(risk_level_map):
    return find_lowest_risk(risk_level_map, 5)


def run():
    risk_level_map = [[int(risk_level) for risk_level in row] for row in read_list_of_strings('day15')]
    print(f'Day 15 pt1: {part1(risk_level_map)}')
    print(f'Day 15 pt2: {part2(risk_level_map)}')

# Day 15 pt1: 527
# Day 15 pt2: 2887
