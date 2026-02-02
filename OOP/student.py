def  main():
    student = get_students()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student["house"]}")


def get_students():
   name = input("Name: ")
   house = input("House:")
   return{"name": name,"house": house}  




if __name__ == "__main__":    
    main()