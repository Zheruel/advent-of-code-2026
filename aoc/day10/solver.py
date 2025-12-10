"""Solver for Day 10: Factory puzzle.

Part 1: Linear algebra over GF(2). Since pressing a button twice
is the same as not pressing it at all, we only care about whether each button
is pressed 0 or 1 times (in GF(2)).

Part 2: Integer linear programming over non-negative integers. Each button
press adds 1 to each counter it affects. We need to minimize total presses.
"""
from fractions import Fraction
from itertools import product


def buttons_to_matrix(num_lights: int, buttons: list[list[int]]) -> list[list[int]]:
    """Convert button definitions to a matrix.

    Returns a matrix where each column represents a button,
    and each row represents a light. Entry [i][j] is 1 if button j toggles light i.
    """
    matrix = [[0] * len(buttons) for _ in range(num_lights)]
    for j, button in enumerate(buttons):
        for light_idx in button:
            if light_idx < num_lights:
                matrix[light_idx][j] = 1
    return matrix


def solve_gf2(matrix: list[list[int]], target: list[int]) -> list[list[int]] | None:
    """Solve Ax = b over GF(2) using Gaussian elimination.

    Returns the solution space as a list of solutions, or None if no solution exists.
    The solution space is represented as [particular_solution, null_vector1, null_vector2, ...]
    """
    if not matrix or not matrix[0]:
        # No buttons - can only solve if target is all zeros
        if all(t == 0 for t in target):
            return [[]]
        return None

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create augmented matrix [A | b]
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]

    # Gaussian elimination with partial pivoting
    pivot_cols = []
    pivot_row = 0

    for col in range(num_cols):
        # Find pivot
        found = False
        for row in range(pivot_row, num_rows):
            if aug[row][col] == 1:
                # Swap rows
                aug[pivot_row], aug[row] = aug[row], aug[pivot_row]
                found = True
                break

        if not found:
            continue

        pivot_cols.append(col)

        # Eliminate other rows
        for row in range(num_rows):
            if row != pivot_row and aug[row][col] == 1:
                for c in range(num_cols + 1):
                    aug[row][c] ^= aug[pivot_row][c]

        pivot_row += 1

    # Check for inconsistency (row of form [0 0 ... 0 | 1])
    for row in range(pivot_row, num_rows):
        if aug[row][num_cols] == 1:
            return None  # No solution

    # Build particular solution
    particular = [0] * num_cols
    for i, col in enumerate(pivot_cols):
        particular[col] = aug[i][num_cols]

    # Find free variables (columns not in pivot_cols)
    free_cols = [c for c in range(num_cols) if c not in pivot_cols]

    # Build null space basis vectors
    null_vectors = []
    for free_col in free_cols:
        null_vec = [0] * num_cols
        null_vec[free_col] = 1
        # Set pivot variables
        for i, pivot_col in enumerate(pivot_cols):
            null_vec[pivot_col] = aug[i][free_col]
        null_vectors.append(null_vec)

    return [particular] + null_vectors


def min_weight_solution(solution_space: list[list[int]]) -> int:
    """Find the minimum weight solution in the solution space.

    Solution space is [particular, null1, null2, ...].
    Any solution is particular XOR (some subset of null vectors).
    """
    if not solution_space:
        return 0

    particular = solution_space[0]
    null_vectors = solution_space[1:]

    if not null_vectors:
        return sum(particular)

    # Try all combinations of null vectors
    min_weight = float('inf')
    num_null = len(null_vectors)

    # For efficiency, limit search if too many null vectors
    if num_null > 20:
        # Use greedy approach for large null spaces
        current = particular[:]
        for _ in range(num_null):
            best_improvement = 0
            best_vec = None
            for null_vec in null_vectors:
                new_sol = [c ^ n for c, n in zip(current, null_vec)]
                improvement = sum(current) - sum(new_sol)
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_vec = null_vec
            if best_vec is None:
                break
            current = [c ^ n for c, n in zip(current, best_vec)]
        return sum(current)

    # Enumerate all 2^num_null combinations
    for bits in range(1 << num_null):
        solution = particular[:]
        for i in range(num_null):
            if bits & (1 << i):
                solution = [s ^ n for s, n in zip(solution, null_vectors[i])]
        weight = sum(solution)
        min_weight = min(min_weight, weight)

    return min_weight


def solve_machine(target: list[bool], buttons: list[list[int]]) -> int:
    """Find the minimum button presses to configure a single machine."""
    num_lights = len(target)
    target_int = [1 if t else 0 for t in target]

    matrix = buttons_to_matrix(num_lights, buttons)
    solution_space = solve_gf2(matrix, target_int)

    if solution_space is None:
        # No solution exists - this shouldn't happen for valid puzzles
        return float('inf')

    return min_weight_solution(solution_space)


