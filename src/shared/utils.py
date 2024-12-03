# from math import gcd
from math import lcm
from functools import reduce
from typing import Callable, List, Tuple, Optional, Any
from collections import deque
import re


def parse_input(file_path: str) -> List[str]:
    """
    Parses an input file into a list of stripped strings.

    Args:
        file_path (str): Path to the input file.

    Returns:
        List[str]: List of lines from the file, stripped of whitespace.
    """
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def parse_ints(file_path: str) -> List[int]:
    """
    Parses an input file into a list of integers.

    Args:
        file_path (str): Path to the input file.

    Returns:
        List[int]: List of integers from the file.
    """
    with open(file_path, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def parse_grid(file_path: str) -> List[List[str]]:
    """
    Parses an input file into a 2D grid of characters.

    Args:
        file_path (str): Path to the input file.

    Returns:
        List[List[str]]: 2D list representing the grid.
    """
    with open(file_path, "r") as f:
        return [list(line.strip()) for line in f.readlines()]


def neighbors(x: int, y: int, include_diagonals: bool = False) -> List[Tuple[int, int]]:
    """
    Computes the neighbors of a cell in a grid.

    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        include_diagonals (bool): Whether to include diagonal neighbors.

    Returns:
        List[Tuple[int, int]]: List of neighboring coordinates.
    """
    offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),  # Cardinal directions
    ]
    if include_diagonals:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    return [(x + dx, y + dy) for dx, dy in offsets]


def lcmm(numbers: List[int]) -> int:
    """
    Computes the least common multiple of multiple integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The least common multiple of all integers in the list.
    """
    return reduce(lcm, numbers)


def bfs(
    start: Any,
    is_goal: Callable[[Any], bool],
    get_neighbors: Callable[[Any], List[Any]],
) -> Optional[Any]:
    """
    Performs Breadth-First Search (BFS) to find a goal node.

    Args:
        start (Any): The starting node.
        is_goal (Callable[[Any], bool]): A function to check if a node is the goal.
        get_neighbors (Callable[[Any], List[Any]]): A function to get the neighbors of a node.

    Returns:
        Optional[Any]: The goal node if found, None otherwise.
    """
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if is_goal(node):
            return node
        queue.extend(get_neighbors(node))
    return None


def extract_pattern(
    text: str, pattern: str, transform: Callable[[tuple[str, ...]], Any] = lambda x: x
) -> list[Any]:
    """
    Extracts matches of a given pattern from a text and applies a transformation function to each match.

    Args:
        text (str): The input text to search.
        pattern (str): A regular expression pattern to find matches.
        transform (Callable): A function to transform each match tuple into the desired output format.

    Returns:
        list[Any]: A list of transformed matches.
    """
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.findall(text)
    return [transform(match) for match in matches]


def convert_str_tuple_to_int(match: tuple[str, str]) -> tuple[int, int]:
    """
    Transform regex match tuples into integers.
    """
    return int(match[0]), int(match[1])
