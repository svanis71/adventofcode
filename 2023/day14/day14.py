from collections import Counter

from indata import read_list_of_chars

NUM_CYCLES = 1_000_000_000


class Direction:
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    WEST = (0, -1)
    EAST = (0, 1)


def part1(platform: list[list[str]]) -> int:
    tilt_north(platform)
    return count_total_load(platform)


def part2(platform: list[list[str]]):
    cycle_count, loops, found_loop = 0, {}, False
    while cycle_count < NUM_CYCLES:
        state = run_cycle(platform)
        if not found_loop and state in loops:
            found_loop = True
            cycle_count = NUM_CYCLES - (NUM_CYCLES - cycle_count) % (cycle_count - loops[state])
        elif not found_loop:
            loops[state] = cycle_count
        cycle_count += 1

    return count_total_load(platform)


def count_total_load(platform):
    return sum(Counter(yr)['O'] * (len(platform) - yl) for yl, yr in enumerate(platform))


def run_cycle(platform: list[list[str]]):
    tilt_north(platform)
    tilt_west(platform)
    tilt_south(platform)
    tilt_east(platform)
    return tuple(''.join(x) for x in platform)


def tilt_north(platform, direction: Direction = Direction.NORTH) -> None:
    y_dir, x_dir = direction
    for iy, line in enumerate(platform):
        for ix, col in enumerate(line):
            if col == 'O':
                new_y, new_x = move_to((y_dir, x_dir), ix + x_dir, iy + y_dir, platform)
                platform[iy][ix], platform[new_y - y_dir][new_x - x_dir] = platform[new_y - y_dir][new_x - x_dir], \
                    platform[iy][ix]


def tilt_west(platform) -> None:
    y_dir, x_dir = Direction.WEST
    for iy, line in enumerate(platform):
        for ix, col in enumerate(line):
            if col == 'O':
                new_y, new_x = move_to((y_dir, x_dir), ix + x_dir, iy + y_dir, platform)
                platform[iy][ix], platform[new_y][new_x - x_dir] = platform[new_y][new_x - x_dir], platform[iy][ix]


def tilt_south(platform) -> None:
    y_dir, x_dir = Direction.SOUTH
    for iy in range(len(platform) - 1, -1, -1):  # iy, line in enumerate(platform):
        line: list[str] = platform[iy]
        for ix, _ in enumerate(line):  # range(len(line) - 1, 0, -1):
            col = line[ix]
            if col == 'O':
                new_y, new_x = move_to((y_dir, x_dir), ix + x_dir, iy + y_dir, platform)
                platform[iy][ix], platform[new_y - 1][new_x] = platform[new_y - 1][new_x], platform[iy][ix]


def tilt_east(platform, direction: Direction = Direction.EAST) -> None:
    y_dir, x_dir = direction
    for iy, line in enumerate(platform):
        for ix in range(len(line) - 1, -1, -1):
            col = line[ix]
            if col == 'O':
                new_y, new_x = move_to((y_dir, x_dir), ix + x_dir, iy + y_dir, platform)
                platform[iy][ix], platform[new_y - y_dir][new_x - x_dir] = platform[new_y - y_dir][new_x - x_dir], \
                    platform[iy][ix]


def move_to(direction: tuple[int, int], from_column: int, from_row: int, platform: list[list[str]]) -> tuple[int, int]:
    y_direction, x_direction = direction
    while 0 <= from_row < len(platform) and 0 <= from_column < len(platform) and platform[from_row][from_column] == '.':
        from_row += y_direction
        from_column += x_direction
    return from_row, from_column


def run():
    print(f"Day 14 pt1: {part1(read_list_of_chars('day14', use_testdata=False, splitchar=''))}")
    print(f"Day 14 pt2: {part2(read_list_of_chars('day14', use_testdata=False, splitchar=''))}")


# Day 14 pt1: 106990
# Day 14 pt2: 100531

if __name__ == '__main__':
    run()
