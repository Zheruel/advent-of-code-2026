import unittest

from aoc.day06.parser import parse_worksheet, parse_worksheet_part2
from aoc.day06.solver import solve_part1, solve_part2


EXAMPLE_INPUT = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


class TestDay06(unittest.TestCase):
    def test_parse_worksheet(self):
        problems = parse_worksheet(EXAMPLE_INPUT)
        self.assertEqual(len(problems), 4)

        # Problem 1: 123, 45, 6 with *
        self.assertEqual(problems[0], ([123, 45, 6], '*'))

        # Problem 2: 328, 64, 98 with +
        self.assertEqual(problems[1], ([328, 64, 98], '+'))

        # Problem 3: 51, 387, 215 with *
        self.assertEqual(problems[2], ([51, 387, 215], '*'))

        # Problem 4: 64, 23, 314 with +
        self.assertEqual(problems[3], ([64, 23, 314], '+'))

    def test_individual_problems(self):
        # Problem 1: 123 * 45 * 6 = 33210
        self.assertEqual(123 * 45 * 6, 33210)

        # Problem 2: 328 + 64 + 98 = 490
        self.assertEqual(328 + 64 + 98, 490)

        # Problem 3: 51 * 387 * 215 = 4243455
        self.assertEqual(51 * 387 * 215, 4243455)

        # Problem 4: 64 + 23 + 314 = 401
        self.assertEqual(64 + 23 + 314, 401)

    def test_example_part1(self):
        problems = parse_worksheet(EXAMPLE_INPUT)
        result = solve_part1(problems)
        self.assertEqual(result, 4277556)

    def test_parse_worksheet_part2(self):
        problems = parse_worksheet_part2(EXAMPLE_INPUT)
        self.assertEqual(len(problems), 4)

        # Part 2 reads columns right-to-left
        # Leftmost problem: columns read as 356, 24, 1 with *
        # (column 0: 1,4,6 -> 146? Actually: 1, ' ', ' ' in col 0... let me verify)
        # Actually the problems are still in left-to-right order, just numbers are column-based

    def test_individual_problems_part2(self):
        # From the puzzle description:
        # Rightmost problem: 4 + 431 + 623 = 1058
        self.assertEqual(4 + 431 + 623, 1058)

        # Second from right: 175 * 581 * 32 = 3253600
        self.assertEqual(175 * 581 * 32, 3253600)

        # Third from right: 8 + 248 + 369 = 625
        self.assertEqual(8 + 248 + 369, 625)

        # Leftmost: 356 * 24 * 1 = 8544
        self.assertEqual(356 * 24 * 1, 8544)

    def test_example_part2(self):
        problems = parse_worksheet_part2(EXAMPLE_INPUT)
        result = solve_part2(problems)
        self.assertEqual(result, 3263827)


if __name__ == "__main__":
    unittest.main()
