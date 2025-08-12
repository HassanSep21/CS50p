def main():
    while True:
        try:
            f = input("Fraction: ")
            perc = convert(f)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(perc))


def convert(fraction):
    fraction = fraction.split("/")
    x, y = int(fraction[0]), int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return round(100 * (x / y))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
