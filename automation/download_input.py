import os
import requests
from datetime import datetime

AOC_YEAR = 2024
SESSION_COOKIE = os.getenv("AOC_SESSION")
BASE_URL = f"https://adventofcode.com/{AOC_YEAR}/day"


def download_input(day):
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    input_url = f"{BASE_URL}/{day}/input"
    desc_url = f"{BASE_URL}/{day}"

    # Fetch input data
    print(desc_url)
    response = requests.get(input_url, headers=headers)
    response.raise_for_status()
    input_data = response.text

    # Save input file
    day_folder = f"src/day{day:02d}"
    os.makedirs(day_folder, exist_ok=True)
    with open(os.path.join(day_folder, "input.txt"), "w") as f:
        f.write(input_data)

    # Optionally fetch description (part 1)
    desc_response = requests.get(desc_url, headers=headers)
    desc_response.raise_for_status()

    with open(os.path.join(day_folder, "description.md"), "w") as f:
        f.write(desc_response.text)

    print(f"Downloaded data for Day {day}.")


if __name__ == "__main__":
    today = datetime.now()
    day = today.day
    download_input(day)
