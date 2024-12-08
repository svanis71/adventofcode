import indata


def find_path(puzzle_input: list[str], obstructions_pos: list[tuple[int, int]],
              pos: tuple[int, int]) -> list[tuple[int, int]]:
    visited: list[tuple[int, int]] = []
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while 0 <= pos[0] < len(puzzle_input) and 0 <= pos[1] < len(puzzle_input):
        visited.append(pos)
        next_pos = (pos[0] + directions[0][0], pos[1] + directions[0][1])
        if 0 <= next_pos[0] < len(puzzle_input) and 0 <= next_pos[1] < len(
                puzzle_input) and next_pos in obstructions_pos:
            directions.append(directions.pop(0))
        else:
            pos = next_pos
    return visited


def part1(puzzle_input: list[str], obstructions_pos: list[tuple[int, int]], pos: tuple[int, int]) -> int:
    return len(set(find_path(puzzle_input, obstructions_pos, pos)))


def test_circular(puzzle_input: list[str], obstructions_pos: list[tuple[int, int]], start_pos: tuple[int, int]) -> bool:
    pos = start_pos
    obstruction_hits = {*()}
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while 0 <= pos[0] < len(puzzle_input) and 0 <= pos[1] < len(puzzle_input):
        next_pos = (pos[0] + directions[0][0], pos[1] + directions[0][1])
        if 0 <= next_pos[0] < len(puzzle_input) and 0 <= next_pos[1] < len(
                puzzle_input) and next_pos in obstructions_pos:
            hit_cnt = len(obstruction_hits)
            obstruction_hits.add((next_pos, directions[0]))
            if hit_cnt == len(obstruction_hits):
                return True
            directions.append(directions.pop(0))
        else:
            pos = next_pos
    return False


def part2(puzzle_input: list[str], obstructions_pos: list[tuple[int, int]], start_pos: tuple[int, int]) -> int:
    inital_path = list(set(find_path(puzzle_input, obstructions_pos, start_pos)))
    circ_count: int = 0
    for pos in inital_path[1:]:
        obs_test = obstructions_pos + [pos]
        if test_circular(puzzle_input, obs_test, start_pos):
            circ_count += 1
    return circ_count


def run():
    puzzle_data = indata.read_list_of_strings('day6', use_testdata=False)
    obstructions_pos: list[tuple[int, int]] = []

    pos: tuple[int, int] = (0, 0)
    for y, row in enumerate(puzzle_data):
        obstructions_pos += [(y, x) for x, cx in enumerate(row) if cx == '#']
        x = -1 if '^' not in row else row.index('^')
        if x >= 0:
            pos = (y, x)

    print(f'Day 6 pt1: {part1(puzzle_data, obstructions_pos, pos)}')
    print(f'Day 6 pt2: {part2(puzzle_data, obstructions_pos, pos)}')


# Day 6 pt1: 4903
# Day 6 pt2: 1911

if __name__ == '__main__':
    run()
