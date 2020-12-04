import re

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

field_map = {
    'byr': lambda x: re.match(r'^19[2-9]\d|200[0-2]$', x) is not None,
    'iyr': lambda x: re.match(r'^201\d|2020$', x) is not None,
    'eyr': lambda x: re.match(r'^202\d|2030$', x) is not None,
    'hgt': lambda x: re.match(r'^(?:1([5-8]\d)|(19[0-3]))cm$', x) is not None or \
                     re.match(r'^(?:(59)|(6\d)|(7[0-6]))in$', x) is not None,
    'hcl': lambda x: re.match(r'^[#][0-9a-f]{6}$', x) is not None,
    'ecl': lambda x: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x) is not None,
    'pid': lambda x: re.match(r'^\d{9}$', x) is not None,
    'cid': lambda x: True
}


def get_passports(batch):
    valid_passports = []
    for passport in re.split(r'\n\n', batch):
        fields = passport.replace('\n', ' ').split(' ')
        if len(fields) >= 7:
            valid_fields = [n for n, v in [f.split(':') for f in fields] if n in field_map or n == 'cid']
            if 'cid' not in valid_fields:
                valid_fields.append('cid')
            if len(valid_fields) == 8:
                valid_passports.append(passport.replace('\n', ' '))
    return valid_passports


def get_validated_passports(passports):
    valids = []
    for pp in passports:
        invalido = [False for n, v in [x.split(':') for x in [x for x in [f for f in pp.split(' ')]]] if
                    not field_map[n](v)]
        if len(invalido) == 0:
            valids.append(pp)
    return valids


def part1():
    with open('indata/day4.txt') as f:
        content = f.read()
    valid_passports = get_passports(content)
    return len(valid_passports)


def part2():
    with open('indata/day4.txt') as f:
        content = f.read()
    valid_passports = get_validated_passports(get_passports(content))
    return len(valid_passports)


def run():
    print(f'Day 4 part 1: {part1()}')
    print(f'Day 4 part 2: {part2()}')
