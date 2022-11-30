from datetime import datetime
from itertools import cycle

import indata


class Player:
    def __init__(self, playerno: int, startpos: int):
        self.score = 0
        self.space = startpos
        self.playerno = playerno

    def move(self, steps):
        self.space = (self.space + steps - 1) % 10 + 1
        self.score += self.space

    def is_a_winner(self):
        return self.score >= 1000


def deterministic_dice(sides: int):
    sides = cycle(range(1, sides + 1))
    while True:
        yield sum(next(sides) for _ in range(3))


def play_game(p1: Player, p2: Player):
    players = [p1, p2]
    moves = 0
    dice = deterministic_dice(100)
    player = cycle(players)
    while True:
        p = next(player)
        steps = next(dice)
        p.move(steps)
        moves += 3
        if p.is_a_winner():
            break
    p = next(player)
    return moves * p.score


def part1():
    startposistions = indata.read_list_of_strings('day21')
    p1, p2 = [Player(int(s[7]), int(s[s.rindex(':') + 2:])) for s in startposistions]
    return play_game(p1, p2)


def part2():
    pass


def run():
    start = datetime.now()
    print(f'Day 21 pt1: {part1()}')
    p1end = datetime.now()
    print(f'Day 21 pt2: {part2()}')
    p2end = datetime.now()
    print(f'Total time: {int((p2end - start).total_seconds() * 1000)} ms')

# Day 21 pt1: 
# Day 21 pt2:
