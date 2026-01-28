 #Import regular expressions module
#from email_validator import validate_email, EmailNotValidError
import  re
 #Validate Email Address
email = input("Enter your email address: ").strip()

# #Simple regex pattern to check for "@" followed by at least two characters
if re.search(r"^.+@.+\.edu$", email): #Check if email matches the pattern, ".+@.+" = at least one character before and after "@", ".*@.*" = zero or more characters before and after "@"
    print("Valid email address.") #If it matches, print valid message
else: #If it doesn't match
    print("Invalid email address.") #Print invalid message

    """
      Python has many ways to solve a problem like email validation.
     Python has different ways to validate email addresses, including using libraries like `validate_email` or `email-validator` for more comprehensive checks.
     However, for basic validation, regex can be sufficient.
     Note that this regex is quite simple and may not cover all valid email formats or exclude all invalid ones.
     For production-level code, consider using more robust validation methods.
     let me show you an example using the `email-validator` library:
     You can install it via pip:
     pip install email-validator
     Then you can use it as follows:
     
     try:
         valid = validate_email(email)
         email = valid.email
         print("Valid email address.")
     except EmailNotValidError as e:
         print(str(e))
     This approach provides a more comprehensive validation of email addresses.
     """