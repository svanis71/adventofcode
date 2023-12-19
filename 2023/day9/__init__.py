from indata import read_list_of_strings


def part1(indata: list[list[int]]) -> int:
    extrapolated_values = []
    for line in indata:
        l, baseline = get_history(line)
        for ix, x in enumerate(reversed(baseline)):
            if l - ix > 0:
                baseline[l - ix - 1].append(x[-1] + baseline[l - ix - 1][-1])
            else:
                extrapolated_values.append(x[-1])

    return sum(extrapolated_values)


def part2(indata: list[list[int]]) -> int:
    extrapolated_values = []
    for line in indata:
        l, baseline = get_history(line)
        for ix, x in enumerate(reversed(baseline)):
            if l - ix > 0:
                baseline[l - ix - 1].insert(0, baseline[l - ix - 1][0] - x[0])
            else:
                extrapolated_values.append(x[0])

    return sum(extrapolated_values)


def get_history(line):
    basis = [line]
    while not all(x == 0 for x in basis[-1]):
        basis.append([])
        for l, r in zip(basis[-2], basis[-2][1:]):
            basis[-1].append(r - l)
    l = len(basis) - 1
    return l, basis


def run():
    indata = [[int(i) for i in l.split(' ')] for l in (read_list_of_strings('day9', use_testdata=False))]
    print(f'Day 9 pt1: {part1(indata)}')
    print(f'Day 9 pt2: {part2(indata)}')


# Day 9 pt1: 1708206096
# Day 9 pt2: 1050

if __name__ == '__main__':
    run()
