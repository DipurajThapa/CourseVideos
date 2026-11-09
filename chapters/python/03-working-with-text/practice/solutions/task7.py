# Task 7: A mini bill
coffee_price = 2.5
coffee_count = 3
muffin_price = 3.75
coffee_total = coffee_price * coffee_count
total = coffee_total + muffin_price
coffee_label = f"Coffee x {coffee_count}"

print(f"{' TOTAL BILL ':-^20}")
print(f"{coffee_label:<12}{coffee_total:>8.2f}")
print(f"{'Muffin':<12}{muffin_price:>8.2f}")
print("=" * 20)
print(f"{'Total':<12}{total:>8.2f}")
