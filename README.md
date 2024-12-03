# 🎅 Advent of Code 2024 - Python Setup 🐍

Welcome to my **Advent of Code 2024** repository! This project is designed to streamline solving AoC puzzles using Python, focusing on **code reuse**, **automation**, and **testing**.

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-yellow.svg)


---

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Quickstart](#quickstart)
  - [Step-by-step instructions](#step-by-step-instructions)
      - [Install Dependencies](#1-install-dependencies)
      - [Configure Cookie Session](#2-configure-advent-of-code-session)
      - [Run Automation Scripts](#3-run-automation-scripts)
  - [Troubleshooting](#troubleshooting)
- [How to Solve a Day](#how-to-solve-a-day)
- [Tools and Techniques](#tools-and-techniques)
  - [Data Structures and Utilities](#data-structures-and-utilities)
  - [Algorithms](#algorithms)
  - [Libraries](#libraries)
  - [Templates](#templates)
  - [Recommended Libraries for Future Exercises](#recommended-libraries-for-future-exercises)
- [Developer Tips](#developer-tips)
- [Contributing](#contributing)
- [License](#license)

---

## 🎄 Progress Tracker (2024) 🎅
<!-- IMPLEMENTED_DAYS -->
**Stars Collected**: 6/50 ⭐️
**Days Completed**: 3/25 🎄

- [x] ⭐️ **Day 01**
- [x] ⭐️ **Day 02**
- [x] ⭐️ **Day 03**
- [ ] ❄️ Day 04
- [ ] ❄️ Day 05
- [ ] ❄️ Day 06
- [ ] ❄️ Day 07
- [ ] ❄️ Day 08
- [ ] ❄️ Day 09
- [ ] ❄️ Day 10
- [ ] ❄️ Day 11
- [ ] ❄️ Day 12
- [ ] ❄️ Day 13
- [ ] ❄️ Day 14
- [ ] ❄️ Day 15
- [ ] ❄️ Day 16
- [ ] ❄️ Day 17
- [ ] ❄️ Day 18
- [ ] ❄️ Day 19
- [ ] ❄️ Day 20
- [ ] ❄️ Day 21
- [ ] ❄️ Day 22
- [ ] ❄️ Day 23
- [ ] ❄️ Day 24
- [ ] ❄️ Day 25
<!-- END_IMPLEMENTED_DAYS -->

## Project Structure

```yaml
advent_of_code/
├── .vscode/                      # VS Code settings
├── .env                          # Environment configuration for UV
│
├── automation/                   # Automation scripts
│   ├── download_input.py         # Downloads input and exercise description from the website
│   └── generate_day.py           # Generates day structure for each day in the Advent of Code
│
├── src/                          # Source code for each day
│   ├── day01/
│   │   ├── __init__.py           # Python module initialization
│   │   ├── day01_solution.py     # Solution file with a consistent naming convention
│   │   ├── description1.md       # Puzzle description in markdown
│   │   ├── input.txt             # Puzzle input
│   │   ├── test_input.txt        # Example input for tests
│   │   ├── test_solution_01.py   # Unit tests for day 01
│   ├── day02/
│   │   ├── __init__.py           # Python module initialization
│   │   ├── day02_solution.py     # Solution file for day 02
│   │   └── ...
│   ├── dayXX/
│   │   ├── __init__.py           # Python module initialization
│   │   ├── dayXX_solution.py     # Solution file for day XX
│   │   └── ...
│   │
│   └── shared/                   # Shared utilities and data classes
│       ├── data_classes.py       # Data classes for reusable components like Grid and Point
│       └── utils.py              # Utility functions for parsing, grid operations, etc.
│
├── templates/
│   └── day_template/             # Template for new days
│       ├── input.txt             # Empty file to store the input from the website
│       ├── test_input.txt        # Empty file to store a simplified input example
│       ├── solution.py           # Starter solution with type hints and structure
│       └── test_solution.py      # Starter test suite with type hints
│ 
├── README.md                     # This file
├── pyproject.toml                # Python project configuration
└── requirements.txt              # Project requirements to run the files
```

---

## Setup

### Prerequisites
- Python 3.13 or higher
- UV package manager
- Git

### Quickstart

```bash
gh repo clone rjvitorino/advent-of-code-2024
cd advent_of_code
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Step-by-step instructions

#### 1. Install Dependencies

Ensure you install Python and **set up a virtual environment [using uv](https://docs.astral.sh/uv/)**. Install the dependencies:

```bash
uv pip install -r requirements.txt
```

This will install all necessary libraries, including:

* `beautifulsoup4`: For parsing HTML to extract puzzle descriptions.
* `markdownify`: For converting HTML puzzle descriptions to Markdown.
* `python-dotenv`: Loads environment variables from a `.env` file.

#### 2. Configure Advent of Code Session

- Set your Advent of Code **session cookie** to download inputs and descriptions. 
You can find this in your browser's cookies after logging into the AoC website.
- Ensure the `.env` file is placed in the **root directory** of the project, where the `automation/` folder is located with the following content:

```yaml
AOC_SESSION=your_session_cookie_here
```

- Alternatively, export the session variable in your shell:

```bash
export AOC_SESSION=your_session_cookie_here
```

#### 3. Run Automation Scripts

1. **Generate folder structure for a day in the Advent of Code:**

```bash
uv run python automation/generate_day.py
```

2. **Download input file and challenge description for a day in the Advent of Code:**

```bash
uv run python automation/download_input.py
```

This script performs the following:

* Downloads the puzzle input and saves it as `input.txt`.
* Dynamically generates the Markdown description as `description{day}.md` based on the day number.

3. **Dynamically update README with implemented days:**

```bash
uv run python automation/update_readme_days.py
```

This script performs the following:

- Generates a list of all 24 Advent of Code days (Day 01 to Day 25).
- Checks which days are implemented by looking for corresponding `src/dayXX` folders.
- Updates the `README.md` under the "[**Progress Tracker**](#-progress-tracker-2024-)" section:
  - Marks completed days with a star emoji (⭐️) and a checkmark ([x]).
  - Marks incomplete days with a snowflake emoji (❄️) and an empty checkbox ([ ]).
  - Calculates the 




### Troubleshooting
- **Session Cookie Issues**: Make sure your session cookie is valid and properly formatted
- **UV Installation**: If UV isn't recognized, ensure it's properly installed...

---

## How to solve a day in the Advent of Code

### 1. Write your solution

  - Implement the solution in `src/dayXX/dayXX_solution.py`, using **type hints** and reusable **utilities** to ensure clarity and consistency.
  - Type hints help catch bugs early and provide better IDE support.
  - Example:

    ```python
    def part1(data: List[str]) -> int:
      pass

    def part2(data: List[str]) -> int:
      pass
    ```

### 2. Write your tests

  - Create test cases in `src/dayXX/test_solution_XX.py`, using type hints and the provided template.
  - Example:

    ```python
    def test_part1() -> None:
        example_input: List[str] = ["test input"]
        expected_result: int = 42
        assert part1(example_input) == expected_result
    ```

### 3. Run and validate your code

  - Test your solution with `pytest`:

    ```bash
    uv tool run pytest
    ```

  - Check linting with `ruff`:
    
    ```bash
    uv tool run ruff check .
    ```
  
  - Format the code with `ruff`:
    
    ```bash
    uv tool run ruff format .
    ```

  - Run your solution:
    
    ```bash
    uv run -m src.dayXX.solution
    ```

---

## Tools and Techniques

### Data Structures and Utilities

#### Data Classes
- **Point**: Represents a 2D point with arithmetic operations (`+`, `-`), useful for grid-based navigation.
- **Grid**: A 2D data structure with methods for safe element access and modification.
  - `grid.get(x, y, default=None)`: Retrieves an element safely with bounds checking.
  - `grid.set(x, y, value)`: Sets a value at specified coordinates.
- **Range**: A numerical range with utilities for checking overlaps and containment.
  - `range.overlaps(other_range)`: Checks if two ranges overlap.
  - `range.contains(value)`: Determines if a value lies within the range.

#### Utility Functions
- **Input Parsing:**
  - `parse_input(file_path)`: Reads a file into a list of stripped strings.
  - `parse_ints(file_path)`: Reads a file into a list of integers.
  - `parse_grid(file_path)`: Parses a file into a 2D grid of characters.
- **Grid Operations:**
  - `neighbors(x, y, include_diagonals=False)`: Computes the neighbors of a cell in a grid. Supports diagonal neighbors when specified.
- **Mathematical Utilities:**
  - `gcd(a, b)`: Computes the greatest common divisor.
  - `lcm(a, b)`: Computes the least common multiple of two integers.
  - `lcmm(numbers)`: Computes the least common multiple of a list of integers.
- **Graph Traversals:**
  - `bfs(start, is_goal, get_neighbors)`: Implements Breadth-First Search (BFS) to find a goal node.
- **Regex extractions and transformations:**
  - `extract_pattern`: Extracts text and transforms it based on a regular expression.
  - `convert_str_tuple_to_int`: Converts content matched from a regular expression (string tuples) into integers for easier handling.

---

### Algorithms

#### Common Patterns
- **Graph Traversals:**
  - Use `bfs` for shortest paths or goal-oriented searches in grids and graphs.
- **Dynamic Programming:**
  - Solve problems with overlapping subproblems (e.g., caching intermediate results).
- **Grid-Based Navigation:**
  - Combine the `Point` and `Grid` data structures for efficient manipulation of 2D grids.

#### Techniques for Optimization
- **Efficient Counting:**
  - Use `collections.Counter` to count occurrences in lists or strings.
- **Prime Numbers:**
  - Use `sympy` or implement Sieve of Eratosthenes for prime number generation.

---

### Libraries

#### Libraries used
- `beautifulsoup4`: Parses HTML for extracting puzzle descriptions.
- `markdownify`: Converts HTML puzzle descriptions into Markdown.
- `python-dotenv`: Manages environment variables for session configuration.

#### Templates
The project includes pre-built templates for solutions and tests:
- `solution.py`:
  - Uses type hints for inputs and outputs.
  - Dynamically resolves input file paths.
- `test_solution.py`:
  - Includes type hints for inputs and expected outputs.
  - Provides placeholders for example inputs and expected results.

#### Recommended Libraries for future exercises
- `networkx`: For advanced graph algorithms and visualization.
- `sympy`: For symbolic mathematics, including prime number utilities.
- `numpy`: For numerical computations, useful in multi-dimensional arrays.
- `itertools`: For generating permutations, combinations, and Cartesian products.

---

### Example Usage

#### Using Data Classes

```python
from shared.data_classes import Point, Grid

# Example: Move a point
p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2  # Point(x=4, y=6)

# Example: Create and query a grid
grid = Grid([[1, 2], [3, 4]])
value = grid.get(1, 1)  # Returns 4
```

#### Using Utilities

```python
from shared.utils import parse_grid, neighbors

# Parse a grid from a file
grid = parse_grid("input.txt")

# Get neighbors of a cell
neighbor_coords = neighbors(2, 2, include_diagonals=True)
```

---

## Developer Tips

1. **Code Reusability**
    * Place shared utility functions (e.g., parsing, math utilities) in `src/shared/`.

2. **Testing and Debugging**
    * Use `pytest` for unit testing.
    * Use `pdb` for debugging or add print statements for insights.

3. **Performance Optimization**
    * Use `timeit` for benchmarking.
    * Use `cProfile` for profiling bottlenecks.

---

## Automation Worflow

1. **Daily Automation**

  * Set up automation using `cron` or `launchd` (see project docs) to run `download_input.py` and `generate_day.py` daily.

2. **Run Tests and Linting**

  * Automate testing and formatting with uv commands to ensure code quality:

  ```bash
  uv tool run pytest
  uv tool run ruff check .
  uv tool run ruff format .
  ```

3. **GitHub Actions**

  * Consider setting up CI/CD workflows to automate testing and other checks.

---

## Contributing

Feel free to contribute by adding:
* New utilities for solving puzzles.
* Optimizations for existing solutions.
* Tests or enhancements to the automation scripts.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🎄✨ May the stars guide us through the puzzles!
