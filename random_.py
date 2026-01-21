import random


number = random.randint(1, 10)  # returns a random integer between 1 and 10 (inclusive)
print(f"Random integer between 1 and 10: {number}")

cards = ["queen", "king", "ace"]
random.shuffle(cards)  # shuffles the list in place
print(f"Shuffled cards: {cards}")
for card in cards :
    print(f"Card: {card}")