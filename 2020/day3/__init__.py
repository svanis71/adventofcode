from indata import read_lines


def part1():
    return traverse(3, 1)


def part2():
    return traverse(5, 1) * traverse(1, 1) * traverse(3, 1) * traverse(7, 1) * traverse(1, 2)


def traverse(right_moves, down_moves):
    themap = read_lines('day3')
    height = len(themap)
    needed_width, mapwidth = height * right_moves, len(themap[0])
    xpos, trees, repeats = 0, 0, needed_width // mapwidth + 1
    for ypos in range(0, height, down_moves):
        trees = trees + 1 if (themap[ypos] * repeats)[xpos] == '#' else trees
        xpos += right_moves
    return trees


def run():
    print(f'Day 3 part 1: {part1()}')
    print(f'Day 3 part 2: {part2()}')
