def parse_junctions(input_text: str) -> list[tuple[int, int, int]]:
    """Parse input into list of (x, y, z) coordinate tuples.

    Args:
        input_text: Raw input text with one junction box per line,
                    each line containing comma-separated x,y,z coordinates.

    Returns:
        List of tuples representing 3D coordinates, e.g., [(162, 817, 812), ...]
    """
    junctions = []
    for line in input_text.strip().split("\n"):
        line = line.strip()
        if line:
            x, y, z = map(int, line.split(","))
            junctions.append((x, y, z))
    return junctions
