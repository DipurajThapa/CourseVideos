# file: examples/ai_compare_boxes.py
import math

for biscuits in [40, 24]:
    mine = biscuits // 12 + 1
    with_ceil = math.ceil(biscuits / 12)
    print(biscuits, "biscuits:", mine, with_ceil)
