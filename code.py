import re 
# Validate hexadecimal color codes
def main():
    code = input("hexadecimal color code: ")
    pattern = r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b$" #{6} quantifier for exactly 6 characters, {3} for exactly 3 characters
     #\b = word boundary , make sure no extra characters follow the code
     # "$" = match the end of the string
     # "^" = match the start of the string
    match = re.search(pattern, code)# Complete the regex pattern to validate hexadecimal color codes
    if match: # if match:
        print(f"Valid. Matched with {match.group(1)}")# Print whether the input is a valid hexadecimal color code
    else: # if not match:
        print(f"Invalid")
    # Example valid codes: #FFF, #123ABC, #abcdef



if __name__ == "__main__":
    main()