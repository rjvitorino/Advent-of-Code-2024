from pathlib import Path
from typing import List, Tuple
import re

from shared.utils import extract_pattern, convert_str_tuple_to_int


def extract_valid_mul_instructions(memory: str) -> list[tuple[int, int]]:
    """
    Extracts valid mul(X,Y) instructions from a memory string.
    Returns a list of tuples (X, Y) representing the operands.
    """
    pattern = r"mul\((\d+),(\d+)\)"
    return extract_pattern(memory, pattern, convert_str_tuple_to_int)


def extract_valid_state_mul_instructions(
    memory: str,
) -> List[Tuple[str, int | None, int | None]]:
    """
    Extracts valid mul(X,Y) instructions and state-changing instructions (do(), don't()) from a memory string.
    Returns a list of tuples representing instructions and their types.
    """
    # Updated regex: Matches mul(X,Y), do(), and don't() with surrounding jibberish
    pattern = r"[^\s\(\)\[\]]*?(mul\((\d+),(\d+)\)|don\'t\(\)|do\(\))"

    def transform(match: re.Match) -> Tuple[str, int | None, int | None]:
        if match.group(2) and match.group(3):  # Matches `mul(X,Y)`
            return "mul", int(match.group(2)), int(match.group(3))
        elif "do()" in match.group(1):  # Matches `do()` exactly
            return "do", None, None
        elif "don't()" in match.group(1):  # Matches `don't()` exactly
            return "don't", None, None

    # Use `re.finditer` to iterate over matches and apply the transformation
    # print(f"Debugging: Memory = {memory}")
    parsed_instructions = [transform(m) for m in re.finditer(pattern, memory)]
    # print(f"Debugging: Parsed Instructions = {parsed_instructions}")
    return parsed_instructions


def part1(data: List[str]) -> int:
    """
    Solve part 1 of the challenge.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 1.
    """
    # Join the input data into a single string (if multiline input)
    memory = " ".join(data)

    # Extract valid instructions and compute the sum of their results
    instructions = extract_valid_mul_instructions(memory)
    return sum(x * y for x, y in instructions)


def part2(data: List[str]) -> int:
    """
    Solve part 2 of the challenge.

    Args:
        data (List[str]): The input data as a list of strings.

    Returns:
        int: The solution to part 2.
    """
    memory = " ".join(data)
    instructions = extract_valid_state_mul_instructions(memory)

    # Keep track of whether mul instructions are enabled
    mul_enabled = True
    total = 0

    for instr, x, y in instructions:
        if instr == "do":
            mul_enabled = True
            # print("Debugging: do() encountered, mul_enabled = True")
        elif instr == "don't":
            mul_enabled = False
            # print("Debugging: don't() encountered, mul_enabled = False")
        elif instr == "mul":
            if mul_enabled:
                # print(f"Debugging: mul({x}, {y}) executed, adding {x * y} to total")
                total += x * y
            else:
                # print(f"Debugging: mul({x}, {y}) skipped, mul_enabled = False")
                pass

    # print(f"Debugging: Final total = {total}")
    return total


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir: Path = Path(__file__).parent
    input_file: Path = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data: List[str] = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
