from numb3rs import validate

def main():
    test_valid()
    test_inValid()

def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_inValid():
    assert validate("1.2.3.1000") == False
    assert validate("cat.2.3.1000") == False
    assert validate("100.899.3.100") == False
    assert validate("100.8.398.100") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()
