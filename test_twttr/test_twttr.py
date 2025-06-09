from twttr import shorten

def main():
    test_twttr()
    test_numbers()
    test_punc()


def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("twitter123") == "twttr123"

def test_punc():
     assert shorten("What's your name?") == "Wht's yr nm?"

if __name__ == "__main__":
    main()
