def part1():
    with open('indata/day6.txt') as f:
        lanternfishes = [int(x) for x in f.readline().split(',')]
    for day in range(0, 80):
        next_day_lanternfishes = []
        newborns = []
        for fish in lanternfishes:
            if fish > 0:
                next_day_lanternfishes.append(fish - 1)
            else:
                next_day_lanternfishes.append(6)
                newborns.append(8)
        next_day_lanternfishes += newborns
        lanternfishes = next_day_lanternfishes.copy()
    return len(lanternfishes)


def part2():
    with open('indata/day6_test.txt') as f:
        lanternfishes = [int(x) for x in f.readline().split(',')]
    fishtionary = {0: lanternfishes.count(0), 1: lanternfishes.count(1), 2: lanternfishes.count(2), 
        3: lanternfishes.count(3), 4: lanternfishes.count(4), 5: lanternfishes.count(5), 6: lanternfishes.count(6), 8: 0}
    for day in range(256):
        new_day = {}
        for (age,cnt) in fishtionary.items():
            if age == 0:
                new_day[8] = new_day[6] = cnt
            else:
                new_day[age - 1] = cnt
        fishtionary = new_day        
    return fishtionary           

def run():
    # print(f'Day 6 pt1: {part1()}')
    print(f'Day 6 pt2: {part2()}')
