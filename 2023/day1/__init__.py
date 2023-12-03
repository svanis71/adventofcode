import re

from indata import read_list_of_strings


def part1():
    l: list[int] = []
    for row in read_list_of_strings('day1', use_testdata=False):
        digits: list[str] = re.findall(r'\d', row)
        l.append(int(digits[0] + digits[-1]))
    return sum(l)


def part2():
    numbers_in_text_pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    text_to_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    l: list[int] = []
    for row in read_list_of_strings('day1', use_testdata=False):
        digits = re.findall(numbers_in_text_pattern, row)
        first = digits[0] if digits[0].isnumeric() else str(text_to_num.index(digits[0]) + 1)
        last = digits[-1] if digits[-1].isnumeric() else str(text_to_num.index(digits[-1]) + 1)
        l.append(int(first + last))
    return sum(l)


def run():
    print(f'Day 1 pt1: {part1()}')
    print(f'Day 1 pt2: {part2()}')

# Day 1 pt1: 56506
# Day 1 pt2: 56017
