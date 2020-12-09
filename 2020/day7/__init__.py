import re
from collections import defaultdict

from indata import read_lines


def drill(bags, rules):
    sum = 0
    for col in bags:
        if 'no other bags' in col:
            return 0
        numbags, color = re.match(r'(\d+)\s(.*)\sbags?', col).groups()
        sum += (int(numbags) + int(numbags) * drill(rules[color], rules))
    return sum


def add_parents(children, reslist, rules):
    if len(children) == 0:
        return reslist
    for col in children:
        reslist.append(col)
        add_parents([k for k, v in rules.items() if any(s for s in v if col in s)], reslist, rules)


def create_ruleset():
    rules = defaultdict(list)
    for ruleset in read_lines('day7'):
        key, value = ruleset.split(' contain ')
        singular_key = re.match(r'(.*)(?:\sbags?)', key).groups(0)[0]
        rules[singular_key] = value[0:-1].split(', ')
    return rules


def part1(rules):
    outerbags = directs = [k for k, v in rules.items() if any(s for s in v if 'shiny gold' in s)]
    for col in directs:
        add_parents([k for k, v in rules.items() if any(s for s in v if col in s)], outerbags, rules)
    return len(set(outerbags))


def part2(rules):
    sum = drill(rules['shiny gold'], rules)
    return sum


def run():
    rules = create_ruleset()
    print(f'Day 7 part 1: {part1(rules)}')
    print(f'Day 7 part 2: {part2(rules)}')
