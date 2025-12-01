def solve_part1(rotations: list[tuple[str, int]]) -> int:
    """Solve part 1: count how many times the dial lands on 0.

    The dial has numbers 0-99 arranged in a circle, starting at 50.
    L rotates left (subtract), R rotates right (add).
    The dial wraps around (0-1=99, 99+1=0).

    Args:
        rotations: List of (direction, distance) tuples

    Returns:
        Number of times the dial points at 0 after a rotation
    """
    position = 50
    zero_count = 0

    for direction, distance in rotations:
        if direction == "L":
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def solve_part2(rotations: list[tuple[str, int]]) -> int:
    """Solve part 2: count every time the dial passes through or lands on 0.

    Unlike part 1, this counts every click that lands on 0, not just
    the final position after each rotation.

    Args:
        rotations: List of (direction, distance) tuples

    Returns:
        Total number of times the dial points at 0 during all rotations
    """
    position = 50
    zero_count = 0

    for direction, distance in rotations:
        if direction == "R":
            # Moving right: we hit 0 every time we wrap from 99 to 0
            zero_count += (position + distance) // 100
            position = (position + distance) % 100
        else:  # L
            # Moving left: we hit 0 every time we wrap from 0 to 99
            if position == 0:
                zero_count += distance // 100
            elif position <= distance:
                zero_count += (distance - position) // 100 + 1
            # else: position > distance, we never cross 0
            position = (position - distance) % 100

    return zero_count
