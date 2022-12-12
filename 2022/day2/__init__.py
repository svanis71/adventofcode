from indata import read_list_of_strings, read_infile


def points_in_round(me: str, opponent: str) -> int:
    if me == opponent:
        return 3
    if me == 'A' and opponent == 'C':
        return 6
    if me == 'C' and opponent == 'B':
        return 6
    if me == 'B' and opponent == 'A':
        return 6
    return 0


def points_for_needs_loss(opponent: str) -> int:
    if opponent == 'A':
        return 3
    if opponent == 'B':
        return 1
    return 2


def points_for_needs_win(opponent: str) -> int:
    if opponent == 'A':
        return 2
    if opponent == 'B':
        return 3
    return 1


def part1(strategy: list) -> int:
    scores = [points + points_in_round(me, opponent) for opponent, me, points in strategy]
    return sum(scores)


def part2(strategy: list) -> int:
    scores = []
    for opponent, me, _ in strategy:
        score = 0 if me == 'A' else 3 if me == 'B' else 6
        if me == 'A':
            score += points_for_needs_loss(opponent)
        if me == 'C':
            score += points_for_needs_win(opponent)
        if me == 'B':
            score += (ord(opponent) - ord('A') + 1)
        scores.append(score)
    return sum(scores)


def run():
    strategy = [(line[0], chr(ord(line[-1]) - 23), ord(line[-1]) - ord('W')) for line in read_list_of_strings('day2')]
    print(f'Day 2 pt1: {part1(strategy)}')
    print(f'Day 2 pt2: {part2(strategy)}')

# Day 2 pt1: 15422
# Day 2 pt2: 15442
