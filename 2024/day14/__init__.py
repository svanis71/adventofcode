import math

import indata


def read_input(puzzle_data: list[str]) -> tuple:
    positions: list[tuple[int, int]] = []
    velocities: list[tuple[int, int]] = []
    for line in puzzle_data:
        p_string, v_string = line.split(' ')
        v = tuple(map(int, v_string[2:].split(',')))
        p = tuple(map(int, p_string[2:].split(',')))
        positions.append((p[0], p[1]))
        velocities.append((v[0], v[1]))
    return positions, velocities


def move_robot(edge_x, edge_y, robot: tuple[int, int], velocity: tuple[int, int]) -> tuple[int, int]:
    cur_x, cur_y = robot
    vel_x, vel_y = velocity
    return (cur_x + vel_x) % edge_x, (cur_y + vel_y) % edge_y


def part1(robot_data: list[str], edge_x: int = 101, edge_y: int = 103) -> int:
    positions, velocities = read_input(robot_data)
    for _ in range(100):
        for robot_id, robot in enumerate(positions):
            positions[robot_id] = move_robot(edge_x, edge_y, robot, velocities[robot_id])
    quads = [0, 0, 0, 0]
    for robot in positions:
        pos_x, pos_y = robot
        if pos_x < edge_x // 2 and pos_y < edge_y // 2:
            quads[0] += 1
        if pos_x > edge_x // 2 and pos_y < edge_y // 2:
            quads[1] += 1
        if pos_x < edge_x // 2 and pos_y > edge_y // 2:
            quads[2] += 1
        if pos_x > edge_x // 2 and pos_y > edge_y // 2:
            quads[3] += 1
    return math.prod(quads)


def part2(robot_data: list[str], edge_x: int = 101, edge_y: int = 103) -> int:
    positions, velocities = read_input(robot_data)
    turns: int = 0
    while len(set(positions)) != len(positions):
        for robot_id, robot in enumerate(positions):
            positions[robot_id] = move_robot(edge_x, edge_y, robot, velocities[robot_id])
        turns += 1

    return turns


def run():
    puzzle_data = indata.read_list_of_strings('day14', use_testdata=False)
    print(f'Day 14 pt1: {part1(puzzle_data)}')
    print(f'Day 14 pt2: {part2(puzzle_data)}')


# Day 14 pt1: 229868730
# Day 14 pt2: 7861

if __name__ == '__main__':
    run()
