# file: examples/ai_save_fixed.py
import csv
from pathlib import Path


def save_score(path, name, score):
    new_file = not Path(path).exists()
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["name", "score"])
        writer.writerow([name, score])


save_score("week.csv", "Asha", 4)
save_score("week.csv", "Omar", 3)
print(Path("week.csv").read_text(encoding="utf-8"), end="")
