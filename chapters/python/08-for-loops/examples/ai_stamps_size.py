# file: examples/ai_stamps_size.py
size = input("Stamps on the card: ")
for stamp in range(1, size + 1):
    if stamp % 5 == 0:
        print(f"Stamp {stamp}: FREE TEA")
    else:
        print(f"Stamp {stamp}: [ ]")