def solve_part1(machines: list[tuple[list[bool], list[list[int]], list[int]]]) -> int:
    """Find the total minimum button presses for all machines."""
    total = 0
    for target, buttons, _ in machines:
        presses = solve_machine(target, buttons)
        total += presses
    return total


def solve_joltage_ilp(buttons: list[list[int]], joltages: list[int]) -> int:
    """Solve the joltage problem using integer linear programming.

    We need to find non-negative integers x_i (presses for each button)
    such that Ax = b and minimize sum(x_i).

    Uses Gaussian elimination to find the solution space, then searches
    for the minimum sum solution with non-negative integer values.
    """
    if not buttons:
        return 0 if all(j == 0 for j in joltages) else float('inf')

    num_counters = len(joltages)
    num_buttons = len(buttons)

    # Build matrix A where A[i][j] = 1 if button j affects counter i
    matrix = [[Fraction(0)] * num_buttons for _ in range(num_counters)]
    for j, button in enumerate(buttons):
        for counter_idx in button:
            if counter_idx < num_counters:
                matrix[counter_idx][j] = Fraction(1)

    target = [Fraction(j) for j in joltages]

    # Gaussian elimination to find solution space
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]
    num_rows = len(aug)
    num_cols = num_buttons

    pivot_cols = []
    pivot_row = 0

    for col in range(num_cols):
        # Find pivot (non-zero entry)
        found = False
        for row in range(pivot_row, num_rows):
            if aug[row][col] != 0:
                aug[pivot_row], aug[row] = aug[row], aug[pivot_row]
                found = True
                break

        if not found:
            continue

        pivot_cols.append(col)

        # Scale pivot row
        scale = aug[pivot_row][col]
        for c in range(num_cols + 1):
            aug[pivot_row][c] /= scale

        # Eliminate other rows
        for row in range(num_rows):
            if row != pivot_row and aug[row][col] != 0:
                factor = aug[row][col]
                for c in range(num_cols + 1):
                    aug[row][c] -= factor * aug[pivot_row][c]

        pivot_row += 1

    # Check for inconsistency
    for row in range(pivot_row, num_rows):
        if aug[row][num_cols] != 0:
            return float('inf')

    # Find free variables
    free_cols = [c for c in range(num_cols) if c not in pivot_cols]

    # Build particular solution (set free vars to 0)
    particular = [Fraction(0)] * num_cols
    for i, col in enumerate(pivot_cols):
        particular[col] = aug[i][num_cols]

    # Build null space basis vectors
    null_vectors = []
    for free_col in free_cols:
        null_vec = [Fraction(0)] * num_cols
        null_vec[free_col] = Fraction(1)
        for i, pivot_col in enumerate(pivot_cols):
            null_vec[pivot_col] = -aug[i][free_col]
        null_vectors.append(null_vec)

    # Search for minimum sum non-negative integer solution
    # Solution = particular + sum(t_i * null_i) for integer t_i
    return find_min_nonneg_integer_solution(particular, null_vectors)


