from dataclasses import dataclass
from typing import Callable, List, Tuple, Optional, Any


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
