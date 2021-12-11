from indata import read_list_of_strings


def get_adjacents(matrix, x, y):
    adjacents = []
    if x > 0: 
        adjacents.append(matrix[y][x - 1])
    if x < len(matrix[y]) - 1:
        adjacents.append(matrix[y][x + 1])
    if y > 0:
        adjacents.append(matrix[y - 1][x])
    if y < len(matrix) - 1:
        adjacents.append(matrix[y + 1][x])
    return adjacents

def part1():
    l = read_list_of_strings('day9')
    matrix = [ [int(i)for i in s] for s in l ]
    lowlevel_riskpoints = []
    for y, row in enumerate(matrix):
        for x, colval in enumerate(row):
            adjacents = get_adjacents(matrix, x, y)
            if len([x for x in adjacents if x <= colval]) == 0:
                print(f'\033[94m\033[1m{colval}\033[0m', end='')
                lowlevel_riskpoints.append(colval + 1)
            else:
                print(f'\033[96m{colval}\033[0m', end='')
        print()
    return sum(lowlevel_riskpoints)


def part2():
    pass

def run():
    print(f'Day 9 pt1: {part1()}')
    print(f'Day 9 pt2: {part2()}')


# Day 9 pt1: 
# Day 9 pt2: 

