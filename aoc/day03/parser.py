def parse_banks(input_text: str) -> list[str]:
    """Parse input into list of battery bank strings.

    Args:
        input_text: Raw input text with one bank per line

    Returns:
        List of bank strings (each string is a sequence of digits)
    """
    banks = []
    for line in input_text.strip().split("\n"):
        line = line.strip()
        if line:
            banks.append(line)
    return banks
