"""Parser for Day 09: Tile Floor Rectangle puzzle."""


def parse_tiles(input_text: str) -> list[tuple[int, int]]:
    """Parse red tile coordinates from input.

    Args:
        input_text: Raw puzzle input with one coordinate per line in "x,y" format.

    Returns:
        List of (x, y) tuples representing red tile positions.
    """
    tiles = []
    for line in input_text.strip().split("\n"):
        line = line.strip()
        if line:
            x, y = line.split(",")
            tiles.append((int(x), int(y)))
    return tiles
