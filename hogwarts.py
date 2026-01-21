students = [
    {"name": "Harry Potter", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione Granger", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron Weasley", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco Malfoy", "house": "Slytherin", "patronus": None},
    {"name": "Luna Lovegood", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Cedric Diggory", "house": "Hufflepuff", "patronus": "Badger"},
]

for student in students:
    print(student["name"],student["house"],student["patronus"], sep=", ")