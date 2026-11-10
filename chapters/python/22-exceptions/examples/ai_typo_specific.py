# file: examples/ai_typo_specific.py
import csv


def load_scores(path):
    scores = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                scores.append((row["name"], int(row["scor"])))
            except (ValueError, TypeError):
                print(f"Skipped {row['name']}: not a score")
    return scores


print(load_scores("case_normal.csv"))
