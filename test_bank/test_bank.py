from bank import value

def main():
    test_hello()
    test_h()
    test_not_h()
    test_case_insensitivity()


def test_hello():
    assert value("hello there") == 0

def test_h():
    assert value("hi there") == 20

def test_not_h():
     assert value("What's your name?") == 100

def test_case_insensitivity():
     assert value("WHAT's your name?") == 100
     assert value("HELLO there") == 0
     assert value("HI there") == 20

if __name__ == "__main__":
    main()
