import unittest

from day21 import Player, play_game


class MyTestCase(unittest.TestCase):
    def test_something(self):
        indata = '''Player 1 starting position: 4
Player 2 starting position: 8'''
        p1, p2 = [Player(int(s[7]), int(s[s.rindex(':') + 2:])) for s in indata.splitlines(False)]
        score = play_game(p1, p2)

        self.assertEqual(739785, score, 'Player 1 wins, player 2 ends with 745 points after 993 moves')


if __name__ == '__main__':
    unittest.main()
