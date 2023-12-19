# Fuel Gauge


def main():

    gas = input("Fraction:")
    result = convert(gas)
    per = gauge(result)
    if type(per) is int:
        print(f"{per}%")
    else:
        print(per)


def convert(fraction):

    while True:
        try:
            x, y = fraction.split('/')
            result = int(x) / int(y)
            if 0 < result <= 1:
                return result
            else:
                fraction = input("Fraction:")
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <= 0.01:
        return "E"
    elif percentage >= 0.99:
        return "F"
    else:
        return int(percentage * 100)


if __name__ == "__main__":
    main()






