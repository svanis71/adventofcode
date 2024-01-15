from functools import cache

from indata import read_list_of_strings


@cache
def part1(layout: tuple[str], start_beam: tuple[int, int, int, int] = (0, -1, 0, 1)) -> int:
    energized: set[tuple[int, int]] = set()
    beams: set[tuple[int, int, int, int]] = {start_beam}
    beams_history: set[tuple[int, int, int, int]] = set()

    while len(beams) > 0:
        y, x, yd, xd = beams.pop()
        y += yd
        x += xd
        if y < 0 or x < 0 or y >= len(layout) or x >= len(layout[0]):
            continue
        energized.add((y, x))
        match layout[y][x]:
            case '|':
                if xd != 0:  # split to up/down
                    yd, xd, = 1, 0
                    if (y, x, -1, 0) not in beams_history:
                        beams.add((y, x, -1, 0))
                        beams_history.add((y, x, -1, 0))
            case '-':
                if yd != 0:
                    yd, xd, = 0, 1
                    beams.add((y, x, 0, -1))
            case '\\':
                yd, xd = xd, yd
            case '/':
                yd, xd = -xd, -yd
        if (y, x, yd, xd) not in beams_history:
            beams.add((y, x, yd, xd))
            beams_history.add((y, x, yd, xd))
    return len(energized)


def part2(indata: tuple[str]):
    ysize = len(indata)
    xsize = len(indata[0])
    # Point is tuple (y, x, y direction, x direction
    starting_points = [
        (0, 0, 1, 0), (0, 0, 0, 1),
        (ysize - 1, 0, -1, 0), (ysize - 1, 0, 0, 1),
        (0, xsize - 1, -1, 0), (0, xsize - 1, 0, -1),
        (ysize - 1, xsize - 1, -1, 0), (ysize - 1, xsize - 1, 0, -1)]

    for x in range(1, xsize - 1):
        starting_points.append((0, x, 1, 0))
        starting_points.append((ysize - 1, x, -1, 0))
    for y in range(1, ysize - 1):
        starting_points.append((y, 0, 0, 1))
        starting_points.append((y, xsize, 0, -1))

    return max(part1(indata, s) for s in starting_points)


def run():
    indata = tuple(read_list_of_strings('day16', use_testdata=False))
    print(f'Day 16 pt1: {part1(indata)}')
    print(f'Day 16 pt2: {part2(indata)}')


# Day 16 pt1: 7067
# Day 16 pt2: 7324

if __name__ == '__main__':
    run()
