"""Solver for Day 7: Laboratories puzzle."""


def solve_part1(grid: list[str], start_col: int) -> int:
    """Count the total number of times the tachyon beam is split.

    A tachyon beam enters at the starting column and moves downward.
    When it hits a splitter ('^'), it stops and creates two new beams
    from the immediate left and right positions.

    Args:
        grid: The manifold diagram as a list of strings.
        start_col: The column index where the beam enters.

    Returns:
        The total number of times the beam is split.
    """
    active_beams = {start_col}
    split_count = 0
    width = len(grid[0]) if grid else 0

    for row in range(1, len(grid)):
        new_beams = set()
        for col in active_beams:
            if 0 <= col < len(grid[row]) and grid[row][col] == '^':
                split_count += 1
                if col > 0:
                    new_beams.add(col - 1)
                if col < width - 1:
                    new_beams.add(col + 1)
            elif 0 <= col < len(grid[row]):
                new_beams.add(col)
        active_beams = new_beams
        if not active_beams:
            break

    return split_count


def solve_part2(grid: list[str], start_col: int) -> int:
    """Count the number of timelines after quantum tachyon splitting.

    Using the many-worlds interpretation, each particle that hits a splitter
    creates two timelines (one where it went left, one where it went right).
    Unlike Part 1, particles at the same column don't merge - each represents
    a distinct timeline.

    Args:
        grid: The manifold diagram as a list of strings.
        start_col: The column index where the particle enters.

    Returns:
        The total number of distinct timelines.
    """
    particles = {start_col: 1}  # col -> particle count
    width = len(grid[0]) if grid else 0

    for row in range(1, len(grid)):
        new_particles: dict[int, int] = {}
        for col, count in particles.items():
            if 0 <= col < len(grid[row]) and grid[row][col] == '^':
                if col > 0:
                    new_particles[col - 1] = new_particles.get(col - 1, 0) + count
                if col < width - 1:
                    new_particles[col + 1] = new_particles.get(col + 1, 0) + count
            elif 0 <= col < len(grid[row]):
                new_particles[col] = new_particles.get(col, 0) + count
        particles = new_particles
        if not particles:
            break

    return sum(particles.values())
