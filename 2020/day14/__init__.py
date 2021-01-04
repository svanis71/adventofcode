import re
from collections import defaultdict

from indata import read_lines


def part1():
    lines = read_lines('day14')
    mem = defaultdict(int)
    current_mask = ''
    for line in lines:
        cmd, val = line.split(' = ')
        if cmd == 'mask':
            current_mask = list(val)
        else:
            mempos = int(re.findall(r'(?:mem\[)(\d+)(?:\])', cmd).pop(0))
            binaryval = list(f'{int(val):b}'.rjust(36, '0'))
            newval = ''.join(
                [maskval if maskval != 'X' else bindig for maskval, bindig in zip(current_mask, binaryval)])
            mem[mempos] = int(newval, 2)
    return sum(mem.values())


def part2():
    lines = read_lines('day14')
    mem = defaultdict(int)
    current_mask = ''
    for line in lines:
        cmd, val = line.split(' = ')
        if cmd == 'mask':
            current_mask = list(val)
        else:
            mempos = int(re.findall(r'(?:mem\[)(\d+)(?:\])', cmd).pop(0))
            binaryval = list(f'{int(mempos):b}'.rjust(36, '0'))
            newval = [bindig if maskval == '0' else maskval for maskval, bindig in zip(current_mask, binaryval)]
            if not 'X' in newval:
                mem[mempos] = newval
            else:
                num_x = newval.count('X')
                for i in range(2 ** num_x):
                    t = list(f'{i:b}'.rjust(num_x, '0'))
                    tv = ''.join([c if c != 'X' else t.pop(0) for c in newval])
                    mem[int(tv, 2)] = int(val)
    return sum(mem.values())


def run():
    print(f'Day 14 part 1: {part1()}')  # 10717676595607
    print(f'Day 14 part 2: {part2()}')  # 3974538275659
