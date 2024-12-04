from collections import namedtuple
from pathlib import Path
from typing import List
from shared.data_classes import Grid

# Define the Direction structure at module level
Direction = namedtuple("Direction", ["row", "col"])
DIRECTIONS = {
    "UP_LEFT": Direction(-1, -1),
    "UP": Direction(-1, 0),
    "UP_RIGHT": Direction(-1, 1),
    "LEFT": Direction(0, -1),
    "RIGHT": Direction(0, 1),
    "DOWN_LEFT": Direction(1, -1),
    "DOWN": Direction(1, 0),
    "DOWN_RIGHT": Direction(1, 1),
}


def parse_grid(input_lines: List[str]) -> Grid:
    """
    Parse input lines into a Grid object.
    """
    return Grid(data=[list(line.strip()) for line in input_lines])


def find_word(grid: Grid, word: str) -> int:
    """
    Find all occurrences of the word in the grid.

    Args:
        grid (Grid): The grid of characters.
        word (str): The target word to find.

    Returns:
        int: The count of all occurrences of the word.
    """
    if not word:
        return 0

    # Pre-compute valid starting positions
    # Only check positions where first character matches
    starting_positions = [
        (x, y)
        for y, row in enumerate(grid.data)
        for x, char in enumerate(row)
        if char == word[0]
    ]

    count = 0
    # Only check from valid starting positions
    for x, y in starting_positions:
        for direction in DIRECTIONS.values():
            if grid.check_direction(x, y, direction.col, direction.row, word):
                count += 1

    return count


def find_xmas(grid: Grid) -> int:
    """
    Find all occurrences of the "X-MAS" pattern in the grid:
    M.S
    .A.
    M.S
    """
    rows, cols = grid.get_grid_dimensions()
    count = 0

    # Pre-compute A positions to avoid scanning entire grid
    a_positions = [
        (x, y)
        for y in range(1, rows - 1)
        for x in range(1, cols - 1)
        if grid.get(x, y) == "A"
    ]

    # Define the base positions we care about
    CORNERS = [
        (-1, -1),  # top-left
        (1, -1),  # top-right
        (-1, 1),  # bottom-left
        (1, 1),  # bottom-right
    ]

    # Define the pattern variations
    patterns = [
        # Pattern 1: S on top, M on bottom
        [("S", x, -1) if y == -1 else ("M", x, 1) for x, y in CORNERS],
        # Pattern 2: M on top, S on bottom
        [("M", x, -1) if y == -1 else ("S", x, 1) for x, y in CORNERS],
        # Pattern 3: Alternating diagonal
        [("M", -1, y) if x == -1 else ("S", 1, y) for x, y in CORNERS],
        # Pattern 4: Alternating diagonal (reversed)
        [("S", -1, y) if x == -1 else ("M", 1, y) for x, y in CORNERS],
    ]

    # Cache grid data to reduce method calls
    grid_data = grid.data

    # For each A found, check if any pattern match all its conditions
    for x, y in a_positions:
        if any(
            all(grid_data[y + dy][x + dx] == char for char, dx, dy in pattern)
            for pattern in patterns
        ):
            count += 1

    return count


def part1(data: List[str]) -> int:
    """
    Solve part 1 of the challenge: Find all occurrences of "XMAS".
    """
    grid = parse_grid(data)
    return find_word(grid, "XMAS")


def part2(data: List[str]) -> int:
    """
    Solve part 2 of the challenge: Find all occurrences of "X-MAS".
    """
    grid = parse_grid(data)
    return find_xmas(grid)


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
