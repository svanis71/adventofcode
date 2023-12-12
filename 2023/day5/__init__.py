from indata import read_list_of_strings


def part1():
    almanac = [line for line in read_list_of_strings('day5', use_testdata=False) if line != '']
    my_seeds = [int(i) for i in almanac.pop(0).split(': ').pop().split(' ')]
    almanac.pop(0)
    mapped_seeds = map_seeds(almanac, my_seeds)
    return min(mapped_seeds)


def part2():
    # Work in progress
    almanac = [line for line in read_list_of_strings('day5', use_testdata=False) if line != '']
    my_seeds = [int(i) for i in almanac.pop(0).split(': ').pop().split(' ')]
    almanac.pop(0)
    mapped_seeds = map_seeds(almanac, my_seeds)
    return min(mapped_seeds)


def map_seeds(almanac, my_seeds):
    the_map = []
    while len(almanac) > 0:
        next_row = almanac.pop(0)
        if next_row.endswith(':'):
            my_seeds = next_mapping(my_seeds, the_map)
            the_map.clear()
        else:
            the_map.append(tuple(int(i) for i in next_row.split(' ')))
    return my_seeds


def next_mapping(my_seeds, the_map):
    mapped_seeds = []
    for seed in my_seeds:
        found_mapping = False
        for mapping in the_map:
            dest, src, rng = mapping
            if src <= seed <= src + rng:
                mapped_seeds.append(seed + dest - src)
                found_mapping = True
                break
        if not found_mapping:
            mapped_seeds.append(seed)
    return mapped_seeds


def run():
    print(f'Day 5 pt1: {part1()}')
    print(f'Day 5 pt2: {part2()}')

# Day 5 pt1: 535088217
# Day 5 pt2:
