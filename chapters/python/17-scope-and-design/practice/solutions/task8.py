# file: practice/solutions/task8.py
def add_stamp(card):
    card.append("stamp")
    return card

lina_card = add_stamp([])
lina_card = add_stamp(lina_card)
omar_card = add_stamp([])
print("Lina stamps:", len(lina_card))
print("Omar stamps:", len(omar_card))
