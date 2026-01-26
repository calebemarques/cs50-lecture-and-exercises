# Validate Email Address
email = input("Enter your email address: ").strip()

username, domain = email.split("@")
try:
    if username and "." in domain and len(domain.split(".")[-1]) >= 2: 
        print("Valid email address.")
    else:
        print("Invalid email address: Username part is empty.")
except ValueError:
    print("Invalid email address: Missing @ symbol or domain.")
# validate.py