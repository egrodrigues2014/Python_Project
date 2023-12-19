import re
import sys


def main():
    print(count(input("Text: ")))

#Um, thanks,..um...yumm um
def count(s):
    um_list = re.findall(r'\b\W*(um)\W*\b', s, re.IGNORECASE)
    return len(um_list)


if __name__ == "__main__":
    main()
