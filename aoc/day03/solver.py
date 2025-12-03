def max_joltage(bank: str) -> int:
    """Find the maximum joltage possible from a single bank.

    Picks exactly 2 batteries at positions i < j to form the 2-digit
    number digit[i] * 10 + digit[j].

    Single pass from right to left, O(1) space.

    Args:
        bank: String of digits representing battery joltage ratings

    Returns:
        Maximum possible joltage from this bank
    """
    n = len(bank)
    if n < 2:
        return 0

    best = 0
    max_second = 0  # max digit seen so far (scanning right to left)

    for i in range(n - 1, -1, -1):
        digit = int(bank[i])
        if i < n - 1:  # can use this as first digit (there's something after)
            best = max(best, digit * 10 + max_second)
        max_second = max(max_second, digit)

    return best


def solve_part1(banks: list[str]) -> int:
    """Solve part 1: sum all maximum joltages across all banks.

    Args:
        banks: List of bank strings

    Returns:
        Sum of maximum joltage from each bank
    """
    return sum(max_joltage(bank) for bank in banks)


def max_joltage_k(bank: str, k: int) -> int:
    """Find the maximum joltage by selecting exactly k batteries.

    Uses monotonic stack approach to greedily select the largest k-digit
    subsequence while maintaining order.

    Args:
        bank: String of digits representing battery joltage ratings
        k: Number of batteries to select

    Returns:
        Maximum possible joltage (as integer) from selecting k batteries
    """
    n = len(bank)
    if k <= 0 or k > n:
        return 0

    # Number of digits we need to drop
    drops = n - k
    stack = []

    for digit in bank:
        # While we can drop and current digit is larger than stack top
        while stack and drops > 0 and digit > stack[-1]:
            stack.pop()
            drops -= 1
        stack.append(digit)

    # Take only first k digits (in case we didn't use all drops)
    result = "".join(stack[:k])
    return int(result)


def solve_part2(banks: list[str]) -> int:
    """Solve part 2: sum all maximum joltages with k=12 batteries.

    Args:
        banks: List of bank strings

    Returns:
        Sum of maximum joltage from each bank using 12 batteries
    """
    return sum(max_joltage_k(bank, 12) for bank in banks)
