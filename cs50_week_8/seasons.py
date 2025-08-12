from datetime import date
import inflect
import sys


p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    timedelta = date.today() - get_date(birth_date)
    minutes = get_minutes(timedelta.days)
    print(p.number_to_words(minutes, andword="").capitalize(), "minutes")


def get_date(birth_date):
    try:
        return date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(time):
    return time * 24 * 60


if __name__ == "__main__":
    main()
