# file: examples/ai/write_compare.py
def mine(given, correct):
    return given.strip().lower() == correct.lower()


def ai_version(given, correct):
    return given.lower().strip() == correct.lower()


for answer in ["carrot", "  Carrot ", "lemon", ""]:
    print(f"{answer!r:12}", mine(answer, "carrot"), ai_version(answer, "carrot"))
