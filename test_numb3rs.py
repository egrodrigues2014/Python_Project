# Test_numb3rs.py

from numb3rs import validate


def main():
    test_format()
    test_range()


def test_range():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False


def test_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"0.0.0.256") == False
    assert validate(r"0.0.256.0") == False
    assert validate(r"0.256.0.0") == False
    assert validate(r"256.0.0.0") == False
    assert validate(r"cat.cat.cat.cat") == False
    assert validate(r"1000.0.0.0") == False


if __name__ == "__main__":
    main()
