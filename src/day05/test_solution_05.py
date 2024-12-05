import pytest
from pathlib import Path
from .day05_solution import (
    parse_rules_and_updates,
    is_update_valid,
    middle_page_sum,
    sort_update,
    part1,
    part2,
)

TEST_INPUT_FILE = Path(__file__).parent / "test_input.txt"
TEST_RULES = [(47, 53), (97, 13), (97, 61), (97, 47), (75, 29)]
TEST_UPDATES = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]


def test_parse_rules_and_updates() -> None:
    """
    Test parse_rules_and_updates function.
    """
    example_input = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
    ]
    rules, updates = parse_rules_and_updates(example_input)
    assert rules == TEST_RULES
    assert updates == TEST_UPDATES


def test_is_update_valid() -> None:
    """
    Test is_update_valid function with both valid and invalid updates.
    """
    rules = [(1, 2), (2, 3), (4, 5)]

    # Valid cases
    assert is_update_valid([1, 2, 3], rules) is True
    assert is_update_valid([4, 5], rules) is True
    assert is_update_valid(TEST_UPDATES[0], TEST_RULES) is True

    # Invalid cases
    assert is_update_valid([2, 1, 3], rules) is False  # Violates 1 -> 2
    assert is_update_valid([1, 3, 2], rules) is False  # Violates 2 -> 3
    assert is_update_valid([5, 4], rules) is False  # Violates 4 -> 5
    assert (
        is_update_valid([47, 75, 97, 61, 53], TEST_RULES) is False
    )  # Violates 97 -> 47


def test_middle_page_sum() -> None:
    """
    Test middle_page_sum function.
    """
    valid_updates = TEST_UPDATES[:2]
    assert middle_page_sum(valid_updates) == 61 + 53


def test_sort_update() -> None:
    """
    Test sort_update function with simple and complex rules.
    """
    rules = [(1, 2), (2, 3), (4, 5)]

    # Case 1: Already sorted
    assert sort_update([1, 2, 3], rules) == [1, 2, 3]

    # Case 2: Needs sorting
    assert sort_update([3, 1, 2], rules) == [1, 2, 3]
    assert sort_update([5, 4], rules) == [4, 5]

    # Case 3: Complex dependencies
    complex_rules = [(1, 2), (1, 3), (2, 4), (3, 4)]
    assert sort_update([4, 3, 2, 1], complex_rules) == [1, 2, 3, 4]

    # Case 4: Independent elements
    independent_rules = [(1, 2), (3, 4)]
    assert sort_update([4, 3, 2, 1], independent_rules) == [1, 2, 3, 4]


def test_part1() -> None:
    """
    Test Part 2 with example input from test_input.txt.
    """
    with TEST_INPUT_FILE.open("r") as file:
        data = file.read().splitlines()
    expected_result = 143
    assert part1(data) == expected_result


def test_part2() -> None:
    """
    Test Part 2 with example input from test_input.txt.
    """
    with TEST_INPUT_FILE.open("r") as file:
        data = file.read().splitlines()
    expected_result = 123
    assert part2(data) == expected_result
