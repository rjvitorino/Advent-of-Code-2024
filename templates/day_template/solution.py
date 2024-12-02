from pathlib import Path
from typing import List


def part1(data: List[str]) -> int:
    """
    Solve part 1 of the challenge.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 1.
    """
    # Solve part 1
    pass


def part2(data: List[str]) -> int:
    """
    Solve part 2 of the challenge.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 2.
    """
    # Solve part 2
    pass


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
