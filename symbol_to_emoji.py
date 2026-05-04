"""Convert simple text emoticons into emoji characters.

This small helper is intentionally minimal and demonstrates mapping
from ASCII emoticons to emoji. It is a utility for demonstration and
learning purposes.
"""

from typing import List

EMOJI_MAP = {
    ";)": "😉",
    ":)": "🙂",
    ":(": "🙁",
    ":|": "😐",
}


def emojify(tokens: List[str]) -> str:
    """Map a list of tokens to their emoji equivalents where available."""
    return " ".join(EMOJI_MAP.get(t, t) for t in tokens)


def emojify_text(text: str) -> str:
    """Map tokens in a whitespace-separated string to emojis."""
    return " ".join(EMOJI_MAP.get(tok, tok) for tok in text.split())


if __name__ == "__main__":
    print(emojify_text(":) :("))