def find_min_nonneg_integer_solution(
    particular: list[Fraction], null_vectors: list[list[Fraction]]
) -> int:
    """Find the minimum sum non-negative integer solution.

    Uses vertex enumeration: the minimum of a linear objective over a polytope
    occurs at a vertex. Vertices are where k constraints are tight (for k free vars).
    """
    num_vars = len(particular)
    num_free = len(null_vectors)

    if num_free == 0:
        if all(p >= 0 and p.denominator == 1 for p in particular):
            return sum(int(p) for p in particular)
        return float('inf')

    def check_solution(coeffs: list[Fraction]) -> int | None:
        """Check if coefficients give valid solution, return sum or None."""
        sol = particular[:]
        for j, t in enumerate(coeffs):
            sol = [sol[i] + t * null_vectors[j][i] for i in range(num_vars)]
        if all(s >= 0 and s.denominator == 1 for s in sol):
            return sum(int(s) for s in sol)
        return None

    def solve_linear_system(rows: list[int]) -> list[Fraction] | None:
        """Solve system where constraints 'rows' are tight (= 0)."""
        # Build system: for each row r, sum_j(t_j * null_vectors[j][r]) = -particular[r]
        n = num_free
        if len(rows) != n:
            return None

        # Matrix A where A[i][j] = null_vectors[j][rows[i]]
        # Vector b where b[i] = -particular[rows[i]]
        A = [[null_vectors[j][rows[i]] for j in range(n)] for i in range(n)]
        b = [-particular[rows[i]] for i in range(n)]

        # Gaussian elimination
        aug = [A[i][:] + [b[i]] for i in range(n)]

        for col in range(n):
            # Find pivot
            pivot_row = None
            for row in range(col, n):
                if aug[row][col] != 0:
                    pivot_row = row
                    break
            if pivot_row is None:
                return None  # Singular

            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

            # Scale
            scale = aug[col][col]
            for c in range(n + 1):
                aug[col][c] /= scale

            # Eliminate
            for row in range(n):
                if row != col and aug[row][col] != 0:
                    factor = aug[row][col]
                    for c in range(n + 1):
                        aug[row][c] -= factor * aug[col][c]

        return [aug[i][n] for i in range(n)]

    min_sum = float('inf')

    if num_free == 1:
        null_vec = null_vectors[0]

        # Find valid t values: those where all components are integers
        # This requires finding the lattice of integer solutions

        # Get all denominators involved
        from math import gcd
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        # For solution to be integer, (p[i] + t*n[i]) must be integer for all i
        # If p[i] = a/b and n[i] = c/d, then we need (a*d + t*c*b) / (b*d) to be integer
        # This means t must satisfy certain modular constraints

        # Compute LCM of all denominators in null_vec
        null_lcm = 1
        for n in null_vec:
            if n != 0:
                null_lcm = lcm(null_lcm, n.denominator)

        # Find starting t and step that produces integer solutions
        # Try t values that are multiples of null_lcm, plus offsets
        candidates = set()

        # Find bounds for t from non-negativity constraints
        lower_bound, upper_bound = -1000, 1000
        for i in range(num_vars):
            if null_vec[i] > 0:
                bound = -particular[i] / null_vec[i]
                lb = int(bound)
                if Fraction(lb) < bound:
                    lb += 1
                lower_bound = max(lower_bound, lb)
            elif null_vec[i] < 0:
                bound = -particular[i] / null_vec[i]
                ub = int(bound)
                if Fraction(ub) > bound:
                    ub -= 1
                upper_bound = min(upper_bound, ub)

        # Search within bounds
        if lower_bound <= upper_bound:
            for t in range(lower_bound, upper_bound + 1):
                result = check_solution([Fraction(t)])
                if result is not None:
                    min_sum = min(min_sum, result)

    elif num_free == 2:
        # Bounded enumeration over all integer points in feasible region
        null0, null1 = null_vectors[0], null_vectors[1]

        # Estimate bounds from non-negativity constraints
        max_bound = 300
        for t0 in range(-max_bound, max_bound + 1):
            # Compute bounds for t1 given t0
            inter = [particular[i] + t0 * null0[i] for i in range(num_vars)]

            lower1, upper1 = -max_bound, max_bound
            for i in range(num_vars):
                if null1[i] > 0:
                    bound = -inter[i] / null1[i]
                    lb = int(bound)
                    if Fraction(lb) < bound:
                        lb += 1
                    lower1 = max(lower1, lb)
                elif null1[i] < 0:
                    bound = -inter[i] / null1[i]
                    ub = int(bound)
                    if Fraction(ub) > bound:
                        ub -= 1
                    upper1 = min(upper1, ub)

            if lower1 > upper1:
                continue

            for t1 in range(lower1, upper1 + 1):
                result = check_solution([Fraction(t0), Fraction(t1)])
                if result is not None:
                    min_sum = min(min_sum, result)

    else:
        # For 3+ free variables, use float-based search for speed
        # Don't compute restrictive bounds - just search wide range and check final solution
        from itertools import product as iproduct

        # Convert to floats for speed
        p_float = [float(p) for p in particular]
        n_float = [[float(n) for n in nv] for nv in null_vectors]

        max_bound = 100
        tol = 1e-9

        for coeffs in iproduct(range(-max_bound, max_bound + 1), repeat=num_free):
            # Quick float check
            sol = p_float[:]
            for j, t in enumerate(coeffs):
                sol = [sol[i] + t * n_float[j][i] for i in range(num_vars)]

            # Check if all non-negative and close to integers
            valid = True
            total = 0
            for s in sol:
                if s < -tol:
                    valid = False
                    break
                r = round(s)
                if abs(s - r) > tol:
                    valid = False
                    break
                total += max(0, r)

            if not valid or total >= min_sum:
                continue

            # Verify with Fraction for exactness
            sol_frac = particular[:]
            for j, t in enumerate(coeffs):
                sol_frac = [sol_frac[i] + t * null_vectors[j][i] for i in range(num_vars)]

            if all(s >= 0 and s.denominator == 1 for s in sol_frac):
                min_sum = sum(int(s) for s in sol_frac)

    return min_sum


def solve_part2(machines: list[tuple[list[bool], list[list[int]], list[int]]]) -> int:
    """Find the total minimum button presses for all machines' joltage requirements."""
    total = 0
    for _, buttons, joltages in machines:
        presses = solve_joltage_ilp(buttons, joltages)
        total += presses
    return total
