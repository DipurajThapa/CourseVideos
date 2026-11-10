# file: examples/ai/flawed/test_quiz_logic.py
"""Tests for the staff quiz rules, written before the code."""
from quiz_logic import check_answer, percentage, grade, result_line


def test_exact_answer():
    assert check_answer("carrot", "carrot")


def test_capitals_and_spaces():
    assert check_answer("  Carrot ", "carrot")


def test_wrong_answer():
    assert not check_answer("lemon", "carrot")


def test_blank_answer():
    assert not check_answer("", "carrot")


def test_three_of_four():
    assert percentage(3, 4) == 75


def test_percentage_rounds():
    assert percentage(2, 3) == 67


def test_grade_boundaries():
    assert grade(75) == "Ready"
    assert grade(74) == "Almost"
    assert grade(50) == "Almost"
    assert grade(49) == "Practise again"


def test_result_line():
    assert result_line(3, 4) == "Score: 3/4 (75%) Ready"
