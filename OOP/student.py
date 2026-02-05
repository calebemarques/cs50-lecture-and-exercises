#OOP = Object Oriented Programming = create your own data types

# Define the Student class to represent a student with name and house
from re import match
from unittest import case


class Student:
    # Constructor method to initialize a Student object
    # Parameters: name (string), house (string)
    def __init__(self, name, house):
        # Validate that name is provided
        """  if not name:
            raise ValueError("Missing name")""" #unnecessary because of setter method
        # Validate that house is one of the valid Hogwarts houses// unnecessary because of setter method
        """ if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house") """
        # Assign the validated name and house to the object
        self.name = name
        self.house = house
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
        return f"{self.name} from {self.house}" 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    # Getter method for the house attribute
    @property #@property = decorator = modifies the behavior of the method below it
    def house(self):
        return self._house # return the value of the private attribute _house// _ = convention to indicate private attribute
    # Setter method for the house attribute
    @house.setter #@house.setter = decorator = modifies the behavior of the method below it
    def house(self, house): # house = new value to set // self = current object
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house")
        self._house = house # _house = private attribute to store the value of house
  
       

# Main function to run the program
def  main():
    # Get a student object from user input
    student = get_students()
    student._house = "Number Four, Privet Drive"#directly accessing private attribute (not recommended)/ _ = don't touch what's private
 




    # Print the student object (which calls __str__)
    print(student)


# Function to get student details from user input
def get_students():
    # Prompt user for name
    name = input("Name: ")
    # Prompt user for house
    house = input("House: ")
    return Student(name,house)

#class = create your own data type

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
