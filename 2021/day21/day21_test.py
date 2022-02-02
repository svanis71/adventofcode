import unittest


class Player:
    def __init__(self, startpos):
        self.score = 0
        self.space = startpos
        self.is_winner = False

    def move(self, steps):
        self.space = (self.space + steps)
        if self.space > 10:
            self.space %= 10
        self.score += self.space
        self.is_winner = self.score > 1000

    def is_a_winner(self):
        return self.is_winner


'''
This is how the game would go:

Player 1 rolls 1+2+3 and moves to space 10 for a total score of 10.
Player 2 rolls 4+5+6 and moves to space 3 for a total score of 3.
Player 1 rolls 7+8+9 and moves to space 4 for a total score of 14.
Player 2 rolls 10+11+12 and moves to space 6 for a total score of 9.
Player 1 rolls 13+14+15 and moves to space 6 for a total score of 20.
Player 2 rolls 16+17+18 and moves to space 7 for a total score of 16.
Player 1 rolls 19+20+21 and moves to space 6 for a total score of 26.
Player 2 rolls 22+23+24 and moves to space 6 for a total score of 22.
...after many turns...

Player 2 rolls 82+83+84 and moves to space 6 for a total score of 742.
Player 1 rolls 85+86+87 and moves to space 4 for a total score of 990.
Player 2 rolls 88+89+90 and moves to space 3 for a total score of 745.
Player 1 rolls 91+92+93 and moves to space 10 for a final score, 1000.
'''


def play_game(p1: Player, p2: Player):
    players = [p1, p2]
    moves, die, next_player = 3, 3, 0
    players[0].move(6)
    while True:
        next_player = next_player ^ 1
        steps = 0
        for i in range(3):
            die = 1 if die == 100 else die + 1
            steps += die
        players[next_player].move(steps)
        if players[next_player].is_a_winner():
            return moves * players[next_player ^ 1].score
        moves += 1
        die = 0 if die > 100 else die
    return moves * players[next_player ^ 1].score


class MyTestCase(unittest.TestCase):
    def test_something(self):
        indata = '''Player 1 starting position: 4
Player 2 starting position: 8'''
        p1, p2 = [Player(int(s[s.rindex(':') + 2:])) for s in indata.splitlines(False)]
        score = play_game(p1, p2)
        self.assertEqual(739785, score, 'Player 1 wins, player 2 ends with 745 points after 993 moves')


if __name__ == '__main__':
    unittest.main()
