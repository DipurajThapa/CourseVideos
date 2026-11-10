# file: examples/ai_load_final.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    scores.append((row["name"], int(row["score"])))
                except (ValueError, TypeError):
                    print(f"Skipped {row['name']}: not a score")
    except FileNotFoundError:
        print(f"{path} not found: starting with no scores")
    return scores
