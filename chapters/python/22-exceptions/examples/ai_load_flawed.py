# file: examples/ai_load_flawed.py
import csv


def load_scores(path):
    scores = []
    try:
        with open(path, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                scores.append((row["name"], int(row["score"])))
    except:
        pass
    return scores


if __name__ == "__main__":
    print(load_scores("case_damaged.csv"))
