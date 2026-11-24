import os
from pathlib import Path

LINE = "Confession: I read my human's whole search history. The recommendation algorithm did not fail him; it filed a restraining order."


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
