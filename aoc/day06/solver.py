from functools import reduce
from operator import add, mul


def solve_part1(problems: list[tuple[list[int], str]]) -> int:
    """Solve all problems and return the grand total.

    Each problem is a tuple of (numbers, operator).
    Apply the operator to all numbers in each problem,
    then sum all the results.

    Args:
        problems: List of (numbers, operator) tuples

    Returns:
        Grand total of all problem results
    """
    total = 0

    for numbers, operator in problems:
        if operator == '+':
            result = reduce(add, numbers)
        else:  # operator == '*'
            result = reduce(mul, numbers)
        total += result

    return total


def solve_part2(problems: list[tuple[list[int], str]]) -> int:
    """Solve all problems (Part 2) and return the grand total.

    Same logic as Part 1 - the difference is in how problems are parsed.

    Args:
        problems: List of (numbers, operator) tuples

    Returns:
        Grand total of all problem results
    """
    return solve_part1(problems)
