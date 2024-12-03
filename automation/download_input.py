import os
import requests
from datetime import datetime
from typing import Optional
from bs4 import BeautifulSoup
from markdownify import markdownify
from dotenv import load_dotenv
import pytz

# Load environment variable(s) from .env
load_dotenv()

AOC_YEAR: int = 2024
SESSION_COOKIE: Optional[str] = os.getenv("AOC_SESSION")
BASE_URL: str = f"https://adventofcode.com/{AOC_YEAR}/day"


def download_input(day: int) -> None:
    """
    Downloads the input and description for a specific Advent of Code day.

    Args:
        day (int): The day of the Advent of Code challenge (1-25).

    Raises:
        ValueError: If the session cookie is not set.
        HTTPError: If the HTTP request fails.
    """
    if not SESSION_COOKIE:
        raise ValueError("AOC_SESSION environment variable is not set.")

    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    input_url: str = f"{BASE_URL}/{day}/input"
    desc_url: str = f"{BASE_URL}/{day}"

    # Fetch input data from the website
    print(f"Fetching input data from: {input_url}")
    response = requests.get(input_url, headers=headers)
    response.raise_for_status()
    input_data: str = response.text

    # Create day folder for the code
    day_folder: str = f"src/day{day:02d}"
    os.makedirs(day_folder, exist_ok=True)

    # Save input file
    input_path: str = os.path.join(day_folder, "input.txt")
    with open(input_path, "w") as f:
        f.write(input_data)

    print(f"Input data saved to {input_path}.")

    # Fetch and save html description
    print(f"Fetching description from: {desc_url}")
    desc_response = requests.get(desc_url, headers=headers)
    desc_response.raise_for_status()

    # Extract <main> content from the HTML
    soup = BeautifulSoup(desc_response.text, "html.parser")
    main_content = soup.select_one("body > main")  # Select <main> inside <body>
    if main_content is None:
        raise ValueError("Could not find <main> content in the HTML.")

    # Convert HTML to Markdown
    markdown_content = markdownify(str(main_content))
    print(markdown_content)

    desc_path: str = os.path.join(day_folder, f"description{day}.md")
    with open(desc_path, "w") as f:
        f.write(markdown_content)

    print(f"Description saved to {desc_path}.")
    print(f"Downloaded data for Day {day}.")


if __name__ == "__main__":
    local_tz = pytz.timezone("UTC")
    today: datetime = datetime.now(tz=local_tz)
    day: int = today.day
    download_input(day)
