# file: examples/step2/config_check.py
from pathlib import Path
from report_tools import load_config

config = load_config(Path("config.json"))
print(config)
print("Currency:", config["currency"])
print("Tax rate:", config["tax_rate"])
