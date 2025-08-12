from numb3rs import validate


def test_len():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False


def test_lim():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_input():
    assert validate("cat") == False
    assert validate("0.275.0.300") == False
