import re


def read_list_of_integers(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_lines(day):
    with open('indata/%s.txt' % day) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def day6_indata():
    with open('indata/day6.txt') as f:
        content = f.read()
    groups = re.split(r'\n\n', content)
    return [person for person in groups]
