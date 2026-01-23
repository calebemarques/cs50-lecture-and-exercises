"""Module for image brightness calculation."""
import numpy as np
import csv
from PIL import Image

names = []

def main():
    catchname()
    with open("images.csv", "r") as file:
         reader = csv.DictReader(file)
         for row in reader:
             print(row)
         
def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255
    return brightness

def catchname(name):
    name = input("name: ")
    names.append(name)
    print(names)

main()