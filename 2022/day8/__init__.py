from indata import read_infile


def part1(trees: list[list[int]]) -> int:
    width, height = len(trees[0]), len(trees)
    visuals = set([])
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            cur_tree_height = trees[y][x]
            if all(cur_tree_height > xi for xi in trees[y][:x]):  # left
                visuals.add((y, x))
            if all(cur_tree_height > xi for xi in trees[y][x + 1:]):  # right
                visuals.add((y, x))
            if all(cur_tree_height > xi for xi in [rv[x] for rv in [_ for _ in trees]][:y]):  # up
                visuals.add((y, x))
            if all(cur_tree_height > xi for xi in [rv[x] for rv in [_ for _ in trees]][y + 1:]):  # down
                visuals.add((y, x))

    return width * 2 + (height - 2) * 2 + len(visuals)


def part2(trees: list[list[int]]) -> int:
    width, height = len(trees[0]), len(trees)
    scores = []
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            cur_tree_height = trees[y][x]
            left = [xl for xl in reversed(trees[y][:x])]
            right = [xr for xr in trees[y][x + 1:]]
            up = [yu for yu in reversed([rv[x] for rv in [_ for _ in trees]][:y])]
            down = [yd for yd in [rv[x] for rv in [_ for _ in trees]][y + 1:]]

            score = 1
            for direction in [left, right, up, down]:
                for i, h in enumerate(direction, 1):
                    if cur_tree_height <= h or i == len(direction):
                        score *= i
                        break
            scores.append(score)
    return max(scores)


def run():
    trees = [[int(height) for height in line] for line in read_infile('day8').split('\n')]
    print(f'Day 8 pt1: {part1(trees)}')
    print(f'Day 8 pt2: {part2(trees)}')

# Day 8 pt1:
# Day 8 pt2:
