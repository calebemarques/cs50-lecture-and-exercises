import re 

locations = {"+1": "United States/Canada",
             "+44": "United Kingdom",
             "+91": "India",
             "+81": "Japan",
             "+55": "Brazil",
             "+61": "Australia",
             "+505": "Nicaragua"
             }
def main():
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}" #\d{1,3} means 1 to 3 digits "\d" means digit , \d{3} means exactly 3 digits
    number = input("Number:  ")

    match = re.search(pattern, number)
    if match: 
        country_code = match.group(1)
        print(f"Valid number from {locations.get(country_code, 'Unknown Country')}")
    else:
        print("Invalid number")



if __name__ == "__main__":
    main()    