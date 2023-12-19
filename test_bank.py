# test_bank

from bank import value


def main():
    test_Hello()
    test_startwith_h()
    test_other_cases()


def test_Hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_startwith_h():
    assert value("How you doing?") == 20
    assert value("HECTOR") == 20
    assert value("hector") == 20
    assert value("Hector") == 20


def test_other_cases():
    assert value("What's happening?") == 100
    assert value("Good Mornig") == 100
    assert value("Bye") == 100


if __name__ == "__main__":
    main()
