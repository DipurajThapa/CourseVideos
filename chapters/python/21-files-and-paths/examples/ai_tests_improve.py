# file: examples/ai_tests_improve.py
import csv
from pathlib import Path


def save_score(path, name, score):
    Path(path).parent.mkdir(exist_ok=True)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "score"])
        writer.writerow([name, score])


def check(label, path, expected):
    text = Path(path).read_text(encoding="utf-8")
    print(label, "pass" if text == expected else "FAIL")


save_score("new.csv", "Asha", 4)
check("1 New file:", "new.csv", "name,score\nAsha,4\n")
save_score("two.csv", "Asha", 4)
save_score("two.csv", "Omar", 3)
check("2 Two saves:", "two.csv", "name,score\nAsha,4\nOmar,3\n")
save_score("case_old.csv", "Lina", 2)
check("3 Old file:", "case_old.csv", "name,score\nAsha,4\nLina,2\n")
save_score("data/week.csv", "Asha", 4)
check("4 In a folder:", "data/week.csv", "name,score\nAsha,4\n")
