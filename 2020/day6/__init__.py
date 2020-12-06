from indata import day6_indata


def part1():
    groups = day6_indata()
    return sum(len(set(list(s.replace('\n', '')))) for s in groups)


def part2():
    everyone_yes = 0
    for group in [person.split('\n') for person in day6_indata()]:
        if len(group) == 1:
            everyone_yes += len(group.pop(0))
            continue
        for yes in group.pop(0):
            if all(yes in c for c in group):
                everyone_yes += 1

    return everyone_yes


def run():
    print(f'Day 6 part 1: {part1()}')
    print(f'Day 6 part 2: {part2()}')
