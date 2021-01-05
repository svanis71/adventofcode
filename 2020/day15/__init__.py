from collections import defaultdict


def part1(indata, max_turns=2020):
    turn, lastspoken = 1, 0
    history = defaultdict(list)
    previous = {}
    nextprevious = {}
    while True:
        if len(indata) > 0:
            lastspoken = int(indata.pop(0))
        else:
            if len(history[lastspoken]) <= 1:
                lastspoken = 0
            else:
                # lastspoken = previous[lastspoken]
                lastspoken = history[lastspoken][0] - history[lastspoken][1]
        history[lastspoken].insert(0, turn)
        turn += 1
        if turn > max_turns:
            break
    return lastspoken




def part2(indata):
    return part1(indata, 30*10**6)


def run():
    print(f'Day 14 part 1: {part1("1,12,0,20,8,16".split(","))}')
    print(f'Day 14 part 2: {part2("3,1,2".split(","))}')

run()