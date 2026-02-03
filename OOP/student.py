#OOP = Object Oriented Programming = create your own data types

# Define the Student class to represent a student with name and house
class Student:
    # Constructor method to initialize a Student object
    # Parameters: name (string), house (string)
    def __init__(self, name, house, patronus):
        # Validate that name is provided
        if not name:
            raise ValueError("Missing name")
        # Validate that house is one of the valid Hogwarts houses
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house")
        # Assign the validated name and house to the object
        self.name = name
        self.house = house
        self.patronus = patronus
    """
    __str__ = string representation of the object
    when we print the object, this method is called
    so the string returned by the object is printed

    __str__ method should return a string

    __init__ method is called when we create an object


    """
      # Method to return a string representation of the Student object
    def __str__(self):
        # Return a formatted string with the student's name and hous4
        return f"{self.name} from {self.house} and their patronus is {self.patronus}." 
       

  
       

# Main function to run the program
def  main():
    # Get a student object from user input
    student = get_students()
    # Print the student object (which calls __str__)
    print(student)


# Function to get student details from user input
def get_students():
    # Prompt user for name
    name = input("Name: ")
    # Prompt user for house
    house = input("House: ")
    # Prompt user for patronus
    patronus = input("Patronus: ")
    return Student(name,house,patronus)

#class = create your own data type

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
