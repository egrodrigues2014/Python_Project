from working import convert
import pytest


def main():
    ...


# Test letters upper and lower cases
def test_short_version():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_long_version():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_value_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()