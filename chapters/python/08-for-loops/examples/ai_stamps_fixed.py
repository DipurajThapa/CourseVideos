# file: examples/ai_stamps_fixed.py
for stamp in range(1, 11):
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
