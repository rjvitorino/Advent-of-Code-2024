from collections import Counter
from pathlib import Path
from typing import List, Tuple
from shared.utils import parse_input


def parse_location_ids(data: List[str]) -> Tuple[List[int], List[int]]:
    """
    Parses the input data to extract two lists of location IDs.

    Args:
        data (List[str]): List of input lines.

    Returns:
        Tuple[List[int], List[int]]: Two lists of location IDs.
    """
    left: List[int] = []
    right: List[int] = []
    for line in data:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    return left, right


def calculate_total_distance(left: List[int], right: List[int]) -> int:
    """
    Calculates the total distance between two lists of integers.

    Args:
        left (List[int]): The first list of integers.
        right (List[int]): The second list of integers.

    Returns:
        int: The total distance between paired integers.
    """
    left.sort()
    right.sort()
    return sum(abs(a - b) for a, b in zip(left, right))


def calculate_similarity_score(left: List[int], right: List[int]) -> int:
    """
    Calculates the similarity score for Part 2.

    Args:
        left (List[int]): The first list of integers.
        right (List[int]): The second list of integers.

    Returns:
        int: The similarity score.
    """
    right_counts: Counter[int] = Counter(right)
    return sum(num * right_counts[num] for num in left)


def part1(data: List[str]) -> int:
    left, right = parse_location_ids(data)
    return calculate_total_distance(left, right)


def part2(data: List[str]) -> int:
    left, right = parse_location_ids(data)
    return calculate_similarity_score(left, right)


if __name__ == "__main__":
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
