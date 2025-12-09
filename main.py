from aoc.utils.input_reader import read_input
from aoc.day01.parser import parse_rotations
from aoc.day01.solver import solve_part1, solve_part2
from aoc.day02.parser import parse_ranges
from aoc.day02.solver import solve_part1 as solve_day02_part1, solve_part2 as solve_day02_part2
from aoc.day03.parser import parse_banks
from aoc.day03.solver import solve_part1 as solve_day03_part1, solve_part2 as solve_day03_part2
from aoc.day05.parser import parse_inventory
from aoc.day05.solver import solve_part1 as solve_day05_part1, solve_part2 as solve_day05_part2
from aoc.day06.parser import parse_worksheet, parse_worksheet_part2
from aoc.day06.solver import solve_part1 as solve_day06_part1, solve_part2 as solve_day06_part2
from aoc.day07.parser import parse_manifold
from aoc.day07.solver import solve_part1 as solve_day07_part1, solve_part2 as solve_day07_part2
from aoc.day08.parser import parse_junctions
from aoc.day08.solver import solve_part1 as solve_day08_part1, solve_part2 as solve_day08_part2
from aoc.day09.parser import parse_tiles
from aoc.day09.solver import solve_part1 as solve_day09_part1, solve_part2 as solve_day09_part2


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

    # Day 3
    print("\nDay 3: Lobby")
    input_text = read_input(3)
    banks = parse_banks(input_text)
    part1 = solve_day03_part1(banks)
    print(f"  Part 1: {part1}")
    part2 = solve_day03_part2(banks)
    print(f"  Part 2: {part2}")

    # Day 5
    print("\nDay 5: Cafeteria")
    input_text = read_input(5)
    ranges, ingredient_ids = parse_inventory(input_text)
    part1 = solve_day05_part1(ranges, ingredient_ids)
    print(f"  Part 1: {part1}")
    part2 = solve_day05_part2(ranges, ingredient_ids)
    print(f"  Part 2: {part2}")

    # Day 6
    print("\nDay 6: Trash Compactor")
    input_text = read_input(6)
    problems = parse_worksheet(input_text)
    part1 = solve_day06_part1(problems)
    print(f"  Part 1: {part1}")
    problems_p2 = parse_worksheet_part2(input_text)
    part2 = solve_day06_part2(problems_p2)
    print(f"  Part 2: {part2}")

    # Day 7
    print("\nDay 7: Laboratories")
    input_text = read_input(7)
    grid, start_col = parse_manifold(input_text)
    part1 = solve_day07_part1(grid, start_col)
    print(f"  Part 1: {part1}")
    part2 = solve_day07_part2(grid, start_col)
    print(f"  Part 2: {part2}")

    # Day 8
    print("\nDay 8: Playground")
    input_text = read_input(8)
    junctions = parse_junctions(input_text)
    part1 = solve_day08_part1(junctions)
    print(f"  Part 1: {part1}")
    part2 = solve_day08_part2(junctions)
    print(f"  Part 2: {part2}")

    # Day 9
    print("\nDay 9: Movie Theater")
    input_text = read_input(9)
    tiles = parse_tiles(input_text)
    part1 = solve_day09_part1(tiles)
    print(f"  Part 1: {part1}")
    part2 = solve_day09_part2(tiles)
    print(f"  Part 2: {part2}")


if __name__ == "__main__":
    main()
