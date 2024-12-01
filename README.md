# Advent of Code 2024 - Python Setup

Welcome to my **Advent of Code 2024** repository! This project is designed to streamline solving AoC puzzles using Python, focusing on **code reuse**, **automation**, and **testing**.

---

## Project Structure

```yaml
advent_of_code/
├── .vscode/                  # VS Code settings
├── .env                      # Environment configuration for UV
├── src/                      # Source code for each day
│   ├── day01/
│   │   ├── input.txt         # Puzzle input
│   │   ├── test_input.txt    # Example input for tests
│   │   ├── solution.py       # Solution file
│   │   ├── test_solution.py  # Unit tests
│   └── shared/               # Shared utilities and data classes
├── templates/                # Template for new days
│   ├── day_template/
│   │   ├── input.txt
│   │   ├── test_input.txt
│   │   ├── solution.py
│   │   ├── test_solution.py
├── automation/               # Automation scripts
│   ├── download_input.py     # Downloads input and exercise description
│   ├── generate_day.py       # Generates day structure
├── README.md                 # This file
└── pyproject.toml            # Python project configuration
```

---

## Setup

### 1. **Install Dependencies**

Ensure you have Python installed and **set up a virtual environment [using uv](https://docs.astral.sh/uv/)**. Install the dependencies:

```bash
uv pip install -r requirements.txt
```

### 2. **Configure Advent of Code Session**

Set your Advent of Code session cookie for downloading inputs and descriptions. You can find this in your browser's cookies after logging into the AoC website.

1. Open .env and add:

```bash
AOC_SESSION=your_session_cookie_here
```

2. Alternatively, set it in your shell:

```bash
export AOC_SESSION=your_session_cookie_here
```

### 3, Run Automation Scripts

1. **Generate folder structure for a day in the Advent of Code:**

```bash
uv run python automation/generate_day.py
```

2. **Download input file and challenge description for a day in the Advent of Code:**

```bash
uv run python automation/download_input.py
```


---

## How to Solve a Day

1. **Write your solution**

Implement the solution in `src/dayXX/solution.py`.

2. **Test your code**

Use  `pytest` to run the tests:

```bash
uv tool run pytest
```

3. **Check linting**

Ensure the code adheres to standards:

```bash
uv tool run ruff check .
```

4. **Format the code**

Format the code automatically:

```bash
uv tool run ruff format .
```

5. **Run your solution**

Execute the solution script:

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
  - Use `collections.Counter` for counting occurrences in lists or strings.
- **Prime Numbers:**
  - Use `sympy` or implement Sieve of Eratosthenes for prime number generation.

---

### Libraries

#### Recommended Libraries
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
  * Place shared utility functions (e.g., parsing, math utilities) in src/shared/.

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

* Consider setting up CI/CD workflows to automate testing and deployment.

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