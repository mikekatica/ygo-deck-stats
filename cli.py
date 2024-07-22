from models import deck

mydeck = deck.Deck.from_file("./deck_example.txt")
print(mydeck)
print([str(i) for i in sorted(mydeck.combos, key=lambda x: x.weight, reverse=True)])
