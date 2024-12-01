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

    def get(self, x: int, y: int, default: Optional[Any] = None) -> Optional[Any]:
        """
        Safely retrieves an element from the grid.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            default (Optional[Any]): Value to return if coordinates are out of bounds.

        Returns:
            Optional[Any]: The value at the specified coordinates, or the default.
        """
        if 0 <= y < len(self.data) and 0 <= x < len(self.data[0]):
            return self.data[y][x]
        return default

    def set(self, x: int, y: int, value: Any) -> None:
        """
        Sets a value in the grid at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (Any): The value to set.
        """
        if 0 <= y < len(self.data) and 0 <= x < len(self.data[0]):
            self.data[y][x] = value


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
