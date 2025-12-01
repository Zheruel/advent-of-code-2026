import unittest

from aoc.day01.parser import parse_rotations
from aoc.day01.solver import solve_part1, solve_part2


EXAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class TestDay01(unittest.TestCase):
    def test_parse_rotations(self):
        rotations = parse_rotations(EXAMPLE_INPUT)
        self.assertEqual(len(rotations), 10)
        self.assertEqual(rotations[0], ("L", 68))
        self.assertEqual(rotations[2], ("R", 48))

    def test_example_part1(self):
        rotations = parse_rotations(EXAMPLE_INPUT)
        result = solve_part1(rotations)
        self.assertEqual(result, 3)

    def test_wrap_left_from_zero(self):
        # Starting at 50, L50 goes to 0, then L1 should go to 99
        rotations = [("L", 50), ("L", 1)]
        result = solve_part1(rotations)
        # First rotation lands on 0, second lands on 99
        self.assertEqual(result, 1)

    def test_wrap_right_from_99(self):
        # Starting at 50, R49 goes to 99, then R1 should go to 0
        rotations = [("R", 49), ("R", 1)]
        result = solve_part1(rotations)
        # First rotation lands on 99, second lands on 0
        self.assertEqual(result, 1)

    def test_example_part2(self):
        rotations = parse_rotations(EXAMPLE_INPUT)
        result = solve_part2(rotations)
        self.assertEqual(result, 6)

    def test_part2_r1000_from_50(self):
        # R1000 from 50 should hit 0 ten times (at 100, 200, ..., 1000)
        rotations = [("R", 1000)]
        result = solve_part2(rotations)
        # (50 + 1000) // 100 = 10
        self.assertEqual(result, 10)

    def test_part2_multiple_wraps_left(self):
        # L250 from 50 should hit 0 three times
        # First at step 50 (position 0), then 150 (position 0), then 250 (position 0)
        # Actually: 50 -> -200 = 50-250 mod 100 = -200 mod 100 = 0? No wait...
        # 50 - 250 = -200, -200 mod 100 = 0 (in Python)
        # Steps where we hit 0: 50, 150, 250
        # Count: (250 - 50) // 100 + 1 = 200 // 100 + 1 = 3
        rotations = [("L", 250)]
        result = solve_part2(rotations)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
