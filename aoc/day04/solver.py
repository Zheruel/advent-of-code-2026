def count_adjacent_rolls(grid: list[str], row: int, col: int) -> int:
    """Count paper rolls (@) in the 8 adjacent positions."""
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
    return count


def solve_part1(grid: list[str]) -> int:
    """Count rolls accessible by forklift (fewer than 4 adjacent rolls)."""
    accessible = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                if count_adjacent_rolls(grid, row, col) < 4:
                    accessible += 1
    return accessible


def solve_part2(grid: list[str]) -> int:
    """Count total rolls removable by repeatedly removing accessible rolls.

    Optimized: Only recheck neighbors of removed rolls instead of full grid scan.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Build set of roll positions and compute initial neighbor counts
    rolls = set()
    neighbor_count = {}

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                rolls.add((r, c))

    # Compute neighbor counts for all rolls
    for (r, c) in rolls:
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if (r + dr, c + dc) in rolls:
                    count += 1
        neighbor_count[(r, c)] = count

    # Seed queue with initially accessible rolls
    queue = [(r, c) for (r, c) in rolls if neighbor_count[(r, c)] < 4]
    queued = set(queue)
    total_removed = 0

    # Process queue
    while queue:
        r, c = queue.pop()

        # Skip if already removed
        if (r, c) not in rolls:
            continue

        # Remove this roll
        rolls.remove((r, c))
        total_removed += 1

        # Update neighbors and check if they become accessible
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if (nr, nc) in rolls:
                    neighbor_count[(nr, nc)] -= 1
                    # If dropped to < 4 and not already queued, add to queue
                    if neighbor_count[(nr, nc)] < 4 and (nr, nc) not in queued:
                        queue.append((nr, nc))
                        queued.add((nr, nc))

    return total_removed
