import csv
"""Module for image brightness calculation."""
import numpy as np

from PIL import Image



def main():
    
    with open("images.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"])


def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255
    return brightness


    
    
if __name__ == "__main__":
   main()
