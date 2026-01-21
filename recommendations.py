def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty.")
        return print("END")

    players = input("Multiplayer or Single-player ?")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players.")
        return print("END")

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif players == "Single-player":
        recommend("klondike")

    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    elif difficulty == "Casual" and players == "Single-player":
        recommend("clock")


def recommend(game):
    print(f"I recommend you play {game}!")


main()
