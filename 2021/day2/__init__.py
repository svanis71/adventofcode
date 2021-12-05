from indata import read_list_of_strings


def part1():
    commands = read_list_of_strings('day2', ' ')
    x, y = 0, 0
    for command in commands:
        direction, steps = command
        if direction == 'forward':
            x += int(steps)
        elif direction == 'up':
            y -= int(steps)
        elif direction == 'down':
            y += int(steps)
    return x * y


def part2():
    commands = read_list_of_strings('day2', ' ')
    x, y, aim = 0, 0, 0
    for command in commands:
        direction, steps = command[0], int(command[1])
        if direction == 'forward':
            x += steps
            y += (steps * aim)
        elif direction == 'up':
            aim -= steps
        elif direction == 'down':
            aim += steps
    return x * y


def run():
    print(f'Day 2 pt1: {part1()}')
    print(f'Day 2 pt2: {part2()}')

# Day 2 pt1: 1451208
# Day 2 pt2: 1620141160
