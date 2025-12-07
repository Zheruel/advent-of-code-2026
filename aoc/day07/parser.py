"""Parser for Day 7: Laboratories puzzle."""


def parse_manifold(input_text: str) -> tuple[list[str], int]:
    """Parse the tachyon manifold grid and find the starting column.

    Args:
        input_text: The raw puzzle input containing the manifold diagram.

    Returns:
        Tuple of (grid as list of strings, starting column index where 'S' is located).
    """
    grid = input_text.strip().split('\n')

    # Find the starting position 'S' in the first row
    start_col = grid[0].index('S')

    return grid, start_col
