import random
cards = ["jack","queen","king"]

def main():
    random.seed(0)
    print(random.choice(cards))
    print(random.sample(cards, k=3))
    print(random.choices(cards, weights=[50,50,50], k=2))
main()
