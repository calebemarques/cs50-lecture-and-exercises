def main():
    name = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad"]
    for name in name:
        letter = write_letter(name, "Princess Peach")
        print(letter)



def write_letter(receiver,sender):
    return f"""
    +------------------------------------+
    | Dear {receiver},                   |
    |                                    |
    | You are cordinally invited to      |
    | a ball at Peach's Castle this.     |           
    | evening, 7:00 PM.                  |
    |                                    |
    | Best wishes,                       |
    | {sender}                           |
    +------------------------------------+
    """


if __name__ == "__main__":
    main()