#OOP = Object Oriented Programming = create your own data types

class Student:
    def __init__(self, name, house, first,last,middle):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin" ]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house       
        self.first = first
        self.last = last
        self.middle = middle

  
def  main():
    student = get_students()
    print(f"{student.name} from {student.house}")


def get_students():
    name = input("Name: ")
    house = input("House: ")
    middle = input("Middle: ")
    first = input("First: ")
    last = input("Last: ")
    try:
        Student(name, house, first, last)
    except ValueError:
        print("Invalid input")

    return Student(name,house, first, last)

#class = create your own data type



if __name__ == "__main__":    
    main()