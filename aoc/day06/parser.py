def parse_worksheet(input_text: str) -> list[tuple[list[int], str]]:
    """Parse the worksheet into a list of problems.

    Each problem is a tuple of (numbers, operator) where:
    - numbers: list of integers to be combined
    - operator: '+' or '*'

    Problems are arranged vertically with numbers stacked and the operator at the bottom.
    Problems are separated by columns that contain only spaces.

    Args:
        input_text: Raw worksheet text

    Returns:
        List of (numbers, operator) tuples for each problem
    """
    lines = input_text.rstrip('\n').split('\n')
    if not lines:
        return []

    # Pad all lines to the same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    num_rows = len(lines)
    num_cols = max_len

    # Find separator columns (all spaces in that column)
    separator_cols = set()
    for col in range(num_cols):
        if all(lines[row][col] == ' ' for row in range(num_rows)):
            separator_cols.add(col)

    # Find problem regions (consecutive non-separator columns)
    problems = []
    start_col = None

    for col in range(num_cols + 1):
        is_separator = col == num_cols or col in separator_cols

        if not is_separator and start_col is None:
            start_col = col
        elif is_separator and start_col is not None:
            # Extract this problem region
            end_col = col
            problem = _extract_problem(lines, start_col, end_col)
            if problem is not None:
                problems.append(problem)
            start_col = None

    return problems


def _extract_problem(
    lines: list[str], start_col: int, end_col: int
) -> tuple[list[int], str] | None:
    """Extract a single problem from a column range.

    Args:
        lines: All lines of the worksheet (padded to equal length)
        start_col: Starting column (inclusive)
        end_col: Ending column (exclusive)

    Returns:
        Tuple of (numbers, operator) or None if invalid
    """
    num_rows = len(lines)

    # Last row contains the operator
    operator_row = lines[num_rows - 1][start_col:end_col].strip()
    if '+' in operator_row:
        operator = '+'
    elif '*' in operator_row:
        operator = '*'
    else:
        return None

    # Other rows contain numbers
    numbers = []
    for row in range(num_rows - 1):
        text = lines[row][start_col:end_col].strip()
        if text:
            numbers.append(int(text))

    if not numbers:
        return None

    return (numbers, operator)


def parse_worksheet_part2(input_text: str) -> list[tuple[list[int], str]]:
    """Parse the worksheet for Part 2 (column-based numbers).

    In Part 2, each column within a problem represents one number.
    Digits are stacked vertically with most significant digit at top.

    Args:
        input_text: Raw worksheet text

    Returns:
        List of (numbers, operator) tuples for each problem
    """
    lines = input_text.rstrip('\n').split('\n')
    if not lines:
        return []

    # Pad all lines to the same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    num_rows = len(lines)
    num_cols = max_len

    # Find separator columns (all spaces in that column)
    separator_cols = set()
    for col in range(num_cols):
        if all(lines[row][col] == ' ' for row in range(num_rows)):
            separator_cols.add(col)

    # Find problem regions (consecutive non-separator columns)
    problems = []
    start_col = None

    for col in range(num_cols + 1):
        is_separator = col == num_cols or col in separator_cols

        if not is_separator and start_col is None:
            start_col = col
        elif is_separator and start_col is not None:
            # Extract this problem region
            end_col = col
            problem = _extract_problem_part2(lines, start_col, end_col)
            if problem is not None:
                problems.append(problem)
            start_col = None

    return problems


def _extract_problem_part2(
    lines: list[str], start_col: int, end_col: int
) -> tuple[list[int], str] | None:
    """Extract a single problem from a column range (Part 2 column-based).

    Each column within the problem region represents one number.
    Digits are stacked vertically with most significant at top.

    Args:
        lines: All lines of the worksheet (padded to equal length)
        start_col: Starting column (inclusive)
        end_col: Ending column (exclusive)

    Returns:
        Tuple of (numbers, operator) or None if invalid
    """
    num_rows = len(lines)

    # Last row contains the operator
    operator_row = lines[num_rows - 1][start_col:end_col].strip()
    if '+' in operator_row:
        operator = '+'
    elif '*' in operator_row:
        operator = '*'
    else:
        return None

    # Each column is a separate number (digits stacked vertically)
    numbers = []
    for col in range(start_col, end_col):
        digits = ''
        for row in range(num_rows - 1):
            char = lines[row][col]
            if char.isdigit():
                digits += char
        if digits:
            numbers.append(int(digits))

    if not numbers:
        return None

    return (numbers, operator)
