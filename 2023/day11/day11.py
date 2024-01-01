from indata import read_list_of_strings


def part1(expansion_size: int = 1):
    indata = read_list_of_strings('day11', use_testdata=True)
    galaxies, galaxy_pos = [], []
    insert_columns_here = [ic for ic, c in enumerate(indata) if '#' not in ''.join(c[ic] for c in indata)]
    for ir, r in enumerate(indata):
        expanded_row, offset = r, 1
        for ix, xc in enumerate(insert_columns_here):
            idx = xc + expansion_size * ix + 1
            expanded_row = expanded_row[:idx] + '.' * expansion_size + expanded_row[idx:]
        galaxies.append(expanded_row)
        if not any(True for c in r if c == '#'):
            galaxies += ['.'*len(expanded_row)]*expansion_size
    for ir, row in enumerate(galaxies):
        if not '#' in row:
            continue
        galaxy_pos += [(ir, ic) for ic, c in enumerate(row) if c == '#']
    path_len = []
    for ix, g1 in enumerate(galaxy_pos):
        for g2 in galaxy_pos[ix+1:]:
            path_len.append(abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]))
    return sum(path_len)

def part2():
    pass


def run():
    print(f'Day 11 pt1: {part1()}')
    print(f'Day 11 pt2: {part1(99)}')


# Day 11 pt1: 
# Day 11 pt2:

if __name__ == '__main__':
    run()
