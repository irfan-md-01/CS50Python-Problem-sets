from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar = Jar(5)
    assert jar.capacity == 5
    jar = Jar(45)
    assert jar.capacity == 45

def test_str():

    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():

    jar = Jar(15)
    jar.deposit(13)
    assert jar.size == 13
    jar.deposit(1)
    assert jar.size == 14
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_withdraw():

    jar = Jar(15)
    jar.deposit(13)
    jar.withdraw(10)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(12)
