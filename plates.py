# Vanity Plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not s[:2].isalpha():
        return False

    # “No periods, spaces, or punctuation marks are allowed.”

    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example,
    # AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first
    # number used cannot be a ‘0’.”

    for i in range(len(s)):
        # print(i, s[i], s[i].isalpha())
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            else:
                break

    # Validar que no hay letras despues de numeros
    for ind in range(2, len(s)):
        if s[ind].isalpha() == False and s[ind] != s[-1]:
            if s[ind + 1].isalpha():
                return False

    # If pass all the tests
    return True


if __name__ == "__main__":
    main()
