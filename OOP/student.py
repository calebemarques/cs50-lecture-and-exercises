#OOP = Object Oriented Programming = create your own data types
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house       

  
def  main():
    student = get_students()
    print(f"{student.name} from {student.house}")


def get_students():
    name = input("Name: ")
    house = input("House: ")
    Student(name,house)
    return student

#class = create your own data type



if __name__ == "__main__":    
    main()