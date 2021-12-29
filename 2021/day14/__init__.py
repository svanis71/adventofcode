from indata import read_list_of_strings


def calc_polymer(steps):
    indata = read_list_of_strings('day14')
    polymer_template = indata.pop(0)
    rules = {}
    for rule in indata:
        if rule == '': continue
        pair, element = rule.split(' -> ')
        rules[pair] = element
    for i in range(steps):
        last, next_polymer = '', ''

        for c1, c2 in zip(polymer_template, polymer_template[1:]):
            last = c2
            next_polymer += (c1 + rules[c1 + c2])
        polymer_template = next_polymer + last
    cnt = [polymer_template.count(letter) for letter in polymer_template]
    res = max(cnt) - min(cnt)
    return res


def part1():
    return calc_polymer(10)


def part2():
    return calc_polymer(40)


def run():
    print(f'Day 14 pt1: {part1()}')
#    print(f'Day 14 pt2: {part2()}')

# Day 14 pt1:
# Day 14 pt2:
