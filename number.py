def main():
    x = get_password("What is the password? ")
    print(f"Access granted with password: {x}")

def get_password(prompt):
    while True:

        try:
            password = ["18","03","2008"]
            x = int(input(prompt))

            if password is None and str(x) not in password:
                raise ValueError
            elif str(x) == password[0:9]:
                print(f"password is {x}")
        except ValueError:
            print("password incorrect!")
        except KeyboardInterrupt:
            print("\nProcess interrupted.")
        else:
            break
    return x

main()