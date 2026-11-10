# file: examples/ai/write_compare.py
def mine(text):
    amount = float(text)
    if amount < 0:
        raise ValueError(f"negative amount {text!r}")
    return amount


def ai_version(text):
    return float(text.strip())


for text in ["3.50", " 2.75", "-2.00"]:
    print(f"{text!r} AI:", ai_version(text))
    try:
        print(f"{text!r} Asha:", mine(text))
    except ValueError:
        print(f"{text!r} Asha: refused")
