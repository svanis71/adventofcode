from indata import read_list_of_strings


def dump_paper(paper):
    for row in paper:
        for col in row:
            print(col, end='')
        print()


def fold_y(from_line, paper):
    y1, y2 = 0, len(paper) - 1
    while y1 < y2:
        for x in range(len(paper[0])):
            if paper[y2][x] == '#':
                paper[y1][x] = paper[y2][x]
                paper[y2][x] = ' '
        y1, y2 = y1 + 1, y2 - 1
    paper = [[x for x in row] for y, row in enumerate(paper) if y < from_line]

    return paper


def fold_x(from_line, paper):
    x1, x2 = 0, len(paper[0]) - 1
    while x1 < x2:
        for y, row in enumerate(paper):
            if row[x2] == '#':
                paper[y][x1] = paper[y][x2]
                paper[y][x2] = ' '
        x1, x2 = x1 + 1, x2 - 1
    paper = [[row[x] for x in range(from_line)] for row in paper]
    return paper


def part1(folding_instructions, paper):
    dir, from_line = folding_instructions[0]
    if dir == 'y':
        paper = fold_y(from_line, paper)
    else:
        paper = fold_x(from_line, paper)
    return sum(row.count('#') for row in paper)


def part2(folding_instructions, paper):
    for (dir, from_line) in folding_instructions:
        if dir == 'y':
            paper = fold_y(from_line, paper)
        else:
            paper = fold_x(from_line, paper)
    dump_paper(paper)
    return sum(row.count('#') for row in paper)


def setup():
    coords = []
    folding_instructions = []
    for row in read_list_of_strings('day13'):
        if len(row) == 0:
            continue
        if row[0:4] != 'fold':
            col, row = row.split(',')
            coords.append((int(col), int(row)))
        else:
            direction, steps = row.split('=')
            folding_instructions.append((direction[-1], int(steps)))
    max_x = max(x for (x, y) in coords)
    max_y = max(y for (x, y) in coords)
    paper = [[' ' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for (x, y) in coords:
        paper[y][x] = '#'
    return folding_instructions, paper


def run():
    folding_instructions, paper = setup()
    print(f'Day 13 pt1: {part1(folding_instructions, paper)}')
    print(f'Day 13 pt2: {part2(folding_instructions, paper)}')

# Day 13 pt1: 842
# Day 13 pt2: BFKRCJZU
