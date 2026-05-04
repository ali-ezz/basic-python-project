"""Dice rolling utility.

Provides a small `Dice` class that can roll one or more six-sided dice.
"""

from __future__ import annotations

import random
from typing import Tuple


class Dice:
    """Simple six-sided dice roller."""

    def roll(self, count: int = 2) -> Tuple[int, ...]:
        """Roll `count` six-sided dice and return a tuple of results."""
        return tuple(random.randint(1, 6) for _ in range(count))


if __name__ == "__main__":
    print(Dice().roll())
