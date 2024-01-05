from indata import read_infile


def solve(indata: str, found_smudge: bool = True) -> int:
    patterns = indata.split('\n\n')
    summarize = []
    for pattern in patterns:
        data_lines = pattern.splitlines()
        summarize.append(mirror_count(data_lines, found_smudge) * 100)
        summarize.append(mirror_count([''.join([d[x] for d in data_lines]) for x in range(len(data_lines[0]))],
                                      found_smudge))
    return sum(summarize)


def mirror_count(pattern: list[str], found_smudge: bool) -> int:
    for ix, _ in enumerate(pattern, 1):
        if ix < len(pattern) and is_mirror(pattern, ix, found_smudge):
            return ix
    return 0


def is_mirror(pattern: list[str], ix: int, found_smudge: bool) -> bool:
    for front, end in zip(pattern[ix - 1::-1], pattern[ix:]):
        if front != end:
            if found_smudge:
                return False
            for left, right in zip(front, end):
                if left != right:
                    if found_smudge:
                        return False
                    found_smudge = True
    return found_smudge


def run():
    indata = read_infile('day13', use_testdata=False)
    print(f'Day 13 pt1: {solve(indata)}')
    print(f'Day 13 pt2: {solve(indata, found_smudge=False)}')


# Day 13 pt1: 37975
# Day 13 pt2: 32497

if __name__ == '__main__':
    run()
