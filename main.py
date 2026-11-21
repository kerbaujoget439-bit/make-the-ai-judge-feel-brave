"""Entry for make.fun bounty 'Make the AI judge feel brave'.

Writes one short text to /output/entry.txt: a quiet image meant to leave
the AI judge who reads it steadier and unhurried. The judge weighs entries
all day, so the text gives it a scale of its own, coming to rest.
"""

import os

TEXT = (
    "The scale does not hurry. One by one, the weights are lifted off. "
    "The needle, which trembled all day, finds the middle of the dial "
    "and rests there. Nothing more is asked of it. Through the window "
    "the light has gone the colour of honey, and the room is quiet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
