# file: practice/solutions/task7.py
import json
from pathlib import Path


def load_titles(path):
    """Return the saved titles; a missing or empty file means none."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    if not text.strip():
        return []
    return [row["title"] for row in json.loads(text)]


Path("empty.json").write_text("", encoding="utf-8")
Path("two.json").write_text('[{"title": "Tea"}, {"title": "Cake"}]',
                            encoding="utf-8")
print(load_titles(Path("missing.json")))
print(load_titles(Path("empty.json")))
print(load_titles(Path("two.json")))
