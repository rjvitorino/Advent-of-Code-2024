import pytest
from pathlib import Path
from typing import List
from .day04_solution import part1, part2, parse_grid, find_word, find_xmas
from shared.data_classes import Grid


def test_parse_grid() -> None:
    """
    Test the parse_grid function with a small example input.
    """
    input_data: List[str] = [
        "XMAS",
        "MAMX",
        "ATXM",
    ]
    expected_output: Grid = Grid(
        data=[
            ["X", "M", "A", "S"],
            ["M", "A", "M", "X"],
            ["A", "T", "X", "M"],
        ]
    )
    assert parse_grid(input_data) == expected_output


def test_find_word() -> None:
    """
    Test the find_word function with various grids and words.
    """
    grid: Grid = Grid(
        data=[
            ["X", "M", "A", "S"],
            ["M", "A", "M", "X"],
            ["A", "T", "X", "M"],
        ]
    )
    assert find_word(grid, "XMAS") == 1  # "XMAS" appears once.
    assert find_word(grid, "SAM") == 1  # "SAM" appears once.
    assert find_word(grid, "TMS") == 1  # "TMS" appears once.
    assert find_word(grid, "AMX") == 4  # "XMA" appears four times.
    assert find_word(grid, "XMA") == 4  # "XMA" appears four times.
    assert find_word(grid, "MMX") == 0  # "MMX" does not appear.


def test_find_xmas() -> None:
    """
    Test the find_xmas function with a small grid.
    """
    """
    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........
    """
    grid: Grid = Grid(
        data=[
            [".", "M", ".", "S", ".", ".", ".", ".", ".", "."],
            [".", ".", "A", ".", ".", "M", "S", "M", "S", "."],
            [".", "M", ".", "S", ".", "M", "A", "A", ".", "."],
            [".", ".", "A", ".", "A", "S", "M", "S", "M", "."],
            [".", "M", ".", "S", ".", "M", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["S", ".", "S", ".", "S", ".", "S", ".", "S", "."],
            [".", "A", ".", "A", ".", "A", ".", "A", ".", "."],
            ["M", ".", "M", ".", "M", ".", "M", ".", "M", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    expected_result: int = 9
    assert find_xmas(grid) == expected_result


def test_part1_example() -> None:
    """
    Test the part1 function with the provided example in test_input.txt.
    """
    # Resolve the path to the test_input.txt file
    test_input_path: Path = Path(__file__).parent / "test_input.txt"

    # Read the test input data
    with test_input_path.open("r") as file:
        input_data: List[str] = file.read().splitlines()

    # Validate the result for part1
    expected_result: int = 18
    assert part1(input_data) == expected_result


def test_part2_example() -> None:
    """
    Test the part2 function with the example in test_input.txt.
    """
    test_input_path: Path = Path(__file__).parent / "test_input.txt"
    with test_input_path.open("r") as file:
        input_data: List[str] = file.read().splitlines()

    # Validate the result for part2
    expected_result: int = 9
    assert part2(input_data) == expected_result
