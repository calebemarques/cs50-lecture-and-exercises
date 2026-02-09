#OOP = Object Oriented Programming = create your own data types

# Define the Student class to represent a student with name and house
from re import match
from unittest import case


class Student:
    # Constructor method to initialize a Student object
    # Parameters: name (string), house (string)
    def __init__(self, name, house):
       
       
        self.name = name
        self.house = house

 
      # Method to return a string representation of the Student object
    def __str__(self):
        # Return a formatted string with the student's name and hous4
        return f"{self.name} from {self.house}" 
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)

    
  
    
# Main function to run the program
def  main():
    # Get a student object from user input
    student = Student.get()
    # Print the student object (which calls __str__)
    print(student)
   

#class = create your own data type

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
