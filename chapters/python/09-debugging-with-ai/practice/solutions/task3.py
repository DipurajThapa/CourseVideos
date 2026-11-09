# file: practice/solutions/task3.py
stamps = 0
for cup in range(1, 5):
    stamps = stamps + 2
    print(f"DEBUG cup={cup} stamps={stamps}")
print(f"Stamps: {stamps}")
