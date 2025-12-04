def parse(input_text: str) -> list[str]:
    """Parse input into a grid (list of strings, one per row)."""
    return input_text.strip().split('\n')
