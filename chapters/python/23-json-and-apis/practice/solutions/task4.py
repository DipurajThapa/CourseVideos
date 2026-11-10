# file: practice/solutions/task4.py
import json
from pathlib import Path

order = {"table": 4, "items": ["tea", "scone"], "paid": False}
Path("order.json").write_text(json.dumps(order, indent=2), encoding="utf-8")
print(Path("order.json").read_text(encoding="utf-8"))
