from seasons import check_user_birthday


def main():
    test_check_bday()


def test_check_bday():
    assert check_user_birthday("1991-10-17") == ("1991", "10", "17")
    assert check_user_birthday("cat") == None

if __name__ == "__main__":
    main()