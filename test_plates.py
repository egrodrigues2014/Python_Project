# Test_plates

from plates import is_valid


def main():
    test_len()
    test_first2digits()
    test_no_marks()


def test_len():
    assert is_valid("C") == False
    assert is_valid("CS5000") == True
    assert is_valid("CS50PPPP") == False

def test_first2digits():
    assert is_valid("AA50") == True
    assert is_valid("1A50") == False
    assert is_valid("1150") == False
    assert is_valid("A150") == False


def test_no_marks():
    assert is_valid(",") == False
    assert is_valid(".") == False
    assert is_valid("!") == False
    assert is_valid(" ") == False


def test_number_not_in_the_middle():
    assert is_valid("AA01A") == False
    assert is_valid("AA11A") == False
    assert is_valid("AA21A") == False
    assert is_valid("AA91A") == False


main()
