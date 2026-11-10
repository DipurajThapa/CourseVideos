# file: examples/ai_save_flawed.py
from pathlib import Path


def save_score(path, name, score):
    with open(path, "w", encoding="utf-8") as file:
        file.write("name,score\n")
        file.write(f"{name},{score}\n")


save_score("week.csv", "Asha", 4)
save_score("week.csv", "Omar", 3)
print(Path("week.csv").read_text(encoding="utf-8"), end="")
