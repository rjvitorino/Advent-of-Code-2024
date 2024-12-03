import os
import re
from typing import List


def format_day(day: str, completed: bool) -> str:
    """
    Formats a single day with festive emojis and status.

    Args:
        day (str): The day (e.g., "Day 01").
        completed (bool): Whether the day is implemented.

    Returns:
        str: A formatted markdown string for the day.
    """
    # Emojis for completed and pending days
    completed_emoji = "⭐️"
    pending_emoji = "❄️"

    if completed:
        return f"- [x] {completed_emoji} **{day}**"
    else:
        return f"- [ ] {pending_emoji} {day}"


def update_readme_with_days(readme_path: str, src_path: str) -> None:
    """
    Updates the README file with festive formatted Advent of Code days.

    Args:
        readme_path (str): Path to the README file.
        src_path (str): Path to the source folder containing day directories (e.g., `src/`).

    Returns:
        None
    """
    # Generate a list of all days (Day 01 to Day 25)
    all_days = [f"Day {i:02}" for i in range(1, 26)]

    # Find existing day directories in the `src/` folder
    existing_days = {
        f"Day {folder[3:]}"
        for folder in os.listdir(src_path)
        if folder.startswith("day") and os.path.isdir(os.path.join(src_path, folder))
    }

    # Calculate stars and days completed directly from existing_days
    days_completed = len(existing_days)
    stars_collected = days_completed * 2  # Each day earns 2 stars

    # Format the list with emojis and checkmarks
    implemented_days = "\n".join(
        format_day(day, day in existing_days) for day in all_days
    )

    # Create the summary text
    summary_text = (
        f"**Stars Collected**: {stars_collected}/50 ⭐️\n"
        f"**Days Completed**: {days_completed}/25 🎄\n\n"
    )

    # Read the current content of the README file
    with open(readme_path, "r") as file:
        content = file.read()

    # Replace the placeholder block in the README
    updated_content = re.sub(
        r"<!-- IMPLEMENTED_DAYS -->(.*?)<!-- END_IMPLEMENTED_DAYS -->",
        f"<!-- IMPLEMENTED_DAYS -->\n{summary_text}{implemented_days}\n<!-- END_IMPLEMENTED_DAYS -->",
        content,
        flags=re.DOTALL,
    )

    # Write back the updated README
    with open(readme_path, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":
    # Paths to README and src folder
    readme_path: str = "README.md"  # Path to the README file
    src_path: str = "src"  # Path to the source folder

    # Update the README with the implemented days
    update_readme_with_days(readme_path, src_path)
