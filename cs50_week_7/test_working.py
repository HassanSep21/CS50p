from working import convert
import pytest


def test_hours():
    assert convert("9:00 AM to 10:00 AM") == "09:00 to 10:00"
    assert convert("1 PM to 2 PM") == "13:00 to 14:00"


def test_minutes():
    assert convert("9:05 AM to 9:10 AM") == "09:05 to 09:10"
    assert convert("1:10 PM to 1:15 PM") == "13:10 to 13:15"


def test_error():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:69 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 15:00 PM")