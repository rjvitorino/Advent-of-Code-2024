# Advent of Code 2024 - Python Setup

Welcome to my Advent of Code 2024 repository! This project is designed to streamline solving AoC puzzles using Python, with a focus on code reuse, automation, and testing.

---

## Project Structure

```yaml
advent_of_code/ 
├── .vscode/ # VS Code settings 
├── .env # Environment configuration for UV 
├── src/ # Source code for each day 
│ ├── day01/ 
│ │ ├── input.txt # Puzzle input 
│ │ ├── test_input.txt # Example input for tests 
│ │ ├── solution.py # Solution file 
│ │ ├── test_solution.py # Unit tests 
│ └── shared/ # Shared utilities and data classes 
├── templates/ # Template for new days 
│ ├── day_template/ 
│ │ ├── input.txt 
│ │ ├── test_input.txt 
│ │ ├── solution.py 
│ │ ├── test_solution.py 
├── automation/ # Automation scripts 
│ ├── download_input.py # Downloads input and exercise description 
│ ├── generate_day.py # Generates day structure 
├── README.md # This file 
└── pyproject.toml # Python project configuration
```

---

## Setup

1. **Install Dependencies**
   Ensure you have Python installed. Use the following command to set up the project dependencies:

```bash
pip install -r requirements.txt
```

2. **Configure AoC Session**
Edit `automation/download_input.py` and replace `{YOUR_SESSION_COOKIE}` with your Advent of Code session cookie. You can find this in your browser's cookies after logging into the AoC website.

3. **Run Automation**
- To download input for a specific day:
  ```bash
  python automation/download_input.py
  ```
- To set up a new day:
  ```bash
  python automation/generate_day.py
  ```

---

## How to Solve a Day

1. Write your solution in `src/dayXX/solution.py`.
2. Test your solution using `pytest`:

```bash
pytest src/dayXX/test_solution.py
```

3. Run your solution:

```bash
python src/dayXX/solution.py
```

---

## Useful Algorithms and Tools

### Data Structures
- `collections.deque`: For efficient appending/popping.
- `heapq`: Implements priority queues.
- `itertools`: For permutations, combinations, etc.

### Algorithms
- **Graph Traversals**: BFS and DFS for pathfinding.
- **Dynamic Programming**: Ideal for optimization problems.
- **String Matching**: Use regular expressions (`re`).

### Libraries
- `numpy`: For numerical and array manipulations.
- `networkx`: For graph algorithms.
- `sympy`: For mathematical operations (e.g., primes).

---

## Developer Tips

1. **Reusability**: Place shared utilities in `src/shared/`.
2. **Unit Testing**: Test each part of your solution in `test_solution.py`.
3. **Performance**: Use `timeit` for benchmarking and `cProfile` for profiling.

Happy coding!