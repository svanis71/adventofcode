import unittest

from day20 import calc_algo_value, solve


class MyTestCase(unittest.TestCase):
    indata = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#..#.
#....
##..#
..#..
..###'''

    def test_compute_algo_value(self):
        lines = self.indata.splitlines(False)
        image_data = [[1 if c == '#' else 0 for c in row] for row in lines[1:]]
        self.assertEqual(34, calc_algo_value(2, 2, image_data, 0))

    def test_simple_p1(self):
        enhanced_image, light_bits = solve(self.indata.splitlines(False), 2)
        for row in enhanced_image:
            for bit in row:
                print('.' if bit == 0 else '#', end='')
            print()
        self.assertEqual(35, [bit for row in enhanced_image for bit in row].count(1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
