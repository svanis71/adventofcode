from indata import read_list_of_strings


def part1():
    lines = read_list_of_strings('day10')
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    token_pairs = ['()', '[]', '{}', '<>']
    tokens = []
    score = 0
    for line in lines:
        for token in line:
            tokens.append(token)
            if token not in ['(', '[', '{', '<']:
                close_token, open_token = (tokens.pop(), tokens.pop())
                if not open_token + close_token in token_pairs:
                    score += scores[close_token]
    return score


def part2():
    lines = read_list_of_strings('day10')
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    token_pairs = ['()', '[]', '{}', '<>']
    scoreboard = []
    for line in lines:
        tokens, valid = [], True
        for token in line:
            tokens.append(token)
            if token not in ['(', '[', '{', '<']:
                close_token, open_token = (tokens.pop(), tokens.pop())
                if not open_token + close_token in token_pairs:
                    valid = False
                    break
        if valid:
            score = 0
            while len(tokens) > 0:
                last_token = tokens.pop()
                for pair in token_pairs:
                    if pair[0] == last_token:
                        score = score * 5 + scores[pair[-1]]
                        break
            scoreboard.append(score)
    return sorted(scoreboard)[int(len(scoreboard) / 2)]


def run():
    print(f'Day 10 pt1: {part1()}')
    print(f'Day 10 pt2: {part2()}')

# Day 10 pt1: 370407
# Day 10 pt2: 3249889609
