# Test Fuel

import pytest
from fuel import convert, gauge


def main():
    test_zero_division()
    test_correct_ouput()


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_correct_ouput():
    assert convert("1/4") == 0.25 and gauge(0.25) == 25
    assert convert("1/100") == 0.01 and gauge(0.01) == "E"
    assert convert("99/100") == 0.99 and gauge(0.99) == "F"


main()
