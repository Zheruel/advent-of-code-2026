import bisect


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or adjacent ranges into non-overlapping ranges.

    Args:
        ranges: List of (start, end) tuples representing ranges (inclusive)

    Returns:
        List of merged (start, end) tuples, sorted by start value
    """
    if not ranges:
        return []

    # Sort by start value
    sorted_ranges = sorted(ranges, key=lambda r: r[0])

    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        # Check if current range overlaps or is adjacent to the last merged range
        if start <= last_end + 1:
            # Merge by extending the end if necessary
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def is_fresh(ingredient_id: int, merged_ranges: list[tuple[int, int]]) -> bool:
    """Check if an ingredient ID falls within any of the merged ranges.

    Uses binary search for efficient lookup in sorted, non-overlapping ranges.

    Args:
        ingredient_id: The ingredient ID to check
        merged_ranges: List of non-overlapping (start, end) tuples, sorted by start

    Returns:
        True if the ingredient ID is within any range (fresh), False otherwise
    """
    if not merged_ranges:
        return False

    # Find the rightmost range where start <= ingredient_id
    # We use the start values for binary search
    starts = [r[0] for r in merged_ranges]
    idx = bisect.bisect_right(starts, ingredient_id) - 1

    if idx < 0:
        return False

    # Check if ingredient_id is within the range at idx
    start, end = merged_ranges[idx]
    return start <= ingredient_id <= end


def solve_part1(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    """Count how many ingredient IDs are fresh.

    An ingredient ID is fresh if it falls within any of the given ranges.
    Ranges are inclusive and can overlap.

    Args:
        ranges: List of (start, end) tuples representing fresh ID ranges
        ingredient_ids: List of ingredient IDs to check

    Returns:
        Number of fresh ingredient IDs
    """
    merged = merge_ranges(ranges)
    return sum(1 for id in ingredient_ids if is_fresh(id, merged))


def solve_part2(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    """Count total unique ingredient IDs covered by all ranges.

    Merges overlapping ranges and counts the total number of unique IDs
    that fall within any range. The ingredient_ids parameter is ignored.

    Args:
        ranges: List of (start, end) tuples representing fresh ID ranges
        ingredient_ids: List of ingredient IDs (unused in Part 2)

    Returns:
        Total number of unique fresh ingredient IDs across all ranges
    """
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)
