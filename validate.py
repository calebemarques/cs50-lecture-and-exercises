 #Import regular expressions module
#from email_validator import validate_email, EmailNotValidError
import  re
 #Validate Email Address
email = input("Enter your email address: ").strip()

 #Simple regex pattern to check for "@" followed by at least two characters
if re.search(r"^m\w+@(\w+\.)?\w+\.(com|edu|gov|net|gov|br|aluno|ce)$", email, re.IGNORECASE): #Check if email matches the pattern, ".+@.+" = at least one character before and after "@", ".*@.*" = zero or more characters before and after "@"


    """
        re.IGNORECASE makes the regex case-insensitive, so it matches both uppercase and lowercase letters.
    
        
        This regex pattern checks for a basic email structure:
        
        - Starts with one or more alphanumeric characters (letters, digits, and underscores).
        - Followed by the "@" symbol.
        - Followed by one or more alphanumeric characters.
        - Ends with a  domain suffix such as ".com", ".edu", ".gov", ".net", ".br", ".aluno", or ".ce".
        Note that this is a simplified validation and may not cover all valid email formats or exclude all invalid ones.
        For more comprehensive email validation, consider using specialized libraries or more complex regex patterns.
    """
# comment section end

################################## Regex Pattern Explanation ##################################
# ^\w+ = start with one or more alphanumeric characters (letters, digits, and underscores)
# @ = followed by "@" symbol
# \w+ = followed by one or more alphanumeric characters (letters, digits, and underscores)
# \.com$ = ends with ".com"
# "[a-z]" = lowercase letters, "[A-Z]" = uppercase letters, "[0-9]" = digits,
# \w = alphanumeric characters (letters, digits, and underscores)
# ^ = start of the string , $ = end of the string ,
# \s = whitespace characters , \S = non-whitespace characters ,
# \d = digits , \D = non-digits ,
# . = any character except newline ,
# * = zero or more occurrences of the preceding element ,
# + = one or more occurrences of the preceding element ,
# ? = zero or one occurrence of the preceding element ,
# {n} = exactly n occurrences of the preceding element ,
# {n,} = n or more occurrences of the preceding element ,
# {n,m} = between n and m occurrences of the preceding element ,
# | = logical OR ,
# () = grouping ,
# (?: ) = non-capturing group ,
# [] = character class 
# [^@]+ = at least one character that is not "@" before the "@" symbol , [^@]+ = at least one character that is not "@" after the "@" symbol , \.edu$ = ends with ".edu" , \.com$ = ends with ".com"
     # ",{1}.*@.*" = exactly one "@" symbol with any characters before and after it

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