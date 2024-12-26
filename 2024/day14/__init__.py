import math

import indata


def part1(robot_data: list[dict], edge_x: int = 101, edge_y: int = 103) -> int:
    for _ in range(100):
        for robot in robot_data:
            move_robot(edge_x, edge_y, robot)

    quads = [0, 0, 0, 0]
    for robot in robot_data:
        pos_x, pos_y = robot['pos']
        if pos_x < edge_x // 2 and pos_y < edge_y // 2:
            quads[0] += 1
        if pos_x > edge_x // 2 and pos_y < edge_y // 2:
            quads[1] += 1
        if pos_x < edge_x // 2 and pos_y > edge_y // 2:
            quads[2] += 1
        if pos_x > edge_x // 2 and pos_y > edge_y // 2:
            quads[3] += 1
    return math.prod(quads)


def move_robot(edge_x, edge_y, robot):
    cur_x, cur_y = robot["pos"]
    vel_x, vel_y = robot["velocity"]
    cur_x += vel_x
    if cur_x < 0 or cur_x >= edge_x:
        cur_x = cur_x % edge_x
    cur_y += vel_y
    if cur_y < 0 or cur_y >= edge_y:
        cur_y = cur_y % edge_y
    robot['pos'] = [cur_x, cur_y]


def check_for_tree(robot_data: list[dict]) -> bool:
    for robot in robot_data:
        if robot['pos'] == [0, 4]:
            return True
    return False

def part2(robot_data: list[dict], edge_x: int = 101, edge_y: int = 103) -> int:
    found_tree:bool = False
    turns:int = 0
    while not found_tree:
        turns += 1
        for robot in robot_data:
            move_robot(edge_x, edge_y, robot)
        found_tree = check_for_tree(robot_data)
    return turns


def run():
    puzzle_data = indata.read_list_of_strings('day14', use_testdata=True)
    robot_data: list[dict] = []
    for robot_id, line in enumerate(puzzle_data):
        p_string, v_string = line.split(' ')
        p = list(map(int, p_string[2:].split(',')))
        v = list(map(int, v_string[2:].split(',')))
        robot_data.append({"robot_id": robot_id, "pos": p, "velocity": v})
    # 0,4 3,-3
    print(f'Day 14 pt1: {part1(robot_data)}')
    print(f'Day 14 pt2: {part2(robot_data)}')


# Day 14 pt1: 229868730
# Day 14 pt2: 0

if __name__ == '__main__':
    run()
