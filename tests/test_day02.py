import unittest

from aoc.day02.parser import parse_ranges
from aoc.day02.solver import (
    is_invalid_id, find_invalid_in_range, solve_part1,
    is_invalid_id_part2, find_invalid_in_range_part2, solve_part2
)


EXAMPLE_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


class TestDay02(unittest.TestCase):
    def test_parse_ranges(self):
        ranges = parse_ranges(EXAMPLE_INPUT)
        self.assertEqual(len(ranges), 11)
        self.assertEqual(ranges[0], (11, 22))
        self.assertEqual(ranges[2], (998, 1012))

    def test_is_invalid_id(self):
        # Valid invalid IDs (repeated patterns)
        self.assertTrue(is_invalid_id(55))
        self.assertTrue(is_invalid_id(6464))
        self.assertTrue(is_invalid_id(123123))
        self.assertTrue(is_invalid_id(11))
        self.assertTrue(is_invalid_id(22))
        self.assertTrue(is_invalid_id(99))
        self.assertTrue(is_invalid_id(1010))

        # Not invalid (odd digits or non-repeating)
        self.assertFalse(is_invalid_id(101))  # odd number of digits
        self.assertFalse(is_invalid_id(1234))  # not repeating
        self.assertFalse(is_invalid_id(12))  # 1 != 2
        self.assertFalse(is_invalid_id(123))  # odd digits

    def test_find_invalid_range_11_22(self):
        invalid = find_invalid_in_range(11, 22)
        self.assertEqual(sorted(invalid), [11, 22])

    def test_find_invalid_range_95_115(self):
        invalid = find_invalid_in_range(95, 115)
        self.assertEqual(invalid, [99])

    def test_find_invalid_range_998_1012(self):
        invalid = find_invalid_in_range(998, 1012)
        self.assertEqual(invalid, [1010])

    def test_find_invalid_range_1188511880_1188511890(self):
        invalid = find_invalid_in_range(1188511880, 1188511890)
        self.assertEqual(invalid, [1188511885])

    def test_find_invalid_range_222220_222224(self):
        invalid = find_invalid_in_range(222220, 222224)
        self.assertEqual(invalid, [222222])

    def test_find_invalid_range_1698522_1698528(self):
        invalid = find_invalid_in_range(1698522, 1698528)
        self.assertEqual(invalid, [])

    def test_find_invalid_range_446443_446449(self):
        invalid = find_invalid_in_range(446443, 446449)
        self.assertEqual(invalid, [446446])

    def test_find_invalid_range_38593856_38593862(self):
        invalid = find_invalid_in_range(38593856, 38593862)
        self.assertEqual(invalid, [38593859])

    def test_example_part1(self):
        ranges = parse_ranges(EXAMPLE_INPUT)
        result = solve_part1(ranges)
        self.assertEqual(result, 1227775554)

    # Part 2 tests
    def test_is_invalid_id_part2(self):
        # Repeated twice (same as part 1)
        self.assertTrue(is_invalid_id_part2(55))
        self.assertTrue(is_invalid_id_part2(6464))
        self.assertTrue(is_invalid_id_part2(123123))

        # Repeated more than twice
        self.assertTrue(is_invalid_id_part2(111))  # 1 three times
        self.assertTrue(is_invalid_id_part2(999))  # 9 three times
        self.assertTrue(is_invalid_id_part2(123123123))  # 123 three times
        self.assertTrue(is_invalid_id_part2(1111111))  # 1 seven times
        self.assertTrue(is_invalid_id_part2(2121212121))  # 21 five times
        self.assertTrue(is_invalid_id_part2(565656))  # 56 three times
        self.assertTrue(is_invalid_id_part2(824824824))  # 824 three times

        # Not invalid
        self.assertFalse(is_invalid_id_part2(101))  # not repeating
        self.assertFalse(is_invalid_id_part2(1234))  # not repeating
        self.assertFalse(is_invalid_id_part2(12))  # 1 != 2

    def test_find_invalid_range_part2_95_115(self):
        invalid = find_invalid_in_range_part2(95, 115)
        self.assertEqual(sorted(invalid), [99, 111])

    def test_find_invalid_range_part2_998_1012(self):
        invalid = find_invalid_in_range_part2(998, 1012)
        self.assertEqual(sorted(invalid), [999, 1010])

    def test_find_invalid_range_part2_565653_565659(self):
        invalid = find_invalid_in_range_part2(565653, 565659)
        self.assertEqual(sorted(invalid), [565656])

    def test_find_invalid_range_part2_824824821_824824827(self):
        invalid = find_invalid_in_range_part2(824824821, 824824827)
        self.assertEqual(sorted(invalid), [824824824])

    def test_find_invalid_range_part2_2121212118_2121212124(self):
        invalid = find_invalid_in_range_part2(2121212118, 2121212124)
        self.assertEqual(sorted(invalid), [2121212121])

    def test_example_part2(self):
        ranges = parse_ranges(EXAMPLE_INPUT)
        result = solve_part2(ranges)
        self.assertEqual(result, 4174379265)


if __name__ == "__main__":
    unittest.main()
