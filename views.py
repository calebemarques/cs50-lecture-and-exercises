
import csv
"""Module for image brightness calculation."""
# Import numpy for numerical operations and array manipulation
import numpy as np

# Import Image from PIL (Pillow) for image processing
from PIL import Image



def main():
    # Open the CSV file that contains image metadata (IDs and other information)
    with open("images.csv", "r", encoding="utf-8") as views , open("analysis.csv", "w", encoding="utf-8") as analysis:
        # Create a CSV reader that treats the first row as column headers (DictReader)
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        # Loop through each row in the CSV file
        for row in reader:
            row["brightness"] = round (calculate_brightness(f"{row["id"]}.jpeg"),2)
            
            writer.writerow(row)
            # Call calculate_brightness function with the image filename (ID + .jpeg extension)
            
            """ 
           writer.writerow({
                "id": row["id"],
                "english_title": row["english_title"],
                "portuguese_title": row["portuguese_title"],
                
                "brightness": round(brightness, 2)
                             })"""
            # Print the image ID to track progress
            print(row["id"])
            # Print the calculated brightness value (0.0 = dark, 1.0 = bright)
           # print(f"Brightness: {row}")
           # print(round(brightness, 2))# Round brightness to 2 decimal places for cleaner output

def calculate_brightness(filename):
    # Open the image file using PIL and use 'with' to ensure it closes properly
    with Image.open(filename) as img:
        # Convert the image to grayscale ("L" mode) which gives luminance values (0-255)
        # Then convert to numpy array for mathematical operations
        # Calculate the mean (average) of all pixel brightness values
        # Divide by 255 to normalize the result to a 0.0 to 1.0 scale
        brightness = np.mean(np.array(img.convert("L"))) / 255
    # Return the normalized brightness value
    return brightness


    
    
# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
   # Call the main function to start the program
   main()
