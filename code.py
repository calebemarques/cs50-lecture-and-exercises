import re 
# Validate hexadecimal color codes
def main():
    code = input("hexadecimal color code: ")
    pattern = r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b"  #\b = word boundary , make sure no extra characters follow the code
    match = re.search(pattern, code)# Complete the regex pattern to validate hexadecimal color codes
    if match: # if match:
        print(f"Valid. Matched with {match.group(1)}")# Print whether the input is a valid hexadecimal color code
    else: # if not match:
        print(f"Invalid")
    # Example valid codes: #FFF, #123ABC, #abcdef



if __name__ == "__main__":
    main()