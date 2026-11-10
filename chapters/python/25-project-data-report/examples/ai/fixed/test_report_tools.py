# file: examples/ai/fixed/test_report_tools.py
from pathlib import Path

import pytest

from report_tools import build_week, money, parse_amount


def test_amount_from_text():
    assert parse_amount("3.50") == 3.5


def test_amount_refuses_words():
    with pytest.raises(ValueError):
        parse_amount("four")


def test_amount_refuses_negative():
    with pytest.raises(ValueError):
        parse_amount("-2.00")


def test_money_has_two_decimals():
    assert money(4, "USD") == "USD 4.00"


def test_week_total_and_skipped():
    week = build_week(Path("data"))
    assert week["total"] == 37.25
    assert week["skipped"] == 2


def test_days_are_not_rounded():
    week = build_week(Path("data"))
    assert week["days"]["Tuesday"] == 11.25
