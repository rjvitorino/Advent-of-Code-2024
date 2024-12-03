import os
import re
from typing import List


def update_readme_with_days(readme_path: str, src_path: str) -> None:
    """
    Updates the README file to list all Advent of Code days (Day 01 to Day 24).
    Marks completed days with a checkmark based on existing directories.

    Args:
        readme_path (str): Path to the README file.
        src_path (str): Path to the source folder containing day directories (e.g., `src/`).

    Returns:
        None
    """
    # Generate a list of all days (Day 01 to Day 24)
    all_days: List[str] = [f"Day {i:02}" for i in range(1, 25)]

    # Find existing `dayXX` directories in the `src/` folder
    existing_days: List[str] = [
        f"Day {folder[3:]}"
        for folder in os.listdir(src_path)
        if folder.startswith("day") and os.path.isdir(os.path.join(src_path, folder))
    ]

    # Format the list of all days with checkmarks for existing directories
    implemented_days: str = "\n".join(
        f"- [{'x' if day in existing_days else ' '}] {day}" for day in all_days
    )

    # Read the current content of the README file
    with open(readme_path, "r") as file:
        content: str = file.read()

    # Use regex to replace the placeholder block in the README
    updated_content: str = re.sub(
        r"<!-- IMPLEMENTED_DAYS -->(.*?)<!-- END_IMPLEMENTED_DAYS -->",
        f"<!-- IMPLEMENTED_DAYS -->\n{implemented_days}\n<!-- END_IMPLEMENTED_DAYS -->",
        content,
        flags=re.DOTALL,  # Allows matching across multiple lines
    )

    # Write the updated content back to the README file
    with open(readme_path, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":
    # Paths to README and src folder
    readme_path: str = "README.md"  # Path to the README file
    src_path: str = "src"  # Path to the source folder

    # Update the README with the implemented days
    update_readme_with_days(readme_path, src_path)
