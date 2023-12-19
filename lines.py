# lines


import sys


def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()

    print(count_lines())


def count_lines():
    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            for row in file:
                if "#" in row[0] or len(row.strip()) == 0:
                    continue
                else:
                    count += 1

            return count


    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


if __name__ == "__main__":
    main()
