from twttr import shorten


def test_upper():
    assert shorten("AMONGUS") == "MNGS"


def test_lower():
    assert shorten("amongus") == "mngs"


def test_both():
    assert shorten("Amongus") == "mngs"


def test_pun():
    assert shorten("amongus??") == "mngs??"


def test_num():
    assert shorten("amongus123") == "mngs123"