from collections import Counter


class UnionFind:
    """Union-Find data structure for tracking connected components."""

    def __init__(self, n: int):
        """Initialize n elements, each in its own component.

        Args:
            n: Number of elements (0 to n-1).
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """Find the root of element x with path compression.

        Args:
            x: Element to find root of.

        Returns:
            Root element of the component containing x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union the components containing x and y.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if x and y were in different components (union performed),
            False if they were already in the same component.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def get_component_sizes(self) -> list[int]:
        """Get sizes of all components.

        Returns:
            List of component sizes, sorted in descending order.
        """
        roots = [self.find(i) for i in range(len(self.parent))]
        counts = Counter(roots)
        return sorted(counts.values(), reverse=True)


def distance_squared(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    """Calculate squared Euclidean distance between two 3D points.

    Args:
        p1: First point as (x, y, z).
        p2: Second point as (x, y, z).

    Returns:
        Squared distance (avoids sqrt for comparison purposes).
    """
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


def solve_part1(
    junctions: list[tuple[int, int, int]], num_connections: int = 1000
) -> int:
    """Connect the closest pairs of junction boxes and find largest circuits.

    Connects the specified number of closest pairs (by straight-line distance).
    When two junction boxes are connected, they become part of the same circuit.
    If two boxes are already in the same circuit, connecting them does nothing.

    Args:
        junctions: List of (x, y, z) coordinates for each junction box.
        num_connections: Number of closest pairs to connect (default 1000).

    Returns:
        Product of the sizes of the three largest circuits.
    """
    n = len(junctions)

    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = distance_squared(junctions[i], junctions[j])
            pairs.append((dist_sq, i, j))

    pairs.sort()

    uf = UnionFind(n)

    for k in range(min(num_connections, len(pairs))):
        _, i, j = pairs[k]
        uf.union(i, j)

    sizes = uf.get_component_sizes()

    top3 = sizes[:3]
    while len(top3) < 3:
        top3.append(1)

    return top3[0] * top3[1] * top3[2]


def solve_part2(junctions: list[tuple[int, int, int]]) -> int:
    """Find the last connection needed to form a single circuit.

    Continues connecting closest pairs until all junction boxes are in one
    circuit. Returns the product of the X coordinates of the last two
    junction boxes that need to be connected.

    Args:
        junctions: List of (x, y, z) coordinates for each junction box.

    Returns:
        Product of X coordinates of the last two connected junction boxes.
    """
    n = len(junctions)

    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = distance_squared(junctions[i], junctions[j])
            pairs.append((dist_sq, i, j))

    pairs.sort()

    uf = UnionFind(n)
    components = n

    for _, i, j in pairs:
        if uf.union(i, j):
            components -= 1
            if components == 1:
                return junctions[i][0] * junctions[j][0]

    return 0
