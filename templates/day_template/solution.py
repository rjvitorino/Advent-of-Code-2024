from pathlib import Path


def part1(data):
    # Solve part 1
    pass


def part2(data):
    # Solve part 2
    pass


if __name__ == "__main__":
    # Dynamically resolve the input file path
    current_dir = Path(__file__).parent
    input_file = current_dir / "input.txt"

    # Read the input data
    with input_file.open("r") as file:
        data = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
