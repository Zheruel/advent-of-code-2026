import unittest

from aoc.day05.parser import parse_inventory
from aoc.day05.solver import merge_ranges, is_fresh, solve_part1, solve_part2


EXAMPLE_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


class TestDay05(unittest.TestCase):
    def test_parse_inventory(self):
        ranges, ingredient_ids = parse_inventory(EXAMPLE_INPUT)
        self.assertEqual(len(ranges), 4)
        self.assertEqual(ranges[0], (3, 5))
        self.assertEqual(ranges[1], (10, 14))
        self.assertEqual(ranges[2], (16, 20))
        self.assertEqual(ranges[3], (12, 18))
        self.assertEqual(len(ingredient_ids), 6)
        self.assertEqual(ingredient_ids, [1, 5, 8, 11, 17, 32])

    def test_merge_ranges_no_overlap(self):
        ranges = [(1, 3), (5, 7), (10, 12)]
        merged = merge_ranges(ranges)
        self.assertEqual(merged, [(1, 3), (5, 7), (10, 12)])

    def test_merge_ranges_with_overlap(self):
        ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        merged = merge_ranges(ranges)
        # 10-14, 12-18, 16-20 should merge into 10-20
        self.assertEqual(merged, [(3, 5), (10, 20)])

    def test_merge_ranges_adjacent(self):
        ranges = [(1, 3), (4, 6)]
        merged = merge_ranges(ranges)
        self.assertEqual(merged, [(1, 6)])

    def test_merge_ranges_empty(self):
        merged = merge_ranges([])
        self.assertEqual(merged, [])

    def test_merge_ranges_single(self):
        merged = merge_ranges([(5, 10)])
        self.assertEqual(merged, [(5, 10)])

    def test_is_fresh_in_range(self):
        merged = [(3, 5), (10, 20)]
        self.assertTrue(is_fresh(5, merged))
        self.assertTrue(is_fresh(3, merged))
        self.assertTrue(is_fresh(4, merged))
        self.assertTrue(is_fresh(10, merged))
        self.assertTrue(is_fresh(15, merged))
        self.assertTrue(is_fresh(20, merged))

    def test_is_fresh_not_in_range(self):
        merged = [(3, 5), (10, 20)]
        self.assertFalse(is_fresh(1, merged))
        self.assertFalse(is_fresh(2, merged))
        self.assertFalse(is_fresh(6, merged))
        self.assertFalse(is_fresh(9, merged))
        self.assertFalse(is_fresh(21, merged))
        self.assertFalse(is_fresh(100, merged))

    def test_is_fresh_empty_ranges(self):
        self.assertFalse(is_fresh(5, []))

    def test_example_part1(self):
        ranges, ingredient_ids = parse_inventory(EXAMPLE_INPUT)
        result = solve_part1(ranges, ingredient_ids)
        self.assertEqual(result, 3)

    def test_individual_ids_from_example(self):
        ranges, _ = parse_inventory(EXAMPLE_INPUT)
        merged = merge_ranges(ranges)
        # ID 1: spoiled
        self.assertFalse(is_fresh(1, merged))
        # ID 5: fresh (in 3-5)
        self.assertTrue(is_fresh(5, merged))
        # ID 8: spoiled
        self.assertFalse(is_fresh(8, merged))
        # ID 11: fresh (in 10-20 after merge)
        self.assertTrue(is_fresh(11, merged))
        # ID 17: fresh (in 10-20 after merge)
        self.assertTrue(is_fresh(17, merged))
        # ID 32: spoiled
        self.assertFalse(is_fresh(32, merged))

    def test_example_part2(self):
        # Part 2: count total unique IDs covered by all ranges
        # Ranges 3-5, 10-14, 16-20, 12-18 merge to 3-5 (3 IDs) and 10-20 (11 IDs)
        # Total: 14 unique fresh IDs
        ranges, ingredient_ids = parse_inventory(EXAMPLE_INPUT)
        result = solve_part2(ranges, ingredient_ids)
        self.assertEqual(result, 14)


if __name__ == "__main__":
    unittest.main()
