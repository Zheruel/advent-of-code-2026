"""Parser for Day 10: Factory puzzle."""
import re


def parse_input(text: str) -> list[tuple[list[bool], list[list[int]], list[int]]]:
    """Parse the input into machines.

    Each machine is a tuple of:
    - target: list of bools (True = on, False = off)
    - buttons: list of lists of ints (each button lists which lights it toggles)
    - joltages: list of ints (ignored for part 1)
    """
    machines = []

    for line in text.strip().split('\n'):
        if not line:
            continue

        # Parse indicator light diagram [.##.]
        diagram_match = re.search(r'\[([.#]+)\]', line)
        if not diagram_match:
            continue
        diagram = diagram_match.group(1)
        target = [c == '#' for c in diagram]

        # Parse button wiring schematics (0,1,2) or (3)
        buttons = []
        # Find all parentheses groups
        button_matches = re.findall(r'\(([0-9,]+)\)', line)
        for match in button_matches:
            indices = [int(x) for x in match.split(',')]
            buttons.append(indices)

        # Parse joltage requirements {3,5,4,7}
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        joltages = []
        if joltage_match:
            joltages = [int(x) for x in joltage_match.group(1).split(',')]

        machines.append((target, buttons, joltages))

    return machines
