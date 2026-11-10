# file: examples/ai_boxes_noimport.py
def boxes_needed(biscuits, per_box=12):
    """Return how many boxes to order, rounded up."""
    return math.ceil(biscuits / per_box)

print(boxes_needed(40))
