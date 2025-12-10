"""Tests for Day 10: Factory puzzle."""
import unittest

from aoc.day10.parser import parse_input
from aoc.day10.solver import solve_part1, solve_part2, solve_machine, solve_joltage_ilp


EXAMPLE_INPUT = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


class TestDay10Parser(unittest.TestCase):
    """Test the parser."""

    def test_parse_example(self):
        """Test parsing the example input."""
        machines = parse_input(EXAMPLE_INPUT)
        self.assertEqual(len(machines), 3)

        # First machine: [.##.]
        target, buttons, joltages = machines[0]
        self.assertEqual(target, [False, True, True, False])
        self.assertEqual(buttons, [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]])
        self.assertEqual(joltages, [3, 5, 4, 7])

        # Second machine: [...#.]
        target, buttons, joltages = machines[1]
        self.assertEqual(target, [False, False, False, True, False])
        self.assertEqual(buttons, [[0, 2, 3, 4], [2, 3], [0, 4], [0, 1, 2], [1, 2, 3, 4]])

        # Third machine: [.###.#]
        target, buttons, joltages = machines[2]
        self.assertEqual(target, [False, True, True, True, False, True])
        self.assertEqual(len(buttons), 4)


class TestDay10Solver(unittest.TestCase):
    """Test the solver."""

    def test_first_machine(self):
        """Test solving the first machine - should be 2 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        target, buttons, _ = machines[0]
        result = solve_machine(target, buttons)
        self.assertEqual(result, 2)

    def test_second_machine(self):
        """Test solving the second machine - should be 3 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        target, buttons, _ = machines[1]
        result = solve_machine(target, buttons)
        self.assertEqual(result, 3)

    def test_third_machine(self):
        """Test solving the third machine - should be 2 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        target, buttons, _ = machines[2]
        result = solve_machine(target, buttons)
        self.assertEqual(result, 2)

    def test_part1_example(self):
        """Test part 1 with example input - should be 7."""
        machines = parse_input(EXAMPLE_INPUT)
        result = solve_part1(machines)
        self.assertEqual(result, 7)


class TestDay10Part2(unittest.TestCase):
    """Test Part 2 solver."""

    def test_first_machine_joltage(self):
        """Test joltage for first machine - should be 10 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        _, buttons, joltages = machines[0]
        result = solve_joltage_ilp(buttons, joltages)
        self.assertEqual(result, 10)

    def test_second_machine_joltage(self):
        """Test joltage for second machine - should be 12 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        _, buttons, joltages = machines[1]
        result = solve_joltage_ilp(buttons, joltages)
        self.assertEqual(result, 12)

    def test_third_machine_joltage(self):
        """Test joltage for third machine - should be 11 presses."""
        machines = parse_input(EXAMPLE_INPUT)
        _, buttons, joltages = machines[2]
        result = solve_joltage_ilp(buttons, joltages)
        self.assertEqual(result, 11)

    def test_part2_example(self):
        """Test part 2 with example input - should be 33."""
        machines = parse_input(EXAMPLE_INPUT)
        result = solve_part2(machines)
        self.assertEqual(result, 33)


if __name__ == '__main__':
    unittest.main()
