def main():
    with open("miraa.txt", "r") as miraa:
        content = miraa.readlines()
        declaração = content[33:35]
        print(declaração[0])
        print(declaração[1])

        #print(len(content))# Print the total number of lines in the file
    phrase1 = content[33]
    phrase2 = content[34]
    with open("ainda_bem.txt", "w") as ainda_bem:
        nessemundo.write(phrase1)
        nessemundo.write(phrase2)


if __name__ == "__main__":
    main()