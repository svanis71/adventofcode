import re

from indata import read_infile


def part1(indata: str) -> int:
    running_sum: int = 0
    for mul in re.findall(r'(mul\(\d+,\d+\))', indata):
        n, m = mul.replace('mul(', '').replace(')', '').split(',')
        running_sum += int(n) * int(m)
    return running_sum


def part2(indata: str):
    running_sum: int = 0
    do: bool = True

    for mat in re.finditer(r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))', indata):
        val = indata[mat.start():mat.end()]
        match val:
            case "don't()":
                do = False
            case "do()":
                do = True
            case _:
                if do:
                    x, y = [int(x) for x in val[4:-1].split(',')]
                    running_sum += (x * y)
    return running_sum


def run():
    indata = read_infile('day3', use_testdata=False)
    print(f'Day 3 pt1: {part1(indata)}')
    print(f'Day 3 pt2: {part2(indata)}')


# Day 3 pt1: 183788984
# Day 3 pt2: 62098619

if __name__ == '__main__':
    run()
