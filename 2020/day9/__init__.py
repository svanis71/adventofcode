from indata import read_list_of_integers

preamble_length = 25


def part1():
    numbers = read_list_of_integers('day9')
    preamble, found_error = [numbers.pop(0) for x in range(preamble_length)], -42

    while len(numbers) > 0 > found_error:
        cur = numbers.pop(0)
        ok = False
        for x in preamble:
            if cur - x in preamble and x != cur - x:
                ok = True
                break
        if not ok:
            return cur
        preamble.pop(0)
        preamble.append(cur)
    return -1


def part2(invalido):
    numbers = read_list_of_integers('day9')
    for ix, n in enumerate(numbers):
        tsum, endix = [n, numbers[ix + 1]], ix + 1
        while True:
            s = sum(tsum)
            if s == invalido:
                return min(tsum) + max(tsum)
            if s > invalido:
                break
            endix += 1
            tsum.append(numbers[endix])
    return -1


def run():
    invalido = part1()
    print(f'Day 9 part 1: {invalido}')
    print(f'Day 9 part 2: {part2(invalido)}')
