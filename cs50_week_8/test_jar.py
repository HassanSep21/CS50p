from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    jar = Jar()
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    with pytest.raises(ValueError):
        jar.deposit(5)
    assert jar.deposit(4) == 4



def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    assert jar.withdraw(2) == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
