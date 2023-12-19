# Outdated

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

list1 = ["9/8/1636", "September 8, 1636", "23/6/1912", "December 80, 1980", "10/17/1991"]

for user_date in list1:

    try:
        if "/" in user_date:
            m, d, y = user_date.split("/")
            if int(m) > 12 or int(d) > 31 or int(y) < 0:
                print(f"ERROR in {user_date}")
                continue
        else:
            m, d, y = user_date.split()
            d = d.strip(" ,")
            if m.capitalize() not in months or int(d) > 31 or int(y) < 0:
                print(f"ERROR in {user_date}")
                continue
            else:
                m = months.index(m.capitalize()) + 1
    except ValueError:
        print(f"Error in {user_date}")

    else:
        print(f"{int(y):0004}-{int(m):02}-{int(d):02}")
