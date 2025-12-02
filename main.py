from aoc.utils.input_reader import read_input
from aoc.day01.parser import parse_rotations
from aoc.day01.solver import solve_part1, solve_part2
from aoc.day02.parser import parse_ranges
from aoc.day02.solver import solve_part1 as solve_day02_part1, solve_part2 as solve_day02_part2


def main():
    print("Advent of Code 2026")
    print("=" * 40)

    # Day 1
    print("\nDay 1: Secret Entrance")
    input_text = read_input(1)
    rotations = parse_rotations(input_text)
    part1 = solve_part1(rotations)
    print(f"  Part 1: {part1}")
    part2 = solve_part2(rotations)
    print(f"  Part 2: {part2}")

    # Day 2
    print("\nDay 2: Gift Shop")
    input_text = read_input(2)
    ranges = parse_ranges(input_text)
    part1 = solve_day02_part1(ranges)
    print(f"  Part 1: {part1}")
    part2 = solve_day02_part2(ranges)
    print(f"  Part 2: {part2}")


if __name__ == "__main__":
    main()
