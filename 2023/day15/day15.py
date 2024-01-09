from collections import defaultdict

from indata import read_infile


def part1(indata: list[str]):
    return sum(calc_hash(s) for s in indata)


def part2(indata: list[str]):
    hashmap: defaultdict[int, list[tuple[str, int]]] = defaultdict(list[tuple[str, int]])
    for step in indata:
        op: str = '-' if step.endswith('-') else '='
        label, focal_length = step.split(op)
        hashcode = calc_hash(label)
        idx: int = find_label(label, hashmap[hashcode])
        if op == '=':
            new_item = (label, int(focal_length))
            if idx < 0:
                hashmap[hashcode].append(new_item)
            else:
                hashmap[hashcode].insert(idx + 1, new_item)
                hashmap[hashcode].pop(idx)
        elif idx > -1:
            hashmap[hashcode].pop(idx)
    s = []
    for boxno, box in hashmap.items():
        for slotno, slot in enumerate(box, 1):
            _, focal_length = slot
            s.append((boxno + 1) * slotno * focal_length)
    return sum(s)


def calc_hash(s: str) -> int:
    """
        Determine the ASCII code for the current character of the string.
        Increase the current value by the ASCII code you just determined.
        Set the current value to itself multiplied by 17.
        Set the current value to the remainder of dividing itself by 256.

    :param s:str string to hash
    :return: hashcode as int
    """
    ts = 0
    for c in s:
        ts += ord(c)
        ts *= 17
        ts = ts % 256
    return ts


def find_label(search_label: str, box: list[tuple[str, int]]) -> int:
    idx : int
    for idx, (label, _) in enumerate(box):
        if label == search_label:
            return idx
    return -1


def run():
    indata: list[str] = read_infile('day15', use_testdata=False).split(',')
    print(f'Day 15 pt1: {part1(indata)}')
    print(f'Day 15 pt2: {part2(indata)}')


# Day 15 pt1: 513214
# Day 15 pt2: 258826

if __name__ == '__main__':
    run()
