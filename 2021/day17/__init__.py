from re import findall


def part1():
    target_area = open('indata/day17.txt').readline().rstrip()
    _, _, ymin, _ = [int(x) for x in findall(r'(-?\d+)', target_area)]
    # Sum 1 to ymin
    return ymin * (ymin + 1) // 2

def part2():
    pass

def run():
    print(f'Day 17 pt1: {part1()}')
    print(f'Day 17 pt2: {part2()}')


# Day 17 pt1: 
# Day 17 pt2: 

