def main():
    with open("miraa.txt", "r") as miraa:
        content = miraa.readlines()
        declaração = content[33:35]
        print(declaração[0])
        print(declaração[1])
        #print(len(content))# Print the total number of lines in the file



if __name__ == "__main__":
    main()