from indata import read_list_of_strings


def part1():
    lines = read_list_of_strings('day10_test')
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    token_pairs = ['()', '[]', '{}', '<>']
    tokens = []
    score = 0
    for line in lines:
        for token in line:
            print(token)
            if token in ['(','[','{', '<']:
                tokens.append(token)
            else:
                test_token = tokens.pop()
                open_token = tokens.pop() 
                if not open_token + test_token in token_pairs:
                    score += scores[test_token]
    return scores


def part2():
    pass

def run():
    print(f'Day 10 pt1: {part1()}')
    print(f'Day 10 pt2: {part2()}')


# Day 10 pt1: 
# Day 10 pt2: 

