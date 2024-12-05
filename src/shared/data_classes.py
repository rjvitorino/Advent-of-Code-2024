from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List, Tuple, Any, Dict


@dataclass
class Point:
    """
    Represents a point in 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    """

    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        """Adds two points together."""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        """Subtracts one point from another."""
        return Point(self.x - other.x, self.y - other.y)


@dataclass
class Grid:
    """
    Represents a 2D grid and provides methods for element access and modification.

    Attributes:
        data (List[List[Any]]): The 2D grid data.
    """

    data: List[List[Any]]

    def __post_init__(self):
        self._rows = len(self.data)
        self._cols = len(self.data[0]) if self._rows > 0 else 0

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def get(self, x: int, y: int) -> str:
        """
        Get the character at the specified position in the grid.

        Args:
            x (int): The column coordinate
            y (int): The row coordinate

        Returns:
            str: The character at the specified position

        Raises:
            IndexError: If the position is outside the grid boundaries
        """
        if not self.is_valid_position(x, y):
            raise IndexError(f"Position ({x}, {y}) is outside grid boundaries")
        return self.data[y][x]

    def get_grid_dimensions(self) -> Tuple[int, int]:
        """
        Get the dimensions of the grid.

        Returns:
            Tuple[int, int]: A tuple containing (rows, columns)
        """
        return self._rows, self._cols

    def is_valid_position(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the grid boundaries.

        Args:
            x (int): The column coordinate to check
            y (int): The row coordinate to check

        Returns:
            bool: True if the position is within bounds (0 <= x < cols and 0 <= y < rows),
                False otherwise

        Example:
            >>> grid.is_valid_position(0, 0)  # Check top-left corner
            True
            >>> grid.is_valid_position(-1, 5) # Check invalid position
            False
        """
        return 0 <= x < self._cols and 0 <= y < self._rows

    def set(self, x: int, y: int, value: Any) -> None:
        """
        Sets a value in the grid at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (Any): The value to set.
        """
        if not self.is_valid_position(x, y):
            raise ValueError(f"Invalid position: ({x}, {y})")
        self.data[y][x] = value

    def check_direction(
        self, start_x: int, start_y: int, dx: int, dy: int, word: str
    ) -> bool:
        """
        Check if a word exists in the grid starting from the given position in the specified direction.

        Args:
            start_x (int): Starting column coordinate
            start_y (int): Starting row coordinate
            dx (int): Direction vector for columns (-1, 0, or 1)
            dy (int): Direction vector for rows (-1, 0, or 1)
            word (str): The word to search for

        Returns:
            bool: True if the word is found in the specified direction from the starting position,
                False otherwise

        Example:
            >>> grid.check_direction(0, 0, 1, 0, "HELLO")  # Check horizontally right from (0,0)
            True
            >>> grid.check_direction(2, 2, -1, 1, "WORLD")  # Check diagonally up-left from (2,2)
            False

        Notes:
            - Direction vectors (dx, dy) should be in range [-1, 0, 1]
        """
        word_length = len(word)
        # Quick boundary check before attempting full word match
        end_x = start_x + (word_length - 1) * dx
        end_y = start_y + (word_length - 1) * dy

        if not self.is_valid_position(end_x, end_y):
            return False

        # Check each character in the word
        for i, char in enumerate(word):
            curr_x = start_x + dx * i
            curr_y = start_y + dy * i
            if self.data[curr_y][curr_x] != char:
                return False
        return True


@dataclass
class Range:
    """
    Represents a numerical range with utilities for overlap and containment.

    Attributes:
        start (int): The start of the range.
        end (int): The end of the range.
    """

    start: int
    end: int

    def overlaps(self, other: "Range") -> bool:
        """
        Checks if this range overlaps with another range.

        Args:
            other (Range): The other range.

        Returns:
            bool: True if the ranges overlap, False otherwise.
        """
        return self.start <= other.end and other.start <= self.end

    def contains(self, value: int) -> bool:
        """
        Checks if a value lies within this range.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is in the range, False otherwise.
        """
        return self.start <= value <= self.end


@dataclass
class TopologicalSorter:
    """
    A utility class for performing topological sorting on a directed acyclic graph (DAG).

    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph, where
                                      each key is a node, and its value is a list of nodes
                                      it points to (its neighbors).
        in_degree (Dict[int, int]): Tracks the in-degree (number of incoming edges) for each node.
                                    Nodes with an in-degree of 0 have no dependencies.
    """

    graph: Dict[int, List[int]] = None
    in_degree: Dict[int, int] = None

    def __post_init__(self):
        """
        Initializes the graph and in-degree map as default dictionaries. The graph uses a list
        for neighbors, and the in-degree map tracks the number of incoming edges for each node.
        """
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, x: int, y: int) -> None:
        """
        Adds a directed edge from node `x` to node `y` in the graph.

        This represents a dependency where `x` must come before `y` in the sorted order.

        Args:
            x (int): The source node.
            y (int): The target node.
        """
        self.graph[x].append(y)  # Add `y` as a neighbor of `x`
        self.in_degree[y] += 1  # Increment the in-degree of `y`
        self.in_degree.setdefault(x, 0)  # Ensure `x` is in the in-degree map

    def sort(self, nodes: List[int]) -> List[int]:
        """
        Performs topological sorting on the graph to determine a valid ordering of nodes.

        The sorting respects all dependencies, ensuring that for every edge `x -> y`,
        node `x` appears before node `y` in the output.

        Args:
            nodes (List[int]): The list of all nodes to sort. Nodes not in this list are ignored.

        Returns:
            List[int]: The nodes sorted in topological order. If there are multiple valid orders,
                       the result will be deterministic due to sorting.

        Raises:
            ValueError: If the graph contains a cycle, making topological sorting impossible.

        Algorithm:
        - Build a queue of nodes with in-degree 0 (nodes with no dependencies).
        - Iteratively process each node from the queue:
            - Add it to the sorted result.
            - Decrement the in-degree of its neighbors.
            - Add neighbors with in-degree 0 to the queue.
        - If the total processed nodes is less than the total input nodes, a cycle exists.
        """
        # Find all nodes with zero in-degree and initialize the processing queue
        queue = deque(sorted(node for node in nodes if self.in_degree[node] == 0))
        sorted_nodes = []  # To store the topological order

        while queue:
            # Process the next node in the queue
            node = queue.popleft()
            sorted_nodes.append(node)

            # Decrease the in-degree of all neighbors
            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                # If a neighbor now has zero in-degree, add it to the queue
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    queue = deque(sorted(queue))  # Maintain deterministic order

        # If not all nodes are in the sorted list, a cycle exists in the graph
        if len(sorted_nodes) != len(nodes):
            raise ValueError("Cycle detected in the graph")

        return sorted_nodes
