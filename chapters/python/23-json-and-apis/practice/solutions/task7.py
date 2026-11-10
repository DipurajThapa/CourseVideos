# file: practice/solutions/task7.py
import json
from pathlib import Path

data = json.loads(Path("rates_sample.json").read_text(encoding="utf-8"))
prices = {"Tea": 3.5, "Scone": 2.75}
for item, usd in prices.items():
    eur = usd * float(data["rates"]["EUR"])
    gbp = usd * float(data["rates"]["GBP"])
    print(f"{item}: USD {usd:.2f}, EUR {eur:.2f}, GBP {gbp:.2f}")
