import re
from collections import defaultdict
from indata.day3_input import first_wire_path, second_wire_path

d = {
    'R': {'x': 1, 'y': 0},
    'L': {'x': -1, 'y': 0},
    'U': {'x': 0, 'y': 1},
    'D': {'x': 0, 'y': -1}
}


def get_path(indata):
    points = set()
    steps = defaultdict(int)
    step_cnt, cx, cy = 1, 0, 0
    for move in indata:
        dir, length = re.findall(r'([UDRL])(\d+)', move)[0]
        for s in range(int(length)):
            cx = cx + d[dir]['x']
            cy = cy + d[dir]['y']
            points.add((cx, cy))
            steps[(cx, cy)] = step_cnt if steps[(cx, cy)] == 0 else steps[(cx, cy)]
            step_cnt += 1
    return points, steps


first, first_steps = get_path(first_wire_path)
second, second_steps = get_path(second_wire_path)

intersections = first & second

sums = [sum(map(abs, x)) for x in intersections]
print('Part 1:', min(sums))
print('Part 2:', min([first_steps[i] + second_steps[i] for i in intersections]))
