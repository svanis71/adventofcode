import itertools

from indata import read_list_of_strings


def solution(indata: list[str], expansion_size: int = 1):
    galaxy_pos = []
    insert_columns_here = [ic for ic, c in enumerate(indata) if '#' not in ''.join(c[ic] for c in indata)]
    insert_rows_here = [ir for ir, r in enumerate(indata) if '#' not in r]

    for ir, row in enumerate(indata):
        if '#' in row:
            galaxy_pos += [(ir, ic) for ic, c in enumerate(row) if c == '#']

    adjusted_galaxy_pos = []
    for (y, x) in galaxy_pos:
        how_many_expansions_x = len([q for q in insert_columns_here if q < x])
        how_many_expansions_y = len([q for q in insert_rows_here if q < y])
        new_x = x + expansion_size * how_many_expansions_x
        new_y = y + expansion_size * how_many_expansions_y
        adjusted_galaxy_pos.append((new_y, new_x))
    return sum(abs(y2 - y1) + abs(x2 - x1) for (y1, x1), (y2, x2) in itertools.combinations(adjusted_galaxy_pos, 2))


def run():
    indata = read_list_of_strings('day11', use_testdata=False)
    print(f'Day 11 pt1: {solution(indata)}')
    print(f'Day 11 pt2: {solution(indata, 999999)}')


# Day 11 pt1: 9274989
# Day 11 pt2: 357134560737

if __name__ == '__main__':
    run()
