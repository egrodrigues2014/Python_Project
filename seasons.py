from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")

    # Check users input
    try:
        year, month, day = check_user_birthday(birthday)
        if int(month) > 12 or int(day) > 31:
            sys.exit("Invalid date")

    except:
        sys.exit("Invalid date")


    # Convert birthdate from users input to date format
    date_of_bday = date(int(year), int(month), int(day))
    date_of_today = date.today()
    # date_of_today = date(2000,1,1)

    # Create a timedelta Object https://docs.python.org/3/library/datetime.html#timedelta-objects
    timedelta_diff = date_of_today - date_of_bday
    # print("Timedelta", timedelta_diff)

    # Get total of minutes from the difference days
    total_minutes = timedelta_diff.days * 24 * 60
    # print("Total minutes:", total_minutes)

    words = p.number_to_words(total_minutes, andword="")
    print(words.capitalize() + " minutes")


def check_user_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date, re.IGNORECASE):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
