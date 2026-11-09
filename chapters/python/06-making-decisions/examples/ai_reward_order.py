# file: examples/ai_reward_order.py
to_pay = 60.0
if to_pay >= 15:
    print("Reward: a free biscuit")
elif to_pay >= 50:
    print("Reward: a free cake")
else:
    print("Reward: none this time")
