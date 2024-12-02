from pathlib import Path
from typing import List
from shared.utils import parse_input


def is_safe(report: List[int]) -> bool:
    """Check if a report is safe based on the rules."""
    if len(report) < 2:
        return False

    # Compute differences between adjacent levels
    diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]

    # Rule: All differences must be within [1, 3]
    if not all(1 <= d <= 3 for d in diffs):
        return False

    # Rule: The report must be strictly increasing or decreasing
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    return is_increasing or is_decreasing


def can_be_safe_with_removal(report: List[int]) -> bool:
    """
    Check if a report can be made safe by removing one level.

    Args:
        report (List[int]): A single report represented as a list of integers.

    Returns:
        bool: True if the report can be made safe by removing one level, False otherwise.
    """
    if len(report) <= 2:
        return (
            True  # Removing one level would leave 1 or 2 levels, which is always safe.
        )

    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def part1(data: List[str]) -> int:
    """
    Solve part 1 of the challenge and count the number of safe reports.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 1.
    """
    # Parse the input into reports as lists of integers
    reports = [list(map(int, line.split())) for line in data]
    # Count the number of safe reports
    return sum(1 for report in reports if is_safe(report))


def part2(data: List[str]) -> int:
    """
    Solve part 2 of the challenge and recount the number of safe reports.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 2.
    """
    reports = [list(map(int, line.split())) for line in data]
    return sum(
        1 for report in reports if is_safe(report) or can_be_safe_with_removal(report)
    )


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
