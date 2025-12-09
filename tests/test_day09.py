"""Tests for Day 09: Tile Floor Rectangle puzzle."""

import unittest

from aoc.day09.parser import parse_tiles
from aoc.day09.solver import solve_part1, solve_part2


EXAMPLE_INPUT = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


class TestDay09(unittest.TestCase):
    """Test cases for Day 09."""

    def test_parse_tiles(self):
        """Test that the parser correctly extracts tile coordinates."""
        tiles = parse_tiles(EXAMPLE_INPUT)
        self.assertEqual(len(tiles), 8)
        self.assertEqual(tiles[0], (7, 1))
        self.assertEqual(tiles[1], (11, 1))
        self.assertEqual(tiles[5], (2, 5))

    def test_solve_part1(self):
        """Test part 1 with the example input."""
        tiles = parse_tiles(EXAMPLE_INPUT)
        result = solve_part1(tiles)
        self.assertEqual(result, 50)

    def test_rectangle_area_calculation(self):
        """Test specific rectangle area calculations from the puzzle."""
        tiles = parse_tiles(EXAMPLE_INPUT)
        # Rectangle between (2,5) and (9,7) has area 24
        # width = |9-2| + 1 = 8, height = |7-5| + 1 = 3, area = 24
        # Rectangle between (7,1) and (11,7) has area 35
        # width = |11-7| + 1 = 5, height = |7-1| + 1 = 7, area = 35
        # Rectangle between (7,3) and (2,3) has area 6
        # width = |7-2| + 1 = 6, height = |3-3| + 1 = 1, area = 6
        result = solve_part1(tiles)
        # The maximum should be 50 (between 2,5 and 11,1)
        # width = |11-2| + 1 = 10, height = |5-1| + 1 = 5, area = 50
        self.assertEqual(result, 50)

    def test_solve_part2(self):
        """Test part 2 with the example input."""
        tiles = parse_tiles(EXAMPLE_INPUT)
        result = solve_part2(tiles)
        # Largest valid rectangle is 24 (between 9,5 and 2,3)
        self.assertEqual(result, 24)


if __name__ == "__main__":
    unittest.main()
