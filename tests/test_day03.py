import unittest

from aoc.day03.parser import parse_banks
from aoc.day03.solver import max_joltage, solve_part1, max_joltage_k, solve_part2


EXAMPLE_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111"""


class TestDay03(unittest.TestCase):
    def test_parse_banks(self):
        banks = parse_banks(EXAMPLE_INPUT)
        self.assertEqual(len(banks), 4)
        self.assertEqual(banks[0], "987654321111111")
        self.assertEqual(banks[3], "818181911112111")

    def test_max_joltage_example1(self):
        # "987654321111111" -> 98 (first two batteries)
        result = max_joltage("987654321111111")
        self.assertEqual(result, 98)

    def test_max_joltage_example2(self):
        # "811111111111119" -> 89 (8 at start, 9 at end)
        result = max_joltage("811111111111119")
        self.assertEqual(result, 89)

    def test_max_joltage_example3(self):
        # "234234234234278" -> 78 (last two batteries)
        result = max_joltage("234234234234278")
        self.assertEqual(result, 78)

    def test_max_joltage_example4(self):
        # "818181911112111" -> 92 (9 at position 6, 2 at position 10)
        result = max_joltage("818181911112111")
        self.assertEqual(result, 92)

    def test_example_part1(self):
        banks = parse_banks(EXAMPLE_INPUT)
        result = solve_part1(banks)
        self.assertEqual(result, 357)

    # Part 2 tests
    def test_max_joltage_k_example1(self):
        # "987654321111111" -> 987654321111 (remove 3 trailing 1s)
        result = max_joltage_k("987654321111111", 12)
        self.assertEqual(result, 987654321111)

    def test_max_joltage_k_example2(self):
        # "811111111111119" -> 811111111119 (remove 3 middle 1s)
        result = max_joltage_k("811111111111119", 12)
        self.assertEqual(result, 811111111119)

    def test_max_joltage_k_example3(self):
        # "234234234234278" -> 434234234278 (remove 2,3,2 from start)
        result = max_joltage_k("234234234234278", 12)
        self.assertEqual(result, 434234234278)

    def test_max_joltage_k_example4(self):
        # "818181911112111" -> 888911112111 (remove 1s before 9)
        result = max_joltage_k("818181911112111", 12)
        self.assertEqual(result, 888911112111)

    def test_example_part2(self):
        banks = parse_banks(EXAMPLE_INPUT)
        result = solve_part2(banks)
        self.assertEqual(result, 3121910778619)


if __name__ == "__main__":
    unittest.main()
