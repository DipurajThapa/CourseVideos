# file: examples/ai_mine.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    scores.append((row["name"], int(row["score"])))
                except ValueError:
                    print(f"Skipped {row['name']}: not a score")
    except FileNotFoundError:
        print(f"{path} not found: starting with no scores")
    return scores


print(load_scores("case_damaged.csv"))
print(load_scores("missing.csv"))
