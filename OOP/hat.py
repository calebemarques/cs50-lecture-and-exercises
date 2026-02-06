import random # import random library to randomize the choice
class Hat:
    def __init__(self): # initialize the class
        print("The sorting hat is ready to sort students into houses.")
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    def sort(self, name): # sort the house
        house = random.choice(self.houses)
        print(f"Sorting hat is placing {name} into a {random.choice(self.houses)}.")

hat = Hat()
hat.sort("Harry") # take the name for input and sort for a house in method sort() // 
