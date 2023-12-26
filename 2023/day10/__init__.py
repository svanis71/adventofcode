from indata import read_list_of_strings


def east_west(from_x: int, to_x: int) -> bool:
    return from_x > to_x


def west_east(from_x: int, to_x: int) -> bool:
    return from_x < to_x


def north_south(from_y: int, to_y: int) -> bool:
    return from_y < to_y


def south_north(from_y: int, to_y: int) -> bool:
    return from_y > to_y


def get_neighbours(maze: list[str], nod: tuple[int, int]) -> list[tuple[int, int]]:
    neighbour_offsets = {"west": (0, -1), "east": (0, 1), "north": (-1, 0), "south": (1, 0)}
    nod_y, nod_x = nod
    neighbours = []
    for n in neighbour_offsets.values():
        y_offset, x_offset = n
        n_y, n_x = nod_y + y_offset, nod_x + x_offset
        if n_y < 0 or n_y >= len(maze) or n_x < 0 or n_x >= len(maze):
            continue
        if maze[nod_y + y_offset][nod_x + x_offset] != '.':
            neighbours.append((nod_y + y_offset, nod_x + x_offset))
    return neighbours


def is_connected(from_node: tuple[int, int], to_node: tuple[int, int], maze: list[str]) -> bool:
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile,
    # but your sketch doesn't show what shape the pipe has.
    from_y, from_x = from_node
    from_val = maze[from_y][from_x]
    to_y, to_x = to_node
    to_val = maze[to_y][to_x]
    if to_y != from_y:
        if south_north(from_y, to_y) and from_val in 'LJ|S' and to_val in '7F|S':
            return True
        if north_south(from_y, to_y) and from_val in '7F|S' and to_val in 'LJ|S':
            return True
    if to_x != from_x:  # check east west
        if east_west(from_x, to_x) and from_val in '7J-S' and to_val in 'FL-S':
            return True
        if west_east(from_x, to_x) and from_val in 'FL-S' and to_val in '7J-S':
            return True
    return False


def part1(maze: list[str]) -> int:
    start: tuple[int, int] = (0, 0)

    for r, row in enumerate(maze):
        c = -1 if 'S' not in row else row.index('S')
        if c >= 0:
            start = (r, c)
            break
    path = set()
    stack = [start]
    while len(stack) > 0:
        from_node = stack.pop()
        path.add(from_node)
        neighbours = get_neighbours(maze, from_node)
        for to_node in neighbours:
            if to_node in path:
                continue
            if is_connected(from_node, to_node, maze):
                stack.append(to_node)
    return (len(path) + 1) // 2


def part2(maze: list[str]):
    pass


def run():
    maze = read_list_of_strings('day10', use_testdata=False)
    print(f'Day 10 pt1: {part1(maze)}')
    print(f'Day 10 pt2: {part2(maze)}')


# Day 10 pt1: 6613
# Day 10 pt2:

if __name__ == '__main__':
    run()
