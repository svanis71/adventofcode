from indata import read_lines


def part1():
    return max(get_seat_list())


def part2():
    seat_list = sorted(get_seat_list())
    for ix, seat_id in enumerate(seat_list):
        if seat_list[ix + 1] == seat_id + 2:
            return seat_id + 1


def get_seat_list():
    return [decode(boardingpass[0:7], 'F', 0, 127) * 8 + decode(boardingpass[7:], 'L', 0, 7) for boardingpass in
            (read_lines('day5'))]


def decode(code, code_lower, lo, hi):
    target = hi // 2
    for ch in code:
        if ch == code_lower:
            hi = target
        else:
            lo = target + 1
        target = lo + (hi - lo) // 2
    return target


def run():
    print(f'Day 5 part 1: {part1()}')
    print(f'Day 5 part 2: {part2()}')
