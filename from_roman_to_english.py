"""Utilities for converting Roman numerals to integers.

This module exposes a single function `roman_to_int` and a small
command-line entrypoint for quick manual use.
"""

from __future__ import annotations


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer.

    Handles standard subtractive notation (IV, IX, XL, XC, CD, CM).
    Non-Roman characters are ignored (treated as 0).
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.strip().upper()):
        val = values.get(ch, 0)
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


if __name__ == "__main__":
    import sys

    arg = sys.argv[1] if len(sys.argv) > 1 else "XII"
    print(roman_to_int(arg))