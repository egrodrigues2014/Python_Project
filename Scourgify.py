# Scourgify

import sys
import csv


def main():

    check_command_line_ags()

    # Read data from csv file
    csv_into_dict = read_csv_file()

    # Write data into a new csv file
    write_to_csv_file(csv_into_dict)

def check_command_line_ags():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".csv"):
        print(f"{sys.argv[1]} is not a CSV file")
        sys.exit()
    elif not sys.argv[2].endswith(".csv"):
        print(f"{sys.argv[2]} is not a CSV file")
        sys.exit()

def read_csv_file():

    name_house_list = []
    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name_house_list.append(row)
            return name_house_list

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit()

def write_to_csv_file(dict_to_wite):
    get_data =[]

    with open(sys.argv[2], "w", newline='') as csv_write_file:
        writer = csv.DictWriter(csv_write_file, fieldnames = ['first', 'last', 'house'])
        writer.writeheader()
        for item in dict_to_wite:
            last, first = item['name'].split(", ")
            writer.writerow({'first': first, 'last': last, 'house': item['house']})
            # print(f"{item['name']} : First: {first} , Last: {last}")


if __name__ == "__main__":
    main()
