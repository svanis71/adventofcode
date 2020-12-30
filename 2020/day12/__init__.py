from indata import read_lines

directions = 'ESWN'
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North


def turn_left(cur_direction, degrees):
    cur = directions.find(cur_direction)
    deg = degrees // 90
    return directions[(cur - deg) % 4]


def turn_right(cur_direction, degrees):
    cur = directions.find(cur_direction)
    deg = degrees // 90
    return directions[(cur + deg) % 4]


def move_ferry(direction, cx, cy, steps):
    dx, dy = deltas[directions.find(direction)]
    return cx + dx * steps, cy + dy * steps


def manhattan_distance(cx, cy):
    return abs(cx) + abs(cy)


def part1():
    moves = read_lines('day12')
    cx, cy = 0, 0
    cur_direction = 'E'
    for move in moves:
        command, steps = move[0], int(move[1:])
        if command == 'F':
            cx, cy = move_ferry(cur_direction, cx, cy, steps)
        if command in directions:
            cx, cy = move_ferry(command, cx, cy, steps)
        elif command == 'L':
            cur_direction = turn_left(cur_direction, steps)
        elif command == 'R':
            cur_direction = turn_right(cur_direction, steps)
    return manhattan_distance(cx, cy)


def part2():
    moves = read_lines('day12')
    cx, cy, wx, wy = 0, 0, 10, -1
    for move in moves:
        command, steps = move[0], int(move[1:])
        if command == 'F':
            dwx, dwy = wx * steps, wy * steps
            cx, cy = cx + dwx, cy + dwy
        if command in directions:
            dx, dy = deltas[directions.find(command)]
            wx += (dx * steps)
            wy += (dy * steps)
        elif command == 'R':
            for i in range(steps // 90):
                wx, wy = -wy, wx
        elif command == 'L':
            for i in range(steps // 90):
                wx, wy = wy, -wx

    return abs(cx) + abs(cy)


def run():
    print(f'Day 12 part 1: {part1()}')
    print(f'Day 12 part 2: {part2()}')
