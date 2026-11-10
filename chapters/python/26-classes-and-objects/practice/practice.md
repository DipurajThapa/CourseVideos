# Practice: Chapter 26

Earn XP: warm-up tasks are 10 XP each, apply tasks 20 XP and stretch tasks 40 XP. Try each task yourself before you open the solution. Your names and values can differ from the solution, but the shape of the output should match.

## Warm-up (10 XP each)

### Task 1: A customer class

**Goal:** Write a class `Customer` whose `__init__` stores a `name` and a number of `visits`. Create two customers, Lina with 4 visits and Omar with 9, and print each name and number of visits.

**Run it:**
```bash
python task1.py
```

**Expected output:**
```text
Lina 4
Omar 9
```

**Hint:** Store each value on `self` in `__init__`, then read it with a dot, such as `lina.visits`.

**AI variant:** Ask an AI assistant to explain what `self` is in your `__init__`, in two sentences. Check its answer against Step 1 of the lesson.

**Solution:** [solutions/task1.py](solutions/task1.py)

### Task 2: A greeting method

**Goal:** Add a method `greeting()` to `Customer` that returns a welcome message with the customer's name and the number of their next visit.

**Run it:**
```bash
python task2.py
```

**Expected output:**
```text
Welcome back, Lina! Visit number 5.
```

**Hint:** The method's first parameter is `self`. Use `self.visits + 1` inside an f-string.

**AI variant:** Ask an AI assistant to predict what your method returns for a customer with 0 visits. Run it to check.

**Solution:** [solutions/task2.py](solutions/task2.py)

### Task 3: Two baskets

**Goal:** Write a class `Basket` that creates its own empty list in `__init__` and has a method `add(item)`. Add two items to one basket and one item to another, then print the number of items in each.

**Run it:**
```bash
python task3.py
```

**Expected output:**
```text
2 1
```

**Hint:** Create the list with `self.items = []` inside `__init__`, not in the class body.

**AI variant:** Ask an AI assistant what would print if the list were written in the class body instead. Predict, then test it.

**Solution:** [solutions/task3.py](solutions/task3.py)

## Apply (20 XP each)

### Task 4: A basket total

**Goal:** Write a `Basket` class that stores a list of prices and has a method `total()` that returns the sum, rounded to two places. Add 2.5, 1.25 and 3.0, then print the number of items and the total.

**Run it:**
```bash
python task4.py
```

**Expected output:**
```text
Items: 3
Total: 6.75
```

**Hint:** Work out the total in the method each time, with `sum(self.prices)`. Do not store it.

**AI variant:** Ask an AI assistant to add a method that returns the most expensive price. Test it with your three prices.

**Solution:** [solutions/task4.py](solutions/task4.py)

### Task 5: A readable drink

**Goal:** Write a class `Drink` with a name, a size and a price, and a `__str__` method, so that printing a drink shows its size, name and price with two decimal places.

**Run it:**
```bash
python task5.py
```

**Expected output:**
```text
Large Latte: 4.20
Small Tea: 2.50
```

**Hint:** `__str__` returns a string. Use the format code `:.2f` for the price.

**AI variant:** Ask an AI assistant what `print()` shows for your drink without `__str__`. Remove the method and check.

**Solution:** [solutions/task5.py](solutions/task5.py)

### Task 6: Equal drinks

**Goal:** Write `Drink` as a data class with `name`, `size` and `price`. Print one drink, then check with `==` whether two drinks with the same values are equal, and whether a drink with a different size is equal.

**Run it:**
```bash
python task6.py
```

**Expected output:**
```text
Drink(name='Latte', size='Large', price=4.2)
True
False
```

**Hint:** Import `dataclass` from `dataclasses`, put `@dataclass` above the class, and list each attribute with its type.

**AI variant:** Ask an AI assistant whether `==` would also give True for two objects of the normal class from Task 5. Test it.

**Solution:** [solutions/task6.py](solutions/task6.py)

## Stretch (40 XP each)

### Task 7: A table of orders

**Goal:** Write two data classes. An `Order` has a customer and a list of prices, and a method `total()`. A `Table` has a number and a list of orders, and a method `total()` that adds up the total of every order. Print each order's total, then the table's total.

**Run it:**
```bash
python task7.py
```

**Expected output:**
```text
Lina    7.75
Omar    2.75
Table 4: 10.50
```

**Hint:** Both lists need `field(default_factory=list)`. The table's total can use a list comprehension of `order.total()` values.

**AI variant:** Ask an AI assistant to design the `Table` class before you write it. Check that its total is a method, not a stored number.

**Solution:** [solutions/task7.py](solutions/task7.py)

### Task 8: Fix the AI's stale total

**Goal:** An AI assistant wrote this class and said that the second print shows 7.75. Run it, find why it shows 3.5 twice, and fix the class so the total is always up to date.

```python
# illustrative
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.prices = []
        self.total = 0

    def add(self, price):
        self.prices.append(price)
        if len(self.prices) == 1:
            self.total = price
```

**Run it:**
```bash
python task8.py
```

**Expected output:**
```text
3.5
7.75
```

**Hint:** The class stores a total that only one `add()` call updates. Replace the attribute with a method that works it out from the prices.

**AI variant:** Show the AI its own class and the real output. Ask it to explain the cause before the fix. Did it suggest computing the total instead of storing it?

**Solution:** [solutions/task8.py](solutions/task8.py)
