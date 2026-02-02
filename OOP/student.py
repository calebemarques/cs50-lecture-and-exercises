#OOP = Object Oriented Programming = create your own data types
class Student:
    ... # TODO        

  
def  main():
    student = get_students()
    print(f"{student.name} from {student.house}")


def get_students():
    student = Student()# create an instance of the Student class // an object
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

#class = create your own data type



if __name__ == "__main__":    
    main()