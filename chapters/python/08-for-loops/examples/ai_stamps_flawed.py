# file: examples/ai_stamps_flawed.py
for stamp in range(1, 10):
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
