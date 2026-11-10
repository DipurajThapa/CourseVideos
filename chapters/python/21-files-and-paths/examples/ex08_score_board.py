# file: examples/ex08_score_board.py
import csv

new_name = "Lina"
new_score = 4

with open("scores.csv", "a", newline="", encoding="utf-8") as file:
    csv.writer(file).writerow([new_name, new_score])

best_name, best_score = "", -1
with open("scores.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        score = int(row["score"])
        print(f"{row['name']:<6}{score} of 4")
        if score > best_score:
            best_name, best_score = row["name"], score

print(f"Best: {best_name} with {best_score} of 4")
