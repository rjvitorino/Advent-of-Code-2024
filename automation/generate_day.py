import os
import shutil
from datetime import datetime

TEMPLATE_DIR = "templates/day_template"


def generate_day(day):
    day_folder = f"src/day{day:02d}"
    if os.path.exists(day_folder):
        print(f"Day {day:02d} folder already exists.")
        return
    shutil.copytree(TEMPLATE_DIR, day_folder)
    print(f"Generated files for Day {day:02d}.")


if __name__ == "__main__":
    today = datetime.now()
    generate_day(today.day)
