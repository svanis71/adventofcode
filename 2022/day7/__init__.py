from collections import defaultdict

from indata import read_list_of_strings


def create_disk_usage(verbose:bool = False):
    commands = [s if not s[0] == '$' else s[1:] for s in read_list_of_strings('day7', ' ')][1:]
    path, sizes, current_total = ['/'], defaultdict(int), 0
    for cmd_line in commands:
        if cmd_line[0] == 'cd':
            arg = cmd_line[1]
            if arg == '..':
                sizes['/'.join(path)] = current_total
                path.pop()
                current_total += sizes['/'.join(path)]
            else:
                sizes['/'.join(path)] = current_total
                path.append(arg)
                current_total = sizes['/'.join(path)]

        if cmd_line[0].isdigit():
            current_total += int(cmd_line[0])
    while len(path) > 1:
        sizes['/'.join(path)] = current_total
        path.pop()
        current_total += sizes['/'.join(path)]
    sizes['/'] = current_total
    if verbose:
        for k, v in sizes.items():
            print(f'dir: {k}, size: {v}')
    return sizes


def part1(max_size: int, sizes: defaultdict) -> int:
    return sum(v for v in sizes.values() if v <= max_size)


def part2(total_space: int, min_unused_space: int, disk_usage: defaultdict) -> int:
    space_needed = min_unused_space - (total_space - disk_usage['/'])
    return min(x for x in sorted(disk_usage.values()) if x > space_needed)


def run():
    usage = create_disk_usage()
    print(f'Day 7 pt1: {part1(100000, usage)}')
    print(f'Day 7 pt2: {part2(70000000, 30000000, usage)}')

# Day 7 pt1:
# Day 7 pt2:
