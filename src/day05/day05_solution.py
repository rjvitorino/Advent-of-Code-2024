from pathlib import Path
from typing import List, Tuple
from shared.data_classes import TopologicalSorter


def parse_rules_and_updates(
    data: List[str],
) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """
    Parses the rules and updates from the input data.

    Args:
        data (List[str]): The input data.

    Returns:
        Tuple[List[Tuple[int, int]], List[List[int]]]: A tuple of rules and updates.
    """
    divider_index = data.index("")
    rules = [tuple(map(int, line.split("|"))) for line in data[:divider_index]]
    updates = [list(map(int, line.split(","))) for line in data[divider_index + 1 :]]
    return rules, updates


def is_update_valid(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    """
    Checks if an update respects the ordering rules.

    Args:
        update (List[int]): The update to check. Each element represents a page in a specific order.
        rules (List[Tuple[int, int]]): The ordering rules as pairs (x, y), where `x` must appear before or at the same position as `y` in the `update`.

    Returns:
        bool: True if the `update` satisfies all the ordering rules, False otherwise.
    """
    # Create a mapping of each page's position in the update
    # Example: If update = [75, 47, 61, 53, 29], position = {75: 0, 47: 1, 61: 2, 53: 3, 29: 4}
    position = {page: i for i, page in enumerate(update)}

    # Validate that all rules are respected:
    # - For each rule (x, y), check if x appears before or at the same position as y.
    # - Ignore rules where either x or y is not in the update.
    return all(
        position.get(x, -1)
        <= position.get(y, -1)  # Ensure x comes before or at the same position as y
        for x, y in rules  # Iterate over all rules
        if x in position
        and y in position  # Only consider rules where both x and y are in the update
    )


def filter_updates(
    updates: List[List[int]], rules: List[Tuple[int, int]], valid: bool = True
) -> List[List[int]]:
    """
    Filters updates based on their validity according to the rules.

    Args:
        updates (List[List[int]]): The list of updates to filter.
        rules (List[Tuple[int, int]]): The ordering rules.
        valid (bool): If True, filters for valid updates. If False, filters for invalid updates.

    Returns:
        List[List[int]]: The filtered list of updates.
    """
    # Use a list comprehension to filter updates:
    # - Keeps updates if `is_update_valid(update, rules)` matches the `valid` flag.
    # - If `valid` is True, only valid updates are kept.
    # - If `valid` is False, only invalid updates are kept.
    return [update for update in updates if is_update_valid(update, rules) == valid]


def middle_page_sum(valid_updates: List[List[int]]) -> int:
    """
    Calculates the sum of the middle pages of valid updates.

    Args:
        valid_updates (List[List[int]]): List of valid updates.

    Returns:
        int: The sum of the middle pages.
    """
    return sum(update[len(update) // 2] for update in valid_updates)


def sort_update(update: List[int], rules: List[Tuple[int, int]]) -> List[int]:
    """
    Sorts an update according to the given rules.

    Args:
        update (List[int]): The update to sort.
        rules (List[Tuple[int, int]]): The ordering rules.

    Returns:
        List[int]: The sorted update.
    """
    sorter = TopologicalSorter()

    # Build the graph with the relevant rules
    for x, y in rules:
        if x in update and y in update:
            sorter.add_edge(x, y)

    # Perform the topological sort
    return sorter.sort(update)


def part1(data: List[str]) -> int:
    """
    Solve Part 1 of the challenge.

    Args:
        data (List[str]): The input data.

    Returns:
        int: The count of valid updates.
    """
    rules, updates = parse_rules_and_updates(data)
    valid_updates = filter_updates(updates, rules, valid=True)
    return middle_page_sum(valid_updates)


def part2(data: List[str]) -> int:
    """
    Solve Part 2 of the challenge.

    Args:
        data (List[str]): The input data.

    Returns:
        int: The sum of the middle pages of corrected updates.
    """
    rules, updates = parse_rules_and_updates(data)
    invalid_updates = filter_updates(updates, rules, valid=False)
    corrected_updates = [sort_update(update, rules) for update in invalid_updates]
    return middle_page_sum(corrected_updates)


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
