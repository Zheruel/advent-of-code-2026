"""Solver for Day 09: Tile Floor Rectangle puzzle."""


def solve_part1(tiles: list[tuple[int, int]]) -> int:
    """Find the largest rectangle area using two red tiles as opposite corners.

    For any two red tiles at positions (x1, y1) and (x2, y2), they can form
    opposite corners of a rectangle. The area is calculated inclusively:
    (|x2 - x1| + 1) * (|y2 - y1| + 1)

    Args:
        tiles: List of (x, y) coordinates of red tiles.

    Returns:
        The maximum rectangle area achievable.
    """
    max_area = 0
    n = len(tiles)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


def _point_in_polygon(x: int, y: int, tiles: list[tuple[int, int]]) -> bool:
    """Check if a point is inside the polygon using ray casting.

    Cast a ray to the right and count edge crossings.

    Args:
        x, y: Point coordinates.
        tiles: Polygon vertices.

    Returns:
        True if point is inside the polygon (not on boundary).
    """
    n = len(tiles)
    crossings = 0

    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        # Only consider vertical edges that the horizontal ray might cross
        if x1 == x2:  # Vertical edge
            # Ray at height y going right from x
            # Edge must be to the right of point
            if x1 > x:
                min_y, max_y = min(y1, y2), max(y1, y2)
                # Ray crosses if y is within the edge's y-range
                # Use min_y <= y < max_y to handle corners consistently
                if min_y <= y < max_y:
                    crossings += 1

    return crossings % 2 == 1


def _point_on_boundary(x: int, y: int, tiles: list[tuple[int, int]]) -> bool:
    """Check if a point is on the polygon boundary.

    Args:
        x, y: Point coordinates.
        tiles: Polygon vertices.

    Returns:
        True if point is on any edge of the polygon.
    """
    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        if x1 == x2:  # Vertical edge
            if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                return True
        else:  # Horizontal edge
            if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True

    return False


def _point_in_or_on_polygon(x: int, y: int, tiles: list[tuple[int, int]]) -> bool:
    """Check if a point is inside or on the polygon boundary."""
    return _point_on_boundary(x, y, tiles) or _point_in_polygon(x, y, tiles)


def _get_edges(tiles: list[tuple[int, int]]) -> tuple[list, list]:
    """Extract horizontal and vertical edges from polygon.

    Returns:
        Tuple of (horizontal_edges, vertical_edges) where each edge is
        (x1, x2, y) for horizontal or (y1, y2, x) for vertical.
    """
    h_edges = []  # (x_min, x_max, y)
    v_edges = []  # (y_min, y_max, x)

    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        if x1 == x2:  # Vertical edge
            v_edges.append((min(y1, y2), max(y1, y2), x1))
        else:  # Horizontal edge
            h_edges.append((min(x1, x2), max(x1, x2), y1))

    return h_edges, v_edges


def _rectangle_valid(
    rx1: int, ry1: int, rx2: int, ry2: int,
    tiles: list[tuple[int, int]],
    h_edges: list, v_edges: list
) -> bool:
    """Check if a rectangle is fully contained in the polygon.

    A rectangle is valid if:
    1. All 4 corners are inside or on the polygon boundary
    2. No polygon edge passes through the interior of the rectangle

    Args:
        rx1, ry1, rx2, ry2: Rectangle corners.
        tiles: Polygon vertices.
        h_edges, v_edges: Pre-computed polygon edges.

    Returns:
        True if the rectangle is fully inside the polygon.
    """
    min_x, max_x = min(rx1, rx2), max(rx1, rx2)
    min_y, max_y = min(ry1, ry2), max(ry1, ry2)

    # Check all 4 corners are inside or on boundary
    corners = [
        (min_x, min_y), (min_x, max_y),
        (max_x, min_y), (max_x, max_y)
    ]
    for cx, cy in corners:
        if not _point_in_or_on_polygon(cx, cy, tiles):
            return False

    # Check no horizontal edge passes through interior
    # A horizontal edge at y crosses the interior if:
    # - min_y < y < max_y (strictly inside vertically)
    # - The edge's x-range overlaps with (min_x, max_x) interior
    for ex_min, ex_max, ey in h_edges:
        if min_y < ey < max_y:
            # Edge is at a y-level inside the rectangle
            # Check if edge x-range enters the rectangle interior
            if ex_min < max_x and ex_max > min_x:
                # There's overlap - but is part of the edge inside?
                # The interior x-range is (min_x, max_x) exclusive
                # Edge x-range is [ex_min, ex_max] inclusive
                # If edge starts or ends strictly inside, it crosses
                if ex_min > min_x and ex_min < max_x:
                    return False
                if ex_max > min_x and ex_max < max_x:
                    return False
                # If edge completely spans the rectangle, it also crosses
                if ex_min <= min_x and ex_max >= max_x:
                    return False

    # Check no vertical edge passes through interior
    for ey_min, ey_max, ex in v_edges:
        if min_x < ex < max_x:
            # Edge is at an x-level inside the rectangle
            if ey_min < max_y and ey_max > min_y:
                if ey_min > min_y and ey_min < max_y:
                    return False
                if ey_max > min_y and ey_max < max_y:
                    return False
                if ey_min <= min_y and ey_max >= max_y:
                    return False

    return True


def solve_part2(tiles: list[tuple[int, int]]) -> int:
    """Find largest rectangle using red corners where all tiles are red or green.

    The red tiles form a closed polygon connected by green edges. Interior
    tiles are also green. The rectangle must have red tiles at opposite
    corners and contain only red or green tiles.

    Args:
        tiles: List of (x, y) coordinates of red tiles.

    Returns:
        The maximum valid rectangle area.
    """
    h_edges, v_edges = _get_edges(tiles)

    max_area = 0
    n = len(tiles)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            if _rectangle_valid(x1, y1, x2, y2, tiles, h_edges, v_edges):
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                if area > max_area:
                    max_area = area

    return max_area
