from indata import read_list_of_integers


def part1():
    input_data = read_list_of_integers('day1')
    while len(input_data) > 0:
        n1 = input_data.pop(0)
        nl2 = [n2 for n2 in input_data if n1 + n2 == 2020]
        if len(nl2):
            return n1, nl2[0], n1 * nl2[0]


def part2():
    input_data = read_list_of_integers('day1')
    while len(input_data) > 0:
        n1 = input_data.pop(0)
        for n2 in [x for x in input_data if n1 + x < 2020]:
            nl3 = [n3 for n3 in input_data[1:] if n1 + n2 + n3 == 2020]
            if len(nl3):
                n3 = nl3.pop(0)
                return n1, n2, n3, n1 * n2 * n3


def run():
    print('Day 1 part 1: %d * %d = %d' % part1())
    print('Day 1 part 2: %d * %d * %d = %d' % part2())
