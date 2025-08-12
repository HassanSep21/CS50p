from fuel import convert, gauge
import pytest


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("4/1")


def test_int():
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_E():
    assert gauge(1) == "E"
    assert gauge(2) == "2%"


def test_F():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
