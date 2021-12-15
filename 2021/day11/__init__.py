from indata import read_list_of_strings

'''
You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

Before any steps:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

After step 1:
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2:
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848
'''


def find_adjacents(grid, x, y):
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)
    a = [(x + xoffset, y + yoffset) for (xoffset, yoffset) in adjacent_squares]
    return [(x, y) for (x, y) in a if x in range(len(grid[0])) and y in range(len(grid))]


def update_grid(grid):
    ng = [[c + 1 for c in r] for r in grid]
    for ir, r in enumerate(ng):
        for ic, c in enumerate(r):
            if c > 9:
                ng[ir][ic] = 0

    return ng


def do_step(grid, blink_cnt=0):
    ng = [[c + 1 for c in r] for r in grid]
    has_flashed = []
    while True:
        flashed = []
        for iy, row in enumerate(ng):
            for ix, colval in enumerate(row):
                if ng[iy][ix] > 9 and not (ix, iy) in has_flashed:
                    flashed.append((ix, iy))
                    for (nx, ny) in find_adjacents(ng, ix, iy):
                        ng[ny][nx] += 1
        if len(flashed) == 0:
            break
        has_flashed.extend(flashed)
    for iy, row in enumerate(ng):
        for ix, colval in enumerate(row):
            if colval > 9:
                ng[iy][ix] = 0
                blink_cnt += 1
    return ng, blink_cnt


def part1():
    grid = [[int(i) for i in s] for s in (read_list_of_strings('day11'))]
    blink_cnt = 0

    for step in range(100):
        grid, blink_cnt = do_step(grid, blink_cnt)

    return blink_cnt


def part2():
    grid = [[int(i) for i in s] for s in (read_list_of_strings('day11'))]
    step, all_flashed, octopusses = 0, False, len(grid) * len(grid[0])
    while not all_flashed:
        step += 1
        (grid, ign) = do_step(grid=grid)
        all_flashed = [colval for row in grid for colval in row].count(0) == octopusses

    return step


def run():
    print(f'Day 11 pt1: {part1()}')
    print(f'Day 11 pt2: {part2()}')

# Day 11 pt1: 1627
# Day 11 pt2: 329
