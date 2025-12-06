def parse_inventory(input_text: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Parse the inventory database into ranges and ingredient IDs.

    The input consists of two sections separated by a blank line:
    - First section: Fresh ingredient ID ranges (e.g., "3-5" means 3, 4, 5 are fresh)
    - Second section: Available ingredient IDs to check (one per line)

    Args:
        input_text: Raw input text with ranges and IDs separated by a blank line

    Returns:
        Tuple of (ranges, ingredient_ids) where:
        - ranges: List of (start, end) tuples representing fresh ID ranges
        - ingredient_ids: List of ingredient IDs to check
    """
    sections = input_text.strip().split("\n\n")

    # Parse ranges from first section
    ranges = []
    for line in sections[0].strip().split("\n"):
        line = line.strip()
        if line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))

    # Parse ingredient IDs from second section
    ingredient_ids = []
    for line in sections[1].strip().split("\n"):
        line = line.strip()
        if line:
            ingredient_ids.append(int(line))

    return ranges, ingredient_ids
