from indata import read_list_of_strings

XMAS = 'XMAS'


def is_xmas(indata: list[str], iy: int, ix: int) -> bool:
    directions: list[tuple[int, int]] = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    maxy, maxx = len(indata), len(indata[0])
    hit_count = 0
    for dy, dx in directions:
        y_edge, x_edge = 3 * dy + iy, 3 * dx + ix
        if 0 <= y_edge < maxy and 0 <= x_edge < maxx:
            if all(indata[iy + wx * dy][ix + wx * dx] == c for wx, c in enumerate(XMAS[1:], 1)):
                hit_count += 1
    return hit_count


def is_x_mas(indata: list[str], iy: int, ix: int) -> bool:
    maxy, maxx = len(indata), len(indata[0])
    if 0 < ix < maxx - 1 and 0 < iy < maxy - 1:
        mas1 = indata[iy - 1][ix - 1] + 'A' + indata[iy + 1][ix + 1]
        mas2 = indata[iy - 1][ix + 1] + 'A' + indata[iy + 1][ix - 1]
        return mas1 in ['MAS', 'SAM'] and mas2 in ['MAS', 'SAM']
    return False


def part1(indata: list[str]) -> int:
    xmas_cnt: int = 0
    for iy, row in enumerate(indata):
        for ix, c in enumerate(row):
            if c == 'X':
                xmas_cnt += is_xmas(indata, iy, ix)
    return xmas_cnt


def part2(indata: list[str]) -> int:
    xmas_cnt: int = 0
    for iy, row in enumerate(indata):
        for ix, c in enumerate(row):
            if c == 'A':
                xmas_cnt += 1 if is_x_mas(indata, iy, ix) else 0
    return xmas_cnt


def run():
    indata = read_list_of_strings('day4', use_testdata=True)
    print(f'Day 4 pt1: {part1(indata)}')
    print(f'Day 4 pt2: {part2(indata)}')


# Day 4 pt1: 2646
# Day 4 pt2: 2000

if __name__ == '__main__':
    run()
