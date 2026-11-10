# file: examples/apptest/quiz_logic.py
"""Scoring rules for the staff quiz."""


def check_answer(given, correct):
    """Return True if the answer matches, ignoring spaces and capitals."""
    return given.strip().lower() == correct.lower()


def percentage(points, total):
    """Return the score as a whole percentage."""
    return round(points / total * 100)


def grade(percent):
    """Return a word for the score."""
    if percent >= 75:
        return "Ready"
    elif percent >= 50:
        return "Almost"
    else:
        return "Practise again"


def result_line(points, total):
    """Return the last line of the quiz."""
    percent = percentage(points, total)
    return f"Score: {points}/{total} ({percent}%) {grade(percent)}"
