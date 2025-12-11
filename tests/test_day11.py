import unittest

from aoc.day11.parser import parse_devices
from aoc.day11.solver import solve_part1, solve_part2


EXAMPLE_INPUT = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


class TestDay11Parser(unittest.TestCase):
    def test_parse_devices(self):
        graph = parse_devices(EXAMPLE_INPUT)
        self.assertEqual(graph['you'], ['bbb', 'ccc'])
        self.assertEqual(graph['bbb'], ['ddd', 'eee'])
        self.assertEqual(graph['eee'], ['out'])
        self.assertEqual(len(graph), 10)


EXAMPLE_INPUT_PART2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


class TestDay11Solver(unittest.TestCase):
    def test_part1_example(self):
        graph = parse_devices(EXAMPLE_INPUT)
        result = solve_part1(graph)
        self.assertEqual(result, 5)

    def test_part2_example(self):
        graph = parse_devices(EXAMPLE_INPUT_PART2)
        result = solve_part2(graph)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
