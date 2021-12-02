from indata import read_list_of_strings


def part1():
    commands = read_list_of_strings('day2', ' ')
    x, y = 0, 0
    for command in commands:
        dir, steps = command
        if dir == 'forward':
            x += int(steps)
        elif dir == 'up':
            y -= int(steps)
        elif dir == 'down':
            y += int(steps)
    return x * y


def part2():
    commands = read_list_of_strings('day2', ' ')
    x, y, aim = 0, 0, 0
    for command in commands:
        dir, steps = command[0], int(command[1])
        if dir == 'forward':
            x += steps
            y += (steps * aim)
        elif dir == 'up':
            aim -= steps
        elif dir == 'down':
            aim += steps
    return x * y


def run():
    print(f'Day 2 pt1: {part1()}')
    print(f'Day 2 pt2: {part2()}')

# Day 2 pt1: 1451208
# Day 2 pt2: 1620141160
