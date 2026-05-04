"""Utilities for finding the maximum value in a list."""

from __future__ import annotations


def find_max(numbers: list) -> int:
    """Return the maximum value from a non-empty list of numbers.

    Raises `ValueError` when `numbers` is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


if __name__ == "__main__":
    print(find_max([3, 1, 4, 2]))