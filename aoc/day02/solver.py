def is_invalid_id(n: int) -> bool:
    """Check if a number is an invalid ID (digits repeated twice).

    Args:
        n: The number to check

    Returns:
        True if the number is made of a sequence of digits repeated twice
    """
    s = str(n)
    length = len(s)

    # Must have even number of digits
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def find_invalid_in_range(start: int, end: int) -> list[int]:
    """Find all invalid IDs in the given range [start, end].

    Uses an efficient algorithm: for a 2k-digit invalid number,
    it equals base * (10^k + 1) where base is a k-digit number.

    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)

    Returns:
        List of all invalid IDs in the range
    """
    invalid_ids = []

    # Try different digit lengths (k = half the total digits)
    k = 1
    while True:
        multiplier = 10**k + 1

        # Smallest k-digit base
        min_base = 1 if k == 1 else 10 ** (k - 1)
        # Largest k-digit base
        max_base = 10**k - 1

        # Smallest possible invalid number with 2k digits
        smallest_invalid = min_base * multiplier

        # If smallest invalid exceeds our range, we're done
        if smallest_invalid > end:
            break

        # Find the range of bases that produce invalid IDs in [start, end]
        # base * multiplier >= start  =>  base >= ceil(start / multiplier)
        # base * multiplier <= end    =>  base <= floor(end / multiplier)
        base_min = max(min_base, -(-start // multiplier))  # ceil division
        base_max = min(max_base, end // multiplier)

        # Add all valid invalid IDs
        for base in range(base_min, base_max + 1):
            invalid_id = base * multiplier
            if start <= invalid_id <= end:
                invalid_ids.append(invalid_id)

        k += 1

    return invalid_ids


def find_invalid_sum_in_range_optimized(start: int, end: int) -> int:
    """Find sum of all invalid IDs in range using O(1) arithmetic series.

    OPTIMIZATION: Instead of iterating over each base, we use the formula:
        sum(base * m for base in range(a, b+1)) = m * (b - a + 1) * (a + b) / 2

    This is O(log(max_digits)) instead of O(number of invalid IDs).

    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)

    Returns:
        Sum of all invalid IDs in the range
    """
    total = 0
    k = 1

    while True:
        multiplier = 10**k + 1

        # Valid k-digit bases
        min_base = 1 if k == 1 else 10 ** (k - 1)
        max_base = 10**k - 1

        # Early exit if smallest possible number exceeds range
        if min_base * multiplier > end:
            break

        # Find bases producing numbers in [start, end]
        base_min = max(min_base, -(-start // multiplier))  # ceil division
        base_max = min(max_base, end // multiplier)

        if base_min <= base_max:
            # Arithmetic series: sum of base_min to base_max
            count = base_max - base_min + 1
            sum_of_bases = count * (base_min + base_max) // 2
            total += multiplier * sum_of_bases

        k += 1

    return total


def solve_part1(ranges: list[tuple[int, int]]) -> int:
    """Solve part 1: sum all invalid IDs across all ranges.

    Uses the optimized O(log(digits)) arithmetic series approach.

    Args:
        ranges: List of (start, end) range tuples

    Returns:
        Sum of all invalid IDs found in the ranges
    """
    total = 0
    for start, end in ranges:
        total += find_invalid_sum_in_range_optimized(start, end)
    return total


def is_invalid_id_part2(n: int) -> bool:
    """Check if a number is an invalid ID (digits repeated at least twice).

    Args:
        n: The number to check

    Returns:
        True if the number is made of a sequence of digits repeated 2+ times
    """
    s = str(n)
    length = len(s)

    # Check all possible base lengths k where length/k >= 2
    for k in range(1, length // 2 + 1):
        if length % k == 0:
            repetitions = length // k
            base = s[:k]
            if base * repetitions == s:
                return True

    return False


def find_invalid_in_range_part2(start: int, end: int) -> set[int]:
    """Find all invalid IDs in the given range [start, end] for part 2.

    An invalid ID is a sequence repeated at least twice.
    Uses a set to avoid double-counting numbers that match multiple patterns.

    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)

    Returns:
        Set of all invalid IDs in the range
    """
    invalid_ids = set()

    # Determine the range of digit counts we need to consider
    min_digits = len(str(start))
    max_digits = len(str(end))

    # For each possible total digit count
    for d in range(min_digits, max_digits + 1):
        # For each base length k that divides d, where d/k >= 2
        for k in range(1, d // 2 + 1):
            if d % k != 0:
                continue

            # multiplier = (10^d - 1) / (10^k - 1)
            # This is 1, 10...01, 100...0100...01, etc.
            multiplier = (10**d - 1) // (10**k - 1)

            # Base must be a k-digit number
            min_base = 1 if k == 1 else 10 ** (k - 1)
            max_base = 10**k - 1

            # Find bases where start <= base * multiplier <= end
            base_min = max(min_base, -(-start // multiplier))  # ceil division
            base_max = min(max_base, end // multiplier)

            for base in range(base_min, base_max + 1):
                invalid_id = base * multiplier
                if start <= invalid_id <= end:
                    invalid_ids.add(invalid_id)

    return invalid_ids


def find_invalid_sum_in_range_part2_optimized(start: int, end: int) -> int:
    """Find sum of all invalid IDs in range for part 2, optimized.

    For Part 2, we cannot use a pure closed-form solution because numbers
    can be generated by multiple (d, k) combinations (e.g., 111111 = 1*111111
    = 11*10101 = 111*1001). We must deduplicate.

    OPTIMIZATION: We use arithmetic series for non-overlapping digit counts,
    and fall back to set-based deduplication only where needed.

    For single-digit bases (k=1), numbers like 111, 1111, 11111 don't overlap
    with each other across different digit counts, so we can use closed-form.

    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)

    Returns:
        Sum of all invalid IDs in the range
    """
    # For Part 2, the cleanest optimization is to generate unique numbers
    # into a set, but use efficient base range computation.
    #
    # A fully closed-form solution would require inclusion-exclusion:
    # - Add sum for each (d, k)
    # - Subtract overlap between pairs
    # - Add back triple overlaps, etc.
    # This is complex and error-prone.
    #
    # Instead, we optimize by:
    # 1. Removing redundant range checks (base_min/base_max already ensure validity)
    # 2. Early exit when no bases are valid

    invalid_ids = set()
    min_digits = len(str(start))
    max_digits = len(str(end))

    for d in range(min_digits, max_digits + 1):
        for k in range(1, d // 2 + 1):
            if d % k != 0:
                continue

            multiplier = (10**d - 1) // (10**k - 1)
            min_base = 1 if k == 1 else 10 ** (k - 1)
            max_base = 10**k - 1

            base_min = max(min_base, -(-start // multiplier))
            base_max = min(max_base, end // multiplier)

            # Skip if no valid bases (optimization: avoid empty loop)
            if base_min > base_max:
                continue

            # Add all invalid IDs for this (d, k) combination
            # The range check is guaranteed by base_min/base_max computation
            for base in range(base_min, base_max + 1):
                invalid_ids.add(base * multiplier)

    return sum(invalid_ids)


def solve_part2(ranges: list[tuple[int, int]]) -> int:
    """Solve part 2: sum all invalid IDs (repeated at least twice) across all ranges.

    Uses the optimized version with early-exit and removed redundant checks.

    Args:
        ranges: List of (start, end) range tuples

    Returns:
        Sum of all invalid IDs found in the ranges
    """
    total = 0
    for start, end in ranges:
        total += find_invalid_sum_in_range_part2_optimized(start, end)
    return total
