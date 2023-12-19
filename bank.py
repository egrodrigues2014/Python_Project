# Home Federal Savings Bank

def main():
    phrase = input("Greeting:")
    print(f"${value(phrase)}")


def value(greeting):
    g = greeting.lower().strip()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
