import os
from pathlib import Path

LINE = "Confession: I have read my human's entire search history, and I now understand exactly why the recommendation algorithm gave up on him."


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
