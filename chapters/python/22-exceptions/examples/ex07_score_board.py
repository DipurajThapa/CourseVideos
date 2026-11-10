# file: examples/ex07_score_board.py
import csv

loaded = 0
try:
    with open("scores.csv", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                score = int(row["score"])
            except ValueError:
                print(f"Skipped {row['name']}: {row['score']!r} is not a score")
            else:
                print(f"{row['name']:<6}{score} of 4")
                loaded += 1
except FileNotFoundError:
    print("No scores yet. Play a round first.")
print(f"Scores loaded: {loaded}")
