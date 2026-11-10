# file: examples/ai_boxes_flawed.py
def boxes_needed(biscuits, per_box=12):
    """Return how many boxes to order, rounded up."""
    return round(biscuits / per_box)

print(boxes_needed(40))
