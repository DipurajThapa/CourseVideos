# file: examples/ai_own_boxes.py
def boxes_needed(biscuits, per_box=12):
    """Return how many boxes to order."""
    return biscuits // per_box + 1

print(boxes_needed(40))
