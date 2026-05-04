"""Convert numeric strings into spoken word sequences.

Example:
    number_to_words('123') -> 'one two three'
"""

DIGIT_WORDS = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def number_to_words(num_str: str) -> str:
    """Return the spoken words for each digit in `num_str`.

    Non-digit characters are represented by '!' in the output.
    """
    return " ".join(DIGIT_WORDS.get(ch, "!") for ch in str(num_str).strip())


if __name__ == "__main__":
    import sys

    s = sys.argv[1] if len(sys.argv) > 1 else "123"
    print(number_to_words(s))
