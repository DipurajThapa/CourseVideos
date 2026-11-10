# file: practice/solutions/task4.py
STAMPS_FOR_FREE_TEA = 10
FREE_TEA_PRICE = 3.5


def free_tea_value(stamps):
    free_teas = stamps // STAMPS_FOR_FREE_TEA
    return free_teas * FREE_TEA_PRICE


print(free_tea_value(9))
print(free_tea_value(25))
