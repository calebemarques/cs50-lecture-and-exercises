import random  # Import the random library to enable random selection of houses

class Hat:
    """
    A class representing the Sorting Hat from Harry Potter.
    This class simulates the process of sorting students into Hogwarts houses.
    It initializes with a list of houses and provides a method to randomly assign a house to a student.
    """

    """def __init__(self):  # Initialize the Hat instance
        print("The sorting hat is ready to sort students into houses.")  # Print a message indicating the hat is ready
        
    """
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]  # Define the list of available Hogwarts houses
    @classmethod
    def sort(cls, name):  # Instance method to sort a student into a house (note: @classmethod decorator removed as it's not needed for instance method)
        """
        Sorts a student into a random Hogwarts house.

        Parameters:
        name (str): The name of the student to be sorted.

        Returns:
        None: Prints the sorting result to the console.
        """
        house = random.choice(cls.houses)  # Randomly select a house from the list of houses
        print(f"Sorting hat is placing {name} into a {house}.")  # Print the sorting result using the selected house


# Call the sort method on the hat instance with "Harry" as the student name

Hat.sort(input("Name: "))
