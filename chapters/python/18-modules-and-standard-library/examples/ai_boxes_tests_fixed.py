# file: examples/ai_boxes_tests_fixed.py
import math

def boxes_needed(biscuits, per_box=12):
    return math.ceil(biscuits / per_box)

cases = {40: 4, 24: 2, 1: 1, 0: 0}
for biscuits, expected in cases.items():
    result = boxes_needed(biscuits)
    check = "pass" if result == expected else "FAIL"
    print(biscuits, "->", result, check)
