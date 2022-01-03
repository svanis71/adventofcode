from collections import defaultdict
from re import findall


def get_vertical_velocity_hits(ymax, ymin):
    yspeed_steps = defaultdict(list)
    for y in range(ymin, abs(ymin) + 1):
        y_steps, cy, cvy = 0, 0, y
        while True:
            cy += cvy
            y_steps += 1
            if ymax >= cy >= ymin:
                yspeed_steps[y].append(y_steps)
            if cy < ymin:
                break
            cvy -= 1
    max_steps = max([max(i) for i in yspeed_steps.values()])
    return yspeed_steps, max_steps


def part1(target_area):
    _, _, ymin, _ = [int(x) for x in findall(r'(-?\d+)', target_area)]
    # Sum 1 to ymin
    return ymin * (ymin + 1) // 2


def part2(target_area):
    xmin, xmax, ymin, ymax = [int(x) for x in findall(r'(-?\d+)', target_area)]
    initvelocities = set([(x, y) for y in range(ymin, ymax + 1) for x in range(xmin, xmax + 1)])
    min_vx = int((2 * xmin) ** .5)
    yspeed_steps, max_steps = get_vertical_velocity_hits(ymax, ymin)

    for vx in range(min_vx - 1, xmax):
        step, x, cvx = 0, 0, vx
        while True:
            step += 1
            x += cvx
            cvx = 0 if cvx == 0 else cvx - 1
            if xmin <= x <= xmax:
                for yspeed, y_steps in yspeed_steps.items():
                    if step in y_steps:
                        initvelocities.add((vx, yspeed))
            if x > xmax or step > max_steps:
                break
    return len(initvelocities)


def run():
    target_area = open('indata/day17.txt').readline().rstrip()
    print(f'Day 17 pt1: {part1(target_area)}')
    print(f'Day 17 pt2: {part2(target_area)}')

# Day 17 pt1: 11781
# Day 17 pt2: 4531
