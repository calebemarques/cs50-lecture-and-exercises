def main():
    history = []

    while True:
        action = input("Action: ") 

        if action == "Undo":
            undone = history.pop()
            print(f"Undid action: {undone}")
        elif action == "Restart":
            history.clear()
            print("History cleared.")
        else:
            history.append(action)
        print(history)




main()