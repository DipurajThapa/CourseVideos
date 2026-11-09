# file: examples/ai_stamps_mine.py
stamp = 1
while stamp <= 10:
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
    stamp += 1
