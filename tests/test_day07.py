"""Tests for Day 7: Laboratories."""
import unittest

from aoc.day07.parser import parse_manifold
from aoc.day07.solver import solve_part1, solve_part2


EXAMPLE_INPUT = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


class TestDay07(unittest.TestCase):
    def test_parse_manifold(self):
        grid, start_col = parse_manifold(EXAMPLE_INPUT)
        self.assertEqual(len(grid), 16)
        self.assertEqual(start_col, 7)
        self.assertEqual(grid[0][start_col], 'S')

    def test_example_part1(self):
        grid, start_col = parse_manifold(EXAMPLE_INPUT)
        result = solve_part1(grid, start_col)
        self.assertEqual(result, 21)

    def test_example_part2(self):
        grid, start_col = parse_manifold(EXAMPLE_INPUT)
        result = solve_part2(grid, start_col)
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()
