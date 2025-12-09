import unittest

from aoc.day08.parser import parse_junctions
from aoc.day08.solver import solve_part1, solve_part2, UnionFind, distance_squared

EXAMPLE_INPUT = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


class TestDay08(unittest.TestCase):
    def test_parse_junctions(self):
        junctions = parse_junctions(EXAMPLE_INPUT)
        self.assertEqual(len(junctions), 20)
        self.assertEqual(junctions[0], (162, 817, 812))
        self.assertEqual(junctions[19], (425, 690, 689))
        self.assertEqual(junctions[5], (466, 668, 158))

    def test_distance_squared(self):
        p1 = (0, 0, 0)
        p2 = (1, 2, 2)
        self.assertEqual(distance_squared(p1, p2), 9)

        p1 = (162, 817, 812)
        p2 = (425, 690, 689)
        expected = (425 - 162) ** 2 + (690 - 817) ** 2 + (689 - 812) ** 2
        self.assertEqual(distance_squared(p1, p2), expected)

    def test_union_find(self):
        uf = UnionFind(5)
        self.assertEqual(uf.get_component_sizes(), [1, 1, 1, 1, 1])

        uf.union(0, 1)
        self.assertEqual(sorted(uf.get_component_sizes(), reverse=True), [2, 1, 1, 1])

        uf.union(0, 1)
        self.assertEqual(sorted(uf.get_component_sizes(), reverse=True), [2, 1, 1, 1])

        uf.union(2, 3)
        self.assertEqual(sorted(uf.get_component_sizes(), reverse=True), [2, 2, 1])

        uf.union(0, 2)
        self.assertEqual(sorted(uf.get_component_sizes(), reverse=True), [4, 1])

    def test_example_part1(self):
        junctions = parse_junctions(EXAMPLE_INPUT)
        result = solve_part1(junctions, num_connections=10)
        self.assertEqual(result, 40)

    def test_example_part2(self):
        junctions = parse_junctions(EXAMPLE_INPUT)
        result = solve_part2(junctions)
        self.assertEqual(result, 25272)


if __name__ == "__main__":
    unittest.main()
