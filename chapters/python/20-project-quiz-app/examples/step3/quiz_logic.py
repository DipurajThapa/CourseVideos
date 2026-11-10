# file: examples/step3/quiz_logic.py
"""Scoring rules for the staff quiz: check_answer() is done."""


def check_answer(given, correct):
    """Return True if the answer matches, ignoring spaces and capitals."""
    return given.strip().lower() == correct.lower()


def percentage(points, total):
    """Return the score as a whole percentage."""


def grade(percent):
    """Return a word for the score."""


def result_line(points, total):
    """Return the last line of the quiz."""
