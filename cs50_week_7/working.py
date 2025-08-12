import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        flag = True
        result = ""
        matches = re.search(
            r"(\d{1,2}(?::?\d{2})? [AP]M) to (\d{1,2}(?::?\d{2})? [AP]M)", s
        )
        for match in matches.groups():
            time, setting = match.split(" ")
            if ":" in time:
                hours, minutes = time.split(":")
                if int(minutes) >= 60 or int(hours) > 12:
                    raise ValueError
            else:
                hours = time
                minutes = "00"
            if int(hours) == 12 and setting == "AM":
                hours = 0
            elif setting == "AM":
                hours = int(hours)
            elif int(hours) == 12 and setting == "PM":
                hours == int(hours)
            else:
                hours = int(hours) + 12
            result += f"{hours:02}:{int(minutes):02}"
            if flag:
                result += " to "
                flag = False
        return result
    except (ValueError, AttributeError):
        raise ValueError


if __name__ == "__main__":
    main()
