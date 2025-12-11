def count_paths(graph: dict[str, list[str]], node: str, memo: dict[str, int]) -> int:
    """Count paths from node to 'out' using memoization.

    Args:
        graph: Adjacency list of device connections
        node: Current node to count paths from
        memo: Memoization cache

    Returns:
        Number of distinct paths from node to 'out'
    """
    if node == 'out':
        return 1
    if node in memo:
        return memo[node]
    if node not in graph:
        return 0

    total = 0
    for neighbor in graph[node]:
        total += count_paths(graph, neighbor, memo)

    memo[node] = total
    return total


def solve_part1(graph: dict[str, list[str]]) -> int:
    """Count all distinct paths from 'you' to 'out'.

    Args:
        graph: Adjacency list of device connections

    Returns:
        Number of distinct paths from 'you' to 'out'
    """
    memo = {}
    return count_paths(graph, 'you', memo)


def count_paths_with_required(
    graph: dict[str, list[str]],
    node: str,
    visited_dac: bool,
    visited_fft: bool,
    memo: dict[tuple, int]
) -> int:
    """Count paths from node to 'out' that visit both dac and fft.

    Args:
        graph: Adjacency list of device connections
        node: Current node
        visited_dac: Whether dac has been visited on this path
        visited_fft: Whether fft has been visited on this path
        memo: Memoization cache keyed by (node, visited_dac, visited_fft)

    Returns:
        Number of paths to 'out' that visit both required nodes
    """
    if node == 'dac':
        visited_dac = True
    if node == 'fft':
        visited_fft = True

    if node == 'out':
        return 1 if (visited_dac and visited_fft) else 0

    state = (node, visited_dac, visited_fft)
    if state in memo:
        return memo[state]

    if node not in graph:
        return 0

    total = 0
    for neighbor in graph[node]:
        total += count_paths_with_required(graph, neighbor, visited_dac, visited_fft, memo)

    memo[state] = total
    return total


def solve_part2(graph: dict[str, list[str]]) -> int:
    """Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'.

    Args:
        graph: Adjacency list of device connections

    Returns:
        Number of paths visiting both dac and fft
    """
    memo = {}
    return count_paths_with_required(graph, 'svr', False, False, memo)
