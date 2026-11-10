# file: practice/solutions/task8.py
def log_event(text):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")


log_event("Tea urn cleaned")
log_event("Closed at 18:00")
with open("log.txt", encoding="utf-8") as file:
    print(file.read().strip())
