def parse_ranges(input_text: str) -> list[tuple[int, int]]:
    """Parse input into list of (start, end) range tuples.

    Args:
        input_text: Raw input text with comma-separated ranges (e.g., "11-22,95-115")

    Returns:
        List of tuples like [(11, 22), (95, 115), ...]
    """
    ranges = []
    # Remove whitespace and trailing comma
    text = input_text.strip().rstrip(",")

    for range_str in text.split(","):
        range_str = range_str.strip()
        if range_str:
            start, end = range_str.split("-")
            ranges.append((int(start), int(end)))

    return ranges
