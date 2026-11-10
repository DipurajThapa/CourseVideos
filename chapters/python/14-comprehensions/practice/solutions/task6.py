# file: practice/solutions/task6.py
tips = [2.0, 0, 1.5, 0, 3.0]
real_tips = []
for tip in tips:
    if tip > 0:
        real_tips.append(tip)
print(real_tips)
short_way = [tip for tip in tips if tip > 0]
print(short_way)
print("Same:", real_tips == short_way)
print("Total tips:", sum(short_way))
