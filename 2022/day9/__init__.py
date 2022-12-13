from indata import read_list_of_strings


def move_head(dir, rope):
    match dir:
        case 'U':
            rope[0] = (rope[0][0], rope[0][1] - 1)
        case 'D':
            rope[0] = (rope[0][0], rope[0][1] + 1)
        case 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        case 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])


def follow_head(rope):
    for ti, t in enumerate(rope[1:], 1):
        diff_y = rope[ti - 1][0] - rope[ti][0]
        diff_x = rope[ti - 1][1] - rope[ti][1]

        if diff_y != 0:
            diff_y -= 1 if diff_y > 0 else -1

        if diff_x != 0:
            diff_x -= 1 if diff_x > 0 else -1

        if diff_y or diff_x:
            rope[ti] = (rope[ti - 1][0] - diff_y, rope[ti - 1][1] - diff_x)


def day9_12(moves: list[list[str]], rope_len: int) -> int:
    rope = [(0, 0) for _ in range(rope_len)]
    tail_path = set()

    for dir, steps in moves:
        for _ in range(int(steps)):
            move_head(dir, rope)
            follow_head(rope)
            tail_path.add(rope[-1])
    return len(tail_path)


def run():
    moves: list[list[str]] = [d.split(' ') for d in read_list_of_strings('day9')]
    print(f'Day 9 pt1: {day9_12(moves, 2)}')
    print(f'Day 9 pt1: {day9_12(moves, 10)}')

# Day 9 pt1: 6271
# Day 9 pt1: 2458
