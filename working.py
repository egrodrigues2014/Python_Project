# 9:00 AM to 5:00 PM
# ^([0-9]+):([0-9]+) (AM|PM) to ([0-9]+):([0-9]+) (AM|PM)$

# Ambas
# 9 AM to 5 PM
# 9:00 AM to 5:00 PM
# r"^([0-9]+)(:([0-9]+))? (AM|PM) to ([0-9]+)(:([0-9]+))? (AM|PM)$"

# Test
# 9 AM to 5 PM
# 9:00 AM to 5:00 PM
# 10 PM to 8 AM
# 10:30 PM to 8:50 AM
# 9:60 AM to 5:60 PM
# 9 AM - 5 PM
# 09:00 AM - 17:00 PM


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r"^([0-9]+)(:([0-9]+))? (AM|PM) to ([0-9]+)(:([0-9]+))? (AM|PM)$", s, re.IGNORECASE):
        # Defining start hour
        if matches.group(4).upper() == "PM":
            if int(matches.group(1)) == 12:
                start_hour = 12
            else:
                start_hour = int(matches.group(1)) + 12
        else:
            if int(matches.group(1)) == 12:
                start_hour = 0
            else:
                start_hour = int(matches.group(1))

        # Defining start minuts based on input string
        if matches.group(2) is None:
            start_min = 0
        else:
            start_min = int(matches.group(3))

        # Defining end hour
        if matches.group(8).upper() == "PM":
            if int(matches.group(5)) == 12:
                end_hour = 12
            else:
                end_hour = int(matches.group(5)) + 12
        else:
            if int(matches.group(5)) == 12:
                end_hour = 0
            else:
                end_hour = int(matches.group(5))

        # Defining end minuts based on input string
        if matches.group(6) is None:
            end_min = 0
        else:
            end_min = int(matches.group(7))

        # Check for Values errors
        if start_hour > 23 or end_hour > 23 or start_min > 59 or end_min > 59:
            raise ValueError

        return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
