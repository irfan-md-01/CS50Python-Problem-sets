from plates import is_valid

def main():
    test_is_Valid()
    test_size()
    test_two_letters()
    test_punctuation()


def test_is_Valid():
    assert is_valid("AAA222") == True
    assert is_valid("AA2AA") == False
    assert is_valid("AA02AA") == False
    assert is_valid("AAA022") == False
    assert is_valid("CS05") == False

def test_size():
    assert is_valid("VANITYPLATES") == False
    assert is_valid("VS") == True
    assert is_valid("V") == False

def test_two_letters():
     assert is_valid("BB605") == True
     assert is_valid("B605") == False
     assert is_valid("CS50") == True
     assert is_valid("50") == False

def test_punctuation():
     assert is_valid("HELLO, WORLD") == False
     assert is_valid("PI3.14") == False
    #  assert is_valid("HELLO there") == 0
    #  assert is_valid("HI there") == 20

if __name__ == "__main__":
    main()
