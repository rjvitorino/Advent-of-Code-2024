import os
import shutil
from datetime import datetime
from typing import Optional


TEMPLATE_DIR = "templates/day_template"


def generate_day(day: int, base_dir: str = "src") -> None:
    """
    Generates the folder and files for a specific day of Advent of Code.

    Args:
        day (int): The day number to generate (e.g., 1 for Day 1).
        base_dir (str): The base directory where the day folder will be created.

    Returns:
        None
    """
    # Ensure the day number is zero-padded
    day_str = f"day{day:02d}"
    day_folder = os.path.join(base_dir, day_str)

    # Check if the folder already exists
    if os.path.exists(day_folder):
        print(f"Day {day:02d} folder already exists.")
        return

    # Create the new day folder
    os.makedirs(day_folder)

    # Generate files with proper naming conventions
    solution_file = os.path.join(day_folder, f"{day_str}_solution.py")
    test_solution_file = os.path.join(day_folder, f"test_solution_{day:02d}.py")
    description_file = os.path.join(day_folder, f"description{day}.md")
    input_file = os.path.join(day_folder, "input.txt")
    test_input_file = os.path.join(day_folder, "test_input.txt")
    init_file = os.path.join(day_folder, "__init__.py")

    # Populate the folder with template files or placeholders
    shutil.copy(os.path.join(TEMPLATE_DIR, "solution.py"), solution_file)
    shutil.copy(os.path.join(TEMPLATE_DIR, "test_solution.py"), test_solution_file)
    open(description_file, "w").close()  # Create an empty markdown file
    open(input_file, "w").close()  # Create an empty input file
    open(test_input_file, "w").close()  # Create an empty test input file
    open(init_file, "w").close()  # Create an empty __init__.py file

    print(f"Generated files for {day_str}.")


if __name__ == "__main__":
    today = datetime.now()
    generate_day(today.day)
