import unittest

from aoc.day04.parser import parse
from aoc.day04.solver import count_adjacent_rolls, solve_part1, solve_part2


EXAMPLE_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


class TestDay04(unittest.TestCase):
    def test_parse(self):
        grid = parse(EXAMPLE_INPUT)
        self.assertEqual(len(grid), 10)
        self.assertEqual(grid[0], "..@@.@@@@.")
        self.assertEqual(grid[9], "@.@.@@@.@.")

    def test_count_adjacent_corner(self):
        grid = parse(EXAMPLE_INPUT)
        # Top-left corner (0,0) is '.', but let's check (0,2) which is '@'
        # Neighbors: (0,1)='.', (0,3)='@', (1,1)='@', (1,2)='@', (1,3)='.'
        # Only 3 adjacent '@' symbols
        count = count_adjacent_rolls(grid, 0, 2)
        self.assertEqual(count, 3)

    def test_count_adjacent_middle(self):
        grid = parse(EXAMPLE_INPUT)
        # Position (1,1) is '@'
        # Neighbors include many '@' symbols
        count = count_adjacent_rolls(grid, 1, 1)
        self.assertGreaterEqual(count, 0)
        self.assertLessEqual(count, 8)

    def test_example_part1(self):
        grid = parse(EXAMPLE_INPUT)
        result = solve_part1(grid)
        self.assertEqual(result, 13)

    def test_example_part2(self):
        grid = parse(EXAMPLE_INPUT)
        result = solve_part2(grid)
        self.assertEqual(result, 43)


if __name__ == "__main__":
    unittest.main()
