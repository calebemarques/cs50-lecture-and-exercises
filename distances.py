distances = {
   "Voyager 1": "152",
    "Voyager 2": "128",
    "Pioneer 10": "122",
    "New Horizons": "50 AU",
    "Pioneer 11": "109"
}


def main():
     spacecraft = input("Enter the name of the spacecraft: ")

     try:
         
         au = float(distances[spacecraft])
     except ValueError:
         print(f"Can't convert '{distances[spacecraft]}' to  a  float")
         return
     except KeyError:
         print(f"'{spacecraft}' not found.")
         return
     
     m = convert(au)
     print(f"{m} m away")

def convert(au):
    return au * 149597870700
   




main()
