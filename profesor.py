#profesor

import random

def main():
    count = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        for i in range(3):
            answer = int(input(f"{x} + {y} = "))
            if answer == result:
                count += +1
                break
            else:
                if i == 2:
                    print(f"{x} + {y} = {result}")
                else:
                    print("EEE")

    print("Score: ",count)

def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if n not in [1,2,3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()