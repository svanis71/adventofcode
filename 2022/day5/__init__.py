import re
from os.path import join

from indata import infiles_path


def read_input():
    with open(join(infiles_path, 'day5.txt'), encoding='utf-8') as f:
        content = ''.join(f.readlines())
    stack_data, rearrangement_data = content.split('\n\n')
    stacks = stack_data.split('\n')
    num_cols = len(re.findall(r'(\d+)(?=\s*)', stacks.pop()))
    stack_list = [[] for _ in range(num_cols)]
    for row in stacks:
        idx = row.index('[', 0)
        while idx != -1:
            c = row[idx + 1]
            stack_list[idx // 4].insert(0, c)
            idx = -1 if len(row) < (idx + 1) else row.find('[', idx + 1)
    return rearrangement_data, stack_list


def part1() -> str:
    rearrangement_data, stack = read_input()
    for move in rearrangement_data.split("\n"):
        num_items, from_col, to_col = re.findall(r'(\d+)', move)
        for _ in range(int(num_items)):
            stack[int(to_col) - 1].append(stack[int(from_col) - 1].pop())
    return ''.join(itm[-1] for itm in stack)


def part2():
    rearrangement_data, stack = read_input()
    for move in rearrangement_data.split("\n"):
        num_items, from_col, to_col = re.findall(r'(\d+)', move)
        tmp = [stack[int(from_col) - 1].pop() for _ in range(int(num_items))]
        for ic in reversed(tmp):
            stack[int(to_col) - 1].append(ic)
    return ''.join(itm[-1] for itm in stack)


def run():
    print(f'Day 5 pt1: {part1()}')
    print(f'Day 5 pt2: {part2()}')

# Day 5 pt1: NTWZZWHFV
# Day 5 pt2: BRZGFVBTJ
