from plates import is_valid


def test_no_char():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("PPP123") == True
    assert is_valid("PPPP123") == False


def test_alpha():
    assert is_valid("CS50") == True
    assert is_valid("PPP50") == True
    assert is_valid("P50") == False


def test_pos_no():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("CS5S0") == False


def test_zero():
    assert is_valid("CC11") == True
    assert is_valid("CS01") == False


def test_punc():
    assert is_valid("PP11") == True
    assert is_valid("PP, ?1") == False