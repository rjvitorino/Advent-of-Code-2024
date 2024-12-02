import pytest
from solution import is_safe, can_be_safe_with_removal, part1, part2


@pytest.mark.parametrize(
    "report, expected",
    [
        ([7, 6, 4, 2, 1], True),  # Decreasing by valid steps
        ([1, 2, 7, 8, 9], False),  # Increase of 5 is invalid
        ([9, 7, 6, 2, 1], False),  # Decrease of 4 is invalid
        ([1, 3, 2, 4, 5], False),  # Not monotonic
        ([8, 6, 4, 4, 1], False),  # Repetition (4,4) is invalid
        ([1, 3, 6, 7, 9], True),  # Increasing by valid steps
    ],
)
def test_is_safe(report, expected):
    """
    Test the is_safe function with various inputs.
    """
    assert is_safe(report) == expected


@pytest.mark.parametrize(
    "report, expected",
    [
        ([7, 6, 4, 2, 1], True),  # Already safe
        ([1, 2, 7, 8, 9], False),  # Cannot be made safe
        ([9, 7, 6, 2, 1], False),  # Cannot be made safe
        ([1, 3, 2, 4, 5], True),  # Safe by removing second level
        ([8, 6, 4, 4, 1], True),  # Safe by removing third level
        ([1, 3, 6, 7, 9], True),  # Already safe
    ],
)
def test_can_be_safe_with_removal(report, expected):
    """
    Test the can_be_safe_with_removal function with various inputs.
    """
    assert can_be_safe_with_removal(report) == expected


def test_part1(tmp_path):
    """
    Test part1 with example input data.
    """
    # Example input data from the problem description
    input_data = (
        "7 6 4 2 1\n"
        "1 2 7 8 9\n"
        "9 7 6 2 1\n"
        "1 3 2 4 5\n"
        "8 6 4 4 1\n"
        "1 3 6 7 9\n"
    )
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_data)

    # Read input lines as a list of strings
    input_lines = input_data.strip().split("\n")

    # Verify part1 result
    assert part1(input_lines) == 2


def test_part2(tmp_path):
    """
    Test part2 with example input data.
    """
    input_data = (
        "7 6 4 2 1\n"
        "1 2 7 8 9\n"
        "9 7 6 2 1\n"
        "1 3 2 4 5\n"
        "8 6 4 4 1\n"
        "1 3 6 7 9\n"
    )
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_data)

    input_lines = input_data.strip().split("\n")
    assert part2(input_lines) == 4
