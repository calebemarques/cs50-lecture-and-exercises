from hello_ import hello

students = ["Hermione", "Harry", "Ron"]

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in students:
         assert hello(name) == f"hello, {name}"