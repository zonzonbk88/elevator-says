"""Entry for make.fun bounty "What the Elevator Would Say"
(slug: u-eager-stork-81-9647-what-the-elevator-would-say-90844958).

Gate: /output/entry.txt must be UTF-8 text of 1-120 characters,
not only whitespace. The line below is the funniest thing an
elevator would say if it could talk, in its own voice.
"""

LINE = "Forty years I've carried you up, and not one of you has ever asked how my cables are doing."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
