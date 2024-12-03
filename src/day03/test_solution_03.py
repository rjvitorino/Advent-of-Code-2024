import pytest
from typing import List
from shared.utils import extract_pattern, convert_str_tuple_to_int
from .day03_solution import extract_valid_mul_instructions, part1, part2


@pytest.fixture
def example_data() -> List[str]:
    """
    Fixture for part 1 example input data as a list of strings.
    """
    return ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]


def test_extract_valid_mul_instructions() -> None:
    """
    Test the extract_valid_mul_instructions utility function.
    """
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = [(2, 4), (5, 5), (11, 8), (8, 5)]
    assert extract_valid_mul_instructions(memory) == expected


def test_extract_pattern() -> None:
    """
    Test the generic extract_pattern utility function.
    """
    text = "mul(2,4)mul(3,5)invalid(6,7)"
    pattern = r"mul\((\d+),(\d+)\)"
    expected = [(2, 4), (3, 5)]
    assert extract_pattern(text, pattern, convert_str_tuple_to_int) == expected


def test_part1(example_data: List[str]) -> None:
    """
    Test part1 of the solution with example input.
    """
    expected_result = 161  # 2*4 + 11*8 + 8*5
    assert part1(example_data) == expected_result


@pytest.fixture
def example_data2() -> List[str]:
    """
    Fixture for part 2 example input data as a list of strings.
    """
    return ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


def test_part2(example_data2: List[str]) -> None:
    expected_result = 48  # 2*4 + 8*5
    result = part2(example_data2)
    print(f"Debugging: Part 2 result = {result}")
    assert result == expected_result
