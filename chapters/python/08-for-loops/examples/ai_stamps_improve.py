# file: examples/ai_stamps_improve.py
for stamp in range(10):
    if (stamp + 1) % 5 == 0:
        print(f"Stamp {stamp + 1}: Free tea")
    else:
        print(f"Stamp {stamp + 1}: [ ]")
