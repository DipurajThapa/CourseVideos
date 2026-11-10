# file: examples/ai/fixed/report_tools.py
"""Rules for the Corner Cafe week report."""
import csv
import json


def load_config(path):
    """Return the settings in a JSON file, or raise ValueError."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"missing settings file {path.name}")
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} is not valid JSON: {error.msg}")


def parse_amount(text):
    """Return a sale amount as a float, or raise ValueError."""
    amount = float(text)
    if amount < 0:
        raise ValueError(f"negative amount {text!r}")
    return amount


def read_sales(path):
    """Return the good sales in a CSV file, and the bad count."""
    sales, bad = [], 0
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            try:
                amount = parse_amount(row["amount"])
            except (ValueError, TypeError):
                bad += 1
            else:
                sales.append((row["item"], amount))
    return sales, bad


def build_week(folder):
    """Return the totals from every CSV file in a folder."""
    week = {"days": {}, "items": {}, "skipped": 0, "total": 0}
    for path in sorted(folder.glob("*.csv")):
        sales, bad = read_sales(path)
        week["skipped"] += bad
        day_total = 0
        for item, amount in sales:
            items = week["items"]
            items[item] = items.get(item, 0) + amount
            day_total += amount
        day = path.stem.split("-")[1].title()
        week["days"][day] = day_total
        week["total"] += day_total
    return week


def money(amount, currency):
    """Return an amount as text, such as USD 12.50."""
    return f"{currency} {amount:.2f}"


def report_lines(week, config):
    """Return the lines of the text report."""
    cur = config["currency"]
    tax = week["total"] * config["tax_rate"]
    with_tax = week["total"] + tax
    lines = ["CORNER CAFE: WEEK REPORT"]
    for day, amount in week["days"].items():
        lines.append(f"{day:<12}{money(amount, cur):>12}")
    lines.append(f"{'Total':<12}{money(week['total'], cur):>12}")
    lines.append(f"{'Tax':<12}{money(tax, cur):>12}")
    lines.append(f"{'With tax':<12}{money(with_tax, cur):>12}")
    lines.append(f"Rows skipped: {week['skipped']}")
    return lines
