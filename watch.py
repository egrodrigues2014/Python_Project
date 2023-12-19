# Watch.py

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"(https?:\/\/)?(?:www\.)?youtube\.com\/embed\/(\w+)", s, re.IGNORECASE):
        return matches.group(1) + "youtu.be/" + matches.group(2)
    else:
        return None


if __name__ == "__main__":
    main()