# pizza

import sys
import csv
from tabulate import tabulate


def main():
    # Check if is a valid csv
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

    # Call csv to dict function
    table = csv_to_dict()

    # print table as tabulate
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def csv_to_dict():
    # Empty List
    pizzas_table = []

    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                pizzas_table.append(row)
            return pizzas_table

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


if __name__ == "__main__":
    main()
