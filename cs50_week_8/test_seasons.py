from seasons import get_date, get_minutes
from datetime import date

def test_get_date():
    # Test with valid date
    assert get_date("2022-01-01") == date(2022, 1, 1)


def test_get_minutes():
    assert get_minutes(365) == 525600
