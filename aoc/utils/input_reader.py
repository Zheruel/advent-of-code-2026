from pathlib import Path


def read_input(day: int) -> str:
    """Read the input file for a given day."""
    input_path = Path(__file__).parent.parent.parent / "inputs" / f"day{day:02d}.txt"
    return input_path.read_text().strip()


def read_input_lines(day: int) -> list[str]:
    """Read the input file for a given day and return as list of lines."""
    return read_input(day).split("\n")
