from indata import read_list_of_chars


class Direction:
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    WEST = (0, -1)
    EAST = (0, 1)


def part1(platform: list[list[str]]) -> int:
    return tilt(platform)


def tilt(platform, direction=Direction.NORTH) -> int:
    total_load, south_edge = 0, len(platform)
    for iy, line in enumerate(platform):
        for ix, col in enumerate(line):
            if col == 'O':
                new_y, new_x = move_to(direction, ix, iy - 1, platform)
                platform[iy][ix], platform[new_y + 1][ix] = platform[new_y + 1][ix], platform[iy][ix]
                total_load += (south_edge - new_y - 1)
    return total_load

def run_cycle(platform: list[list[str]]):
    for direction in [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]:
        tilt(platform, direction)
def part2(platform: list[list[str]]):
    cycle_count = 0
    run_cycle(platform)
    state_0 = platform




def move_to(direction: tuple[int, int], from_column: int, from_row: int, platform: list[list[str]]) -> tuple[int, int]:
    y_direction, x_direction = direction
    while 0 <= from_row < len(platform) and 0 <= from_column < len(platform) and platform[from_row][from_column] == '.':
        from_row += y_direction
        from_column += x_direction
    return (from_row, from_column)

def run():
    print(f"Day 14 pt1: {part1(read_list_of_chars('day14', use_testdata=False, splitchar=''))}")
    print(f"Day 14 pt2: {part2(read_list_of_chars('day14', use_testdata=True, splitchar=''))}")


# Day 14 pt1: 106990
# Day 14 pt2:

if __name__ == '__main__':
    run()
