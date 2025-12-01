def parse_rotations(input_text: str) -> list[tuple[str, int]]:
    """Parse input into list of (direction, distance) tuples.

    Args:
        input_text: Raw input text with one rotation per line (e.g., "L68", "R48")

    Returns:
        List of tuples like [('L', 68), ('R', 48), ...]
    """
    rotations = []
    for line in input_text.strip().split("\n"):
        line = line.strip()
        if line:
            direction = line[0]
            distance = int(line[1:])
            rotations.append((direction, distance))
    return rotations
