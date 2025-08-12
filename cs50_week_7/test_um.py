from um import count


def test_case():
    assert count("UM, hello, um, wolrd") == 2


def test_word():
    assert count("one, um, cucumber please") == 1


def test_char():
    assert count("...um...") == 1
    