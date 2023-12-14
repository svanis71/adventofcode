from math import lcm

from indata import read_list_of_strings


def count_steps(start_nod: str, end_node: str, node_map: dict[str, tuple[str, str]], instructions: list[int]) -> int:
    instr_ptr, num_instr = 0, len(instructions)
    steps: int = 0
    current_node: str = start_nod
    while not current_node.endswith(end_node):
        current_node = node_map[current_node][instructions[instr_ptr]]
        steps += 1
        instr_ptr = (instr_ptr + 1) % num_instr
    return steps


def part1(indata: list[str], instructions: list[int]) -> int:
    nodes: dict[str, tuple[str, str]] = {}
    for line in indata:
        key, val = line.split(' = ')
        nodes[key] = tuple(val[1:-1].split(', '))
    return count_steps('AAA', 'ZZZ', nodes, instructions)


def part2(indata: list[str], instructions: list[int]) -> int:
    nodes: dict[str, tuple[str, str]] = {}
    nodes_end_with_a: list[str] = []
    for line in indata:
        key, val = line.split(' = ')
        nodes[key] = tuple(val[1:-1].split(', '))
        if key.endswith('A'):
            nodes_end_with_a.append(key)
    steps_list: list[int] = []
    while len(nodes_end_with_a) > 0:
        steps_list.append(count_steps(nodes_end_with_a.pop(), 'Z', nodes, instructions))
    return lcm(*steps_list)


def run():
    indata = read_list_of_strings('day8', use_testdata=False)
    instructions: list[int] = [0 if i == 'L' else 1 for i in indata.pop(0)]
    print(f'Day 8 pt1: {part1(indata[1:], instructions)}')
    print(f'Day 8 pt2: {part2(indata[1:], instructions)}')


if __name__ == '__main__':
    run()

# Day 8 pt1: 16897
# Day 8 pt2: 16563603485021
