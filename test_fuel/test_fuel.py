from fuel import convert, gauge
from pytest import raises

def main():
    test_convert()
    test_gauge()
    test_exception()


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(78) == "78%"

def test_exception():
     with raises(ZeroDivisionError):
          convert("8/0")
     with raises(ValueError):
          convert("8/6")
          convert("8/j")
          convert("j/8")
          convert("j/j")


if __name__ == "__main__":
    main()
