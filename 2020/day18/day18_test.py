import unittest

from . import eval_expr


class Part1Tests(unittest.TestCase):

    def test_p1_plus(self):
        self.assertEqual(3, eval_expr(list('1 + 2')))

    def test_p1_multiply(self):
        self.assertEqual(4, eval_expr(list('2 * 2')))

    def test_p1_simple(self):
        self.assertEqual(71, eval_expr(list('1 + 2 * 3 + 4 * 5 + 6')))

    def test_p1_ex1(self):
        self.assertEqual(26, eval_expr(list('2 * 3 + (4 * 5)')))

    def test_p1_simple_parenthensis(self):
        self.assertEqual(51, eval_expr(list('1 + (2 * 3) + (4 * (5 + 6))')))

    def test_p1_ex2(self):
        self.assertEqual(437, eval_expr(list('5 + (8 * 3 + 9 + 3 * 4 * 3)')))

    def test_p1_ex3(self):
        self.assertEqual(12240, eval_expr(list('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')))

    def test_p1_ex3(self):
        self.assertEqual(13632, eval_expr(list('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))


class Part2Tests(unittest.TestCase):

    def test_p2_basic(self):
        self.assertEqual(8, eval_expr(list('2 * 3 + 1'), True))

    def test_p2_simple(self):
        self.assertEqual(231, eval_expr(list('1 + 2 * 3 + 4 * 5 + 6'), True))

    def test_p2_ex1(self):
        self.assertEqual(46, eval_expr(list('2 * 3 + (4 * 5)'), True))

    def test_p2_ex2(self):
        self.assertEqual(1445, eval_expr(list('5 + (8 * 3 + 9 + 3 * 4 * 3)'), True))

    def test_p2_ex3(self):
        self.assertEqual(669060, eval_expr(list('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), True))

    def test_p2_ex4(self):
        self.assertEqual(23340, eval_expr(list('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), True))


if __name__ == '__main__':
    unittest.main()
