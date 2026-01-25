def main():
    # Main function to read from miraa.txt, extract specific lines, and write to ainda_bem.txt
    with open("miraa.txt", "r") as miraa:
        # Open the input file miraa.txt for reading
        content = miraa.readlines()
        # Read all lines from the file into a list
        declaração = content[33:49]
        # Extract lines 34-49 (0-based indices 33-48) into declaração
        print(declaração[0])
        # Print the first extracted line (line 34)
        print(declaração[1])
        # Print the second extracted line (line 35)

        #print(len(content))# Print the total number of lines in the file
    phrase1 = content[33]
    # Assign the 34th line to phrase1
    phrase2 = content[34]
    # Assign the 35th line to phrase2
    phrase3 = content[35]
    # Assign the 36th line to phrase3
    phrase4 = content[36]
    # Assign the 37th line to phrase4
    with open("ainda_bem.txt", "w") as ainda_bem:
        # Open the output file ainda_bem.txt for writing
        ainda_bem.writelines(declaração)
        # Write phrase1 and phrase2 concatenated to the output file


if __name__ == "__main__":
    main()
